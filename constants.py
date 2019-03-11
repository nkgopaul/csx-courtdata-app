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
    'AVG': ['average']
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
        'sql':'SELECT IFNULL(court_type, \'Uncategorized\'), count(*) as total_cases FROM cases LEFT JOIN federal_judges_service ON cases.federal_judge_id=federal_judges_service.nid GROUP BY court_type ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'CASE GENDER JUDGE SUM':{  
        'title':'Assigned Caseload Per Judge Gender',
        'sql':'SELECT IFNULL(gender, \'Uncategorized\'), count(*) as total_cases FROM cases LEFT JOIN federal_judges_demographics ON cases.federal_judge_id=federal_judges_demographics.id GROUP BY gender ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'CASE ETHNICITY JUDGE SUM':{  
        'title':'Assigned Caseload Per Judge Ethnicity',
        'sql':'SELECT IFNULL(ethnicity, \'Uncategorized\'), count(*) as total_cases FROM cases LEFT JOIN federal_judges_demographics ON cases.federal_judge_id=federal_judges_demographics.id GROUP BY ethnicity ORDER BY total_cases DESC;',
        'template': 'bar_chart.html'
   },
   'CASE JUDGE POLITICAL_PARTY':{  
      'question':'',
      'sql':''
   },
   'ABA CASE JUDGE':{  
      'question':'',
      'sql':''
   },
   'NOS SUM':{  
      'question':'',
      'sql':''
   },
   'NOS TIME':{  
      'question':'',
      'sql':''
   },
   'DISTRICT NOS SUM':{  
      'question':'',
      'sql':''
   },
   'JUDGE NOS SUM':{  
      'question':'',
      'sql':''
   },
   'JUDGE NOS SUM TYPE':{  
      'question':'',
      'sql':''
   },
   'ETHNICITY JUDGE NOS SUM':{  
      'question':'',
      'sql':''
   },
   'GENDER JUDGE NOS SUM':{  
      'question':'',
      'sql':''
   },
   'JUDGE NOS POLITICAL_PARTY SUM':{  
      'question':'',
      'sql':''
   },
   'ABA JUDGE NOS SUM':{  
      'question':'',
      'sql':''
   },
   'CASE OUTCOME SUM':{  
      'question':'',
      'sql':''
   },
   'CASE OUTCOME TIME':{  
      'question':'',
      'sql':''
   },
   'CASE JUDGE OUTCOME SUM':{  
      'question':'',
      'sql':''
   },
   'CASE JUDGE OUTCOME SUM TYPE':{  
      'question':'',
      'sql':''
   },
   'CASE GENDER JUDGE OUTCOME SUM':{  
      'question':'',
      'sql':''
   },
   'CASE ETHNICITY JUDGE OUTCOME SUM':{  
      'question':'',
      'sql':''
   },
   'CASE JUDGE OUTCOME POLITICAL_PARTY SUM':{  
      'question':'',
      'sql':''
   },
   'ABA CASE JUDGE OUTCOME SUM':{  
      'question':'',
      'sql':''
   },
   'JUDGE TIME WORK_RATE':{  
      'question':'',
      'sql':''
   },
   'JUDGE WORK_RATE':{  
      'question':'',
      'sql':''
   },
   'GENDER JUDGE WORK_RATE':{  
      'question':'',
      'sql':''
   },
   'ETHNICITY JUDGE WORK_RATE':{  
      'question':'',
      'sql':''
   },
   'JUDGE POLITICAL_PARTY WORK_RATE':{  
      'question':'',
      'sql':''
   },
   'ABA JUDGE WORK_RATE':{  
      'question':'',
      'sql':''
   },
   'AVG CASE TIME':{  
      'question':'',
      'sql':''
   },
   'AVG CASE JUDGE TIME':{  
      'question':'',
      'sql':''
   },
   'AVG CASE JUDGE TIME TYPE':{  
      'question':'',
      'sql':''
   },
   'AVG CASE GENDER JUDGE TIME':{  
      'question':'',
      'sql':''
   },
   'AVG CASE ETHNICITY JUDGE TIME':{  
      'question':'',
      'sql':''
   },
   'AVG CASE JUDGE POLITICAL_PARTY TIME':{  
      'question':'',
      'sql':''
   },
   'ABA AVG CASE JUDGE TIME':{  
      'question':'',
      'sql':''
   },
   'AVG CASE DISTRICT TIME':{  
      'question':'',
      'sql':''
   }
}