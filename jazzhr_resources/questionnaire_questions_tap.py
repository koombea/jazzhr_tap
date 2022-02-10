import json
from os.path import join, dirname
import singer
import requests


def main():
  keys_path = join(dirname(__file__), 'schemas/keys.json')
  with open(keys_path, encoding='utf-8') as json_keys:
    JAZZHR_KEY = json.load(json_keys)["jazzhr_key"]
  schema_path = join(
    dirname(__file__),
    'schemas/questionnaire_questions.json')
  with open(schema_path, encoding='utf-8') as json_schema:
    schema = json.load(json_schema)

  endpoint = "https://api.resumatorapi.com/v1/"

  def retrieve_questionnaires_per_page(page):
    authenticated_endpoint = f"{endpoint}questionnaire_answers/page/{page}?apikey={JAZZHR_KEY}"
    api_response = requests.get(authenticated_endpoint).json()
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
    authenticated_endpoint = f"{endpoint}questionnaire_questions/questionnaire_id/{questionnaire_id}?apikey={JAZZHR_KEY}"
    api_response = requests.get(authenticated_endpoint).json()
    if not isinstance(api_response, list):
      api_response = [api_response]
    return api_response

  list_questionnaires = retrieve_all_questionnaires()
  all_questions = []

  for q in list_questionnaires:
    all_questions = all_questions + retrieve_questionnaire_questions(q)

  stream = "jazzhr_questionnaire_questions"
  singer.write_schema(stream_name=stream, schema=schema, key_properties=[
                      "questionnaire_id", "question_order"])

  for question in all_questions:
    question["question_mandatory"] = (question["question_mandatory"] == 'Yes')
    question["question_order"] = int(question["question_order"])
    singer.write_record(stream_name=stream,
                        record=question)


if __name__ == "__main__":
  main()
