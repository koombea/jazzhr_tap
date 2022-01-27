from faker import Faker
import random
import numpy as np
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

fake = Faker()

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"

def retrieve_items_per_page(resource, page):
  authenticated_endpoint = "{}{}/page/{}?apikey={}".format(endpoint, resource, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  # next line is necessary because when only one element the response is not a list but the only object
  if type(api_response)!=list: api_response=[api_response] 
  return api_response

def retrieve_all_items(resource):
  items = []
  pursue=True
  page=1
  while pursue:
    response = retrieve_items_per_page(resource, page)
    items = items + response
    page = page +1
    if len(response)<100 : pursue=False
  return items

def post_jazzhr_questionnaire_answers(category_data):
  authenticated_endpoint = "{}questionnaire_answers".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json= category_data).json()
  return api_response

current_a2j_list=retrieve_all_items("applicants2jobs")
current_qa_list=retrieve_all_items("questionnaire_answers")

new_categories=[]
i=0
while i<20: # this number defines how many new items will be created
  a2j = random.choice(current_a2j_list)
  invalid = any(current_qa["applicant_id"]==a2j['applicant_id'] and current_qa["job_id"]==a2j['job_id'] for current_qa in current_qa_list)
  if invalid==False:
    qa_data = {
    "applicant_id": a2j["applicant_id"],
    "questionnaire_id": random.choice(["questionnaire_20220126195522_QD6FSWHN56OSJEXK","questionnaire_20220127003308_JDFZN564QK5XEHVQ"]),
    "job_id": a2j["job_id"],
    "answer_value_01": fake.text(),
    "answer_value_02": fake.text(),
    "answer_value_03": random.choice(["a","b","c","d"]),
    "answer_value_04": np.random.randint(0, 100),
    "apikey": JAZZHR_KEY
    }
    response= post_jazzhr_questionnaire_answers(qa_data)
    print(response)
    current_qa_list.append(qa_data)
    i=i+1