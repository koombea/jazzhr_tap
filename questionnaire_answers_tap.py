from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/questionnaire_answers.json')
route = "questionnaire_answers"
schema = json.load(json_schema)
for i in range(1,21):
  key = '0'+str(i) if i<10 else str(i)  
  schema['properties']["answer_value_"+key] = {'type': ["string", "null"]}
  schema['properties']["answer_correct_"+key] = {'type': ["string", "null"]}
stream = "jazzhr_questionnaire_answers"
key_properties=["questionnaire_id", 'applicant_id', 'job_id']
def read_record(item):
  for i in range(1,21):
    key = '0'+str(i) if i<10 else str(i)  
    item["answer_value_"+key] = item.get("answer_value_"+key,"")
    item["answer_correct_"+key] = item.get("answer_correct_"+key,"")
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)