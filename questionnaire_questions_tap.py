import singer
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"

def retrieve_questionnaires_per_page(page):
  authenticated_endpoint = "{}questionnaire_answers/page/{}?apikey={}".format(endpoint, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  # next line is necessary because when only one element the response is not a list but the only object
  if type(api_response)!=list: api_response=[api_response] 
  return list(map(lambda d: d["questionnaire_id"], api_response))

def retrieve_all_questionnaires():
  items = []
  pursue=True
  page=1
  while pursue:
    response = retrieve_questionnaires_per_page(page)
    items = items + response
    page = page +1
    if len(response)<100 : pursue=False
  return list(set(items))

def retrieve_questionnaire_questions(questionnaire_id):
  authenticated_endpoint = "{}questionnaire_questions/questionnaire_id/{}?apikey={}".format(endpoint, questionnaire_id, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  if type(api_response)!=list: api_response=[api_response] 
  return api_response

list_questionnaires=retrieve_all_questionnaires()
all_questions=[]

for q in list_questionnaires:
  all_questions = all_questions + retrieve_questionnaire_questions(q)

stream = "jazzhr_questionnaire_questions"
schema = {'properties': {
    'questionnaire_id': {'type': 'string'},
    'questionnaire_code': {'type': 'string'},
    'question_text': {'type': 'string'},
    'question_answers': {'type': 'string'},
    'question_format': {'type': 'string'},
    'question_order': {'type': 'integer'},
    'question_mandatory': {'type': 'boolean'},
    'question_correct_answer': {'type': 'string'},
    'question_status': {'type': 'string'}
    }
  }

singer.write_schema(stream_name=stream, schema=schema, key_properties=["questionnaire_id", "question_order"])

for question in all_questions:
  question["question_mandatory"]= True if question["question_mandatory"]=='Yes' else False
  question["question_order"]=int(question["question_order"])
  singer.write_record(stream_name=stream,  
  record= question)