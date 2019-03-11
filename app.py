import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import spacy
from spacy.matcher import PhraseMatcher
import json
from constants import LABELS, SQL_MAPPING
import http.client
from dotenv import load_dotenv

app = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__), '.') 
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)

def add_legal_patterns():
    for label, tokens in LABELS.items():
        for token in tokens:
            matcher.add(label, None, nlp(token))

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/legal_query", methods=['POST'])
def legal_query():
    doc = nlp(request.get_json()['question'])
    matches = matcher(doc)
    matched_tags = [nlp.vocab.strings[i[0]] for i in matches]
    print(matched_tags)
    matched_tags = sorted(set(matched_tags))
    if not matched_tags:
        return render_template('no_query_found.html')
    
    print(matched_tags)

    try:
        matched_query = SQL_MAPPING[' '.join(matched_tags)]
    except KeyError:
        return render_template('no_query_found.html')

    print(matched_query['sql'])
    cursor.execute(matched_query['sql'])
    
    labels = []
    values = []
    for row in cursor.fetchall():
        labels.append(row[0])
        for i in range(1, len(row)):
            values.append(row[i])

    return render_template(matched_query['template'], title=matched_query['title'], values=values, labels=labels, max=max(values))

if __name__ == "__main__":
    add_legal_patterns()
    app.run()