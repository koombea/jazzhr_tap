from faker import Faker
import numpy as np
import random
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

fake = Faker()

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"


def retrieve_records_per_page(resource, page, only_id):
  authenticated_endpoint = f"{endpoint}{resource}/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  # next line is necessary because when only one element the response is not
  # a list but the only object
  if not isinstance(api_response, list):
    api_response = [api_response]
  if only_id:
    return list(map(lambda r: r["id"], api_response))
  return api_response


def retrieve_all_records(resource, only_id=True):
  items = []
  pursue = True
  page = 1
  while pursue:
    response = retrieve_records_per_page(resource, page, only_id)
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  return items


def post_jazzhr_categories2applicants(category_data):
  authenticated_endpoint = f"{endpoint}categories2applicants"
  api_response = requests.post(
    authenticated_endpoint, json=category_data).json()
  return api_response


current_categories = retrieve_all_records("categories")
current_applicants = retrieve_all_records("applicants")
current_categories2applicants = retrieve_all_records(
  "categories2applicants", only_id=False)

new_records = []
i = 0
while i < 20:  # this number defines how many new items will be created
  c2a_data = {
    "applicant_id": random.choice(current_applicants),
    "category_id": random.choice(current_categories),
    "apikey": JAZZHR_KEY
  }
  # breakpoint()
  invalid = any(current_c2a['applicant_id'] == c2a_data['applicant_id'] and current_c2a['category_id']
                == c2a_data['category_id'] for current_c2a in current_categories2applicants)
  if not invalid:
    response = post_jazzhr_categories2applicants(c2a_data)
    print(response)
    current_categories2applicants.append(c2a_data)
    i = i + 1
