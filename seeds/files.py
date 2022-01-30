from faker import Faker
import random
import base64
import string
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
alphabet = list(string.ascii_lowercase)+list(string.ascii_uppercase)
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

def post_jazzhr_files(category_data):
  authenticated_endpoint = "{}files".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json= category_data).json()
  return api_response

applicants = retrieve_all_items("applicants")

new_categories=[]
i=0
while i<10: # this number defines how many new items will be created
  applicant = random.choice(applicants)
  file_content = base64.b64encode(fake.text().encode()).decode()
  name = ''.join(random.choice(alphabet) for i in range(20))
  file_data = {
    "applicant_id": applicant["id"],
    "filename": name,
    "file_data":file_content,
    "file_privacy": random.choice([0, 30, 40]),
    "apikey": JAZZHR_KEY
    }
  response= post_jazzhr_files(file_data)
  print(file_data)
  print(response)
  i=i+1