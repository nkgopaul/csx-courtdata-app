import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import spacy
from spacy.matcher import PhraseMatcher
import json
from constants import LABELS, SQL_MAPPING
import http.client
from dotenv import load_dotenv

application = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__), '.') 
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

application.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
application.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
application.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
application.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')

mysql = MySQL()
mysql.init_app(application)
conn = mysql.connect()
cursor = conn.cursor()

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)

def add_legal_patterns():
    for label, tokens in LABELS.items():
        for token in tokens:
            matcher.add(label, None, nlp(token))

@application.route("/")
def main():
    return render_template('index.html')

@application.route("/legal_query", methods=['POST'])
def legal_query():
    doc = nlp(request.get_json()['question'])
    matches = matcher(doc)
    matched_tags = [nlp.vocab.strings[i[0]] for i in matches]
    matched_tags = sorted(set(matched_tags))

    print(matched_tags)

    if not matched_tags:
        return render_template('no_query_found.html')

    try:
        matched_query = SQL_MAPPING[' '.join(matched_tags)]
    except KeyError:
        return render_template('no_query_found.html')

    cursor.execute(matched_query['sql'])

    if(matched_query['template'] == 'heat_map.html'):
        labels = []
        data_labels = []
        data = []

        rows = cursor.fetchall()
        for i in range(1, len(cursor.description)):
            values = []
            for row in rows:
                if(i==1):
                    labels.append(row[0])
                values.append(float(row[i]))
            data_labels.append(cursor.description[i][0])
            data.append({
                'label': cursor.description[i][0],
                'data': values
            })
        
        data = json.dumps(data)
        print(data)
        print(labels)

        return render_template(matched_query['template'], title=matched_query['title'], data=data, labels=labels)

    labels = []
    data = []
    
    for row in cursor.fetchall():
        labels.append(row[0])
        for i in range(1, len(row)):
            data.append(row[i])
    return render_template(matched_query['template'], title=matched_query['title'], data=data, labels=labels, max=max(data))

if __name__ == "__main__":
    add_legal_patterns()
    application.run()