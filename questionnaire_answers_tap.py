from jazzhr_tap import run_jazz_tap

route = "questionnaire_answers"
schema = {'properties': {
    'job_id': {'type': ["string", "null"]},
    'applicant_id': {'type': 'string'},
    'questionnaire_id': {'type': 'string'},
    'questionnaire_code': {'type': 'string'},
    'date_taken': { "type": "string", "format": "date"},
    'time_taken': { "type": "string", "format": "time"}
    },
    "primary_key": "questionnaire_code"
  }
for i in range(1,21):
  key = '0'+str(i) if i<10 else str(i)  
  schema['properties']["answer_value_"+key] = {'type': ["string", "null"]}
  schema['properties']["answer_correct_"+key] = {'type': ["string", "null"]}
stream = "jazzhr_questionnaire_answers"
def read_record(item):
  for i in range(1,21):
    key = '0'+str(i) if i<10 else str(i)  
    item["answer_value_"+key] = item.get("answer_value_"+key,"")
    item["answer_correct_"+key] = item.get("answer_correct_"+key,"")
  return item
run_jazz_tap(route, schema, stream, read_record)