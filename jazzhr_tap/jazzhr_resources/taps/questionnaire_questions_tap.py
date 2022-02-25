import os, sys
sys.path.insert(0, os.getcwd()) 
from jazzhr_resources.http_request import call_api
from jazzhr_resources.load_jsons import load_schema
from  jazzhr_resources import write_records

def main():
  schema = load_schema("questionnaire_questions")
  endpoint = "https://api.resumatorapi.com/v1/"
  def retrieve_questionnaires_per_page(page):
    authenticated_endpoint = f"{endpoint}questionnaire_answers/page/{page}"
    api_response = call_api(authenticated_endpoint)
    if not isinstance(api_response, list):
      api_response = [api_response]
    return [r["questionnaire_id"] for r in api_response]

  def retrieve_all_questionnaires():
    items = []
    pursue = True
    page = 1
    while pursue:
      response = retrieve_questionnaires_per_page(page)
      items = items + response
      page = page + 1
      if len(response) < 100:
        pursue = False
    return list(set(items))
  def retrieve_questionnaire_questions(questionnaire_id):
    authenticated_endpoint = f"{endpoint}questionnaire_questions/questionnaire_id/{questionnaire_id}"
    api_response = call_api(authenticated_endpoint)
    if not isinstance(api_response, list):
      api_response = [api_response]
    return api_response

  list_questionnaires = retrieve_all_questionnaires()
  all_questions = []

  for q in list_questionnaires:
    all_questions = all_questions + retrieve_questionnaire_questions(q)

  stream = "jazzhr_questionnaire_questions"
  
  def read_record(item_):
    item_["question_mandatory"] = (item_["question_mandatory"] == 'Yes')
    item_["question_order"] = int(item_["question_order"])
    return item_
  
  write_records.main(stream, schema, ["questionnaire_id", "question_order"], read_record, all_questions)

if __name__ == "__main__":
  main()
