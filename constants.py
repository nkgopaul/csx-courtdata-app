LABELS = {
    'SUM': ['total', 'total number', 'sum', 'total amount', 'number of', 'all'],
    'CASE': ['cases', 'case', 'caseload'],
    'TIME': ['time', 'over time', 'length'],
    'TYPE': ['type', 'types', 'kind', 'role'],
    'JUDGE': ['judge'],
    'GENDER': ['gender', 'sex', 'female', 'male'],
    'DISTRICT': ['district', 'state', 'jurisdiction'],
    'NOS': ['nature', 'suit', 'nature suit', 'nature of suit'],
    'ETHNICITY': ['ethnicity', 'race', 'white', 'black', 'hispanic', 'asian', 'causcasian'],
    'POLITICAL_PARTY': ['political party', 'republican', 'republicans', 'democrat', 'democrats', 'democratic', 'president', 'appointing president'],
    'ABA': ['ABA rating', 'aba', 'rating', 'ABA', 'American Bar Association'],
    'OUTCOME': ['case outcome', 'case outcomes', 'outcome', 'outcomes', 'result', 'results', 'judgement', 'judgements', 'ruling', 'rulings'],
    'WORK_RATE': ['work rate', 'rate'],
    'AVG': ['average'],
    'CORRELATION': ['correlation', 'relationship', 'between']
}


SQL_MAPPING = {  
   'CASE SUM TYPE':{  
        'title':'Total Number of Each Case Type (Criminal vs. Civil)',
        'sql':'SELECT type, COUNT(type) as case_type FROM cases GROUP BY type;',
        'template': 'bar_chart.html'
   },
   'CASE SUM TIME':{
        'title':'Number of Cases Over Time by Terminating Date',
        'sql': 'SELECT DATE_FORMAT(terminating_date,\'%Y-%m\') AS date, COUNT(*) AS total_cases FROM cases WHERE terminating_date IS NOT NULL GROUP BY date;',
        'template': 'line_chart.html'
   },
   'CASE SUM TIME TYPE':{  
        'question':'',
        'sql':''
   },
   'CASE JUDGE SUM':{  
        'title':'Assigned Caseload Per Judge',
        'sql':'SELECT CONCAT_WS(\' \', first_name, middle_name, last_name, suffix) as judge, COUNT(*) AS total_cases FROM cases JOIN federal_judges_demographics ON federal_judge_id=federal_judges_demographics.id GROUP BY federal_judge_id ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'CASE JUDGE SUM TYPE':{  
        'title':'Assigned Caseload Per Judge Type',
        'sql':'SELECT court_type, count(*) as total_cases FROM cases LEFT JOIN federal_judges_service ON cases.federal_judge_id=federal_judges_service.nid WHERE court_type IS NOT NULL GROUP BY court_type ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'CASE GENDER JUDGE SUM':{  
        'title':'Assigned Caseload Per Judge Gender',
        'sql':'SELECT gender, count(*) as total_cases FROM cases LEFT JOIN federal_judges_demographics ON cases.federal_judge_id=federal_judges_demographics.id WHERE gender IS NOT NULL GROUP BY gender ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'CASE ETHNICITY JUDGE SUM':{  
        'title':'Assigned Caseload Per Judge Ethnicity',
        'sql':'SELECT ethnicity, count(*) as total_cases FROM cases LEFT JOIN federal_judges_demographics ON cases.federal_judge_id=federal_judges_demographics.id WHERE ethnicity IS NOT NULL GROUP BY ethnicity ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'AVG CASE JUDGE SUM TYPE':{  
        'title':'Assigned Caseload Per Judge Type',
        'sql':'SELECT court_type, count(*) as total_cases FROM cases LEFT JOIN federal_judges_service ON cases.federal_judge_id=federal_judges_service.nid WHERE court_type IS NOT NULL GROUP BY court_type ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'AVG CASE GENDER JUDGE SUM':{  
        'title':'Average Caseload Per Judge Gender',
        'sql':'SELECT gender, IF(gender=\'Male\', count(*)/55, count(*)/17) as total_cases FROM cases LEFT JOIN federal_judges_demographics ON cases.federal_judge_id=federal_judges_demographics.id WHERE gender IS NOT NULL GROUP BY gender ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'AVG CASE ETHNICITY JUDGE SUM':{  
        'title':'Assigned Caseload Per Judge Ethnicity',
        'sql':'SELECT ethnicity, count(*) as total_cases FROM cases LEFT JOIN federal_judges_demographics ON cases.federal_judge_id=federal_judges_demographics.id WHERE ethnicity IS NOT NULL GROUP BY ethnicity ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'AVG CASE JUDGE POLITICAL_PARTY TIME':{  
      'title':'Average Case Length By Judge\'s Political Party (In Months)',
      'sql':'SELECT appointing_president_party, AVG(TIMESTAMPDIFF(MONTH, filing_date, terminating_date)) AS avg_case_length FROM cases INNER JOIN federal_judges_service ON cases.federal_judge_id=federal_judges_service.nid WHERE terminating_date IS NOT NULL GROUP BY appointing_president_party;',
      'template': 'bar_chart.html'
   },
   'ABA CASE JUDGE':{  
      'title':'',
      'sql':''
   },
   'NOS SUM':{  
      'title':'',
      'sql':''
   },
   'NOS TIME':{  
      'title':'',
      'sql':''
   },
   'DISTRICT NOS SUM':{  
      'title':'',
      'sql':''
   },
   'JUDGE NOS SUM':{  
      'title':'',
      'sql':''
   },
   'JUDGE NOS SUM TYPE':{  
      'title':'',
      'sql':''
   },
   'ETHNICITY JUDGE NOS SUM':{  
      'title':'',
      'sql':''
   },
   'GENDER JUDGE NOS SUM':{  
      'title':'',
      'sql':''
   },
   'JUDGE NOS POLITICAL_PARTY SUM':{  
      'title':'',
      'sql':''
   },
   'ABA JUDGE NOS SUM':{  
      'title':'',
      'sql':''
   },
   'CASE OUTCOME SUM':{  
      'title':'',
      'sql':''
   },
   'CASE OUTCOME TIME':{  
      'title':'',
      'sql':''
   },
   'CASE JUDGE OUTCOME SUM':{  
      'title':'',
      'sql':''
   },
   'CASE JUDGE OUTCOME SUM TYPE':{  
      'title':'',
      'sql':''
   },
   'CASE GENDER JUDGE OUTCOME SUM':{  
      'title':'',
      'sql':''
   },
   'CASE ETHNICITY JUDGE OUTCOME SUM':{  
      'title':'',
      'sql':''
   },
   'CASE JUDGE OUTCOME POLITICAL_PARTY SUM':{  
      'title':'',
      'sql':''
   },
   'ABA CASE JUDGE OUTCOME SUM':{  
      'title':'',
      'sql':''
   },
   'JUDGE TIME WORK_RATE':{  
      'title':'',
      'sql':''
   },
   'JUDGE WORK_RATE':{  
      'title':'',
      'sql':''
   },
   'GENDER JUDGE WORK_RATE':{  
      'title':'',
      'sql':''
   },
   'ETHNICITY JUDGE WORK_RATE':{  
      'title':'',
      'sql':''
   },
   'JUDGE POLITICAL_PARTY WORK_RATE':{  
      'title':'',
      'sql':''
   },
   'ABA JUDGE WORK_RATE':{  
      'title':'',
      'sql':''
   },
   'AVG CASE TIME':{  
      'title':'',
      'sql':''
   },
   'AVG CASE JUDGE TIME':{  
      'title':'',
      'sql':''
   },
   'AVG CASE JUDGE TIME TYPE':{  
      'title':'',
      'sql':''
   },
   'AVG CASE GENDER JUDGE TIME':{  
      'title':'',
      'sql':''
   },
   'AVG CASE ETHNICITY JUDGE TIME':{  
      'title':'',
      'sql':''
   },
   'ABA AVG CASE JUDGE TIME':{  
      'title':'',
      'sql':''
   },
   'AVG CASE DISTRICT TIME':{  
      'title':'',
      'sql':''
   },
   'CORRELATION GENDER JUDGE NOS':{
      'title':'Correlation Between Nature of Suit and Judge Gender',
      'sql': 'SELECT title, ROUND((SUM(IF(gender=\'Male\', 1, 0))/22762)*100, 2) AS Male, ROUND((SUM(IF(gender=\'Female\', 1, 0))/8075)*100, 2) AS Female FROM federal_judges_demographics INNER JOIN cases ON federal_judges_demographics.id=cases.federal_judge_id INNER JOIN nature_of_suit ON code=nos_code GROUP BY nos_code;',
      'template': 'heat_map.html'
   },
   'CASE CORRELATION GENDER JUDGE OUTCOME':{
      'title': 'Correlation Between Case Outcome and Judge Gender',
      'sql': 'SELECT result, ROUND((SUM(IF(gender=\'Male\', 1, 0))/22762)*100, 2) AS Male, ROUND((SUM(IF(gender=\'Female\', 1, 0))/8075)*100, 2) AS Female FROM federal_judges_demographics INNER JOIN cases ON federal_judges_demographics.id=cases.federal_judge_id WHERE result<>\"CRIMINAL\" GROUP BY result;',
      'template': 'heat_map.html'
   },
   'CASE CORRELATION GENDER JUDGE TYPE': {
      'title': 'Correlation Between Case Type and Judge Gender',
      'sql': 'SELECT type, ROUND((SUM(IF(gender=\'Male\', 1, 0))/22762)*100, 2) AS Male, ROUND((SUM(IF(gender=\'Female\', 1, 0))/8075)*100, 2) AS Female FROM federal_judges_demographics INNER JOIN cases ON federal_judges_demographics.id=cases.federal_judge_id GROUP BY type;',
      'template': 'heat_map.html'
   },
   'CORRELATION JUDGE POLITICAL_PARTY NOS':{
      'title':'Correlation Between Nature of Suit and Judge Gender',
      'sql': 'SELECT title, ROUND((SUM(IF(appointing_president_party=\'Democratic\', 1, 0))/21940)*100, 2) AS Democratic, ROUND((SUM(IF(appointing_president_party=\'Republican\', 1, 0))/10077)*100, 2) AS Republican FROM federal_judges_service INNER JOIN cases ON nid=federal_judge_id INNER JOIN nature_of_suit ON code=nos_code GROUP BY nos_code;',
      'template': 'heat_map.html'
   },
   'CASE CORRELATION JUDGE OUTCOME POLITICAL_PARTY':{
      'title': 'Correlation Between Case Outcome and Judge Gender',
      'sql': 'SELECT result, ROUND((SUM(IF(appointing_president_party=\'Democratic\', 1, 0))/21940)*100, 2) AS Democratic, ROUND((SUM(IF(appointing_president_party=\'Republican\', 1, 0))/10077)*100, 2) AS Republican FROM federal_judges_service INNER JOIN cases ON nid=federal_judge_id WHERE result<>\"CRIMINAL\" GROUP BY result;',
      'template': 'heat_map.html'
   },
   'CASE CORRELATION JUDGE POLITICAL_PARTY TYPE': {
      'title': 'Correlation Between Case Type and Judge Gender',
      'sql': 'SELECT type, ROUND((SUM(IF(appointing_president_party=\'Democratic\', 1, 0))/21940)*100, 2) AS Democratic, ROUND((SUM(IF(appointing_president_party=\'Republican\', 1, 0))/10077)*100, 2) AS Republican FROM federal_judges_service INNER JOIN cases ON nid=federal_judge_id GROUP BY type;',
      'template': 'heat_map.html'
   }
}