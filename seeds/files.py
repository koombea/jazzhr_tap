import random
import base64
import string
import os
from os.path import join, dirname
from faker import Faker
import requests
from dotenv import load_dotenv
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
fake = Faker()

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"


def retrieve_items_per_page(resource, page):
  authenticated_endpoint = f"{endpoint}{resource}/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  if not isinstance(api_response, list):
    api_response = [api_response]
  return api_response


def retrieve_all_items(resource):
  items = []
  pursue = True
  page = 1
  while pursue:
    response = retrieve_items_per_page(resource, page)
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  return items


def post_jazzhr_files(file_data_):
  authenticated_endpoint = f"{endpoint}files"
  api_response = requests.post(authenticated_endpoint, json=file_data_).json()
  return api_response


applicants = retrieve_all_items("applicants")

new_categories = []
i = 0
while i < 10:  # this number defines how many new items will be created
  applicant = random.choice(applicants)
  file_content = base64.b64encode(fake.text().encode()).decode()
  name = ''.join(random.choice(alphabet) for i in range(20))
  file_data = {
    "applicant_id": applicant["id"],
    "filename": name,
    "file_data": file_content,
    "file_privacy": random.choice([0, 30, 40]),
    "apikey": JAZZHR_KEY
  }
  post_jazzhr_files(file_data)
  i = i + 1
