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

def retrieve_jazzhr_categories_per_page(page):
  authenticated_endpoint = "{}categories/page/{}?apikey={}".format(endpoint, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  # next line is necessary because when only one element the response is not a list but the only object
  if type(api_response)!=list: api_response=[api_response] 
  return list(map(lambda r: r["name"], api_response))

def retrieve_all_categories():
  categories = []
  pursue=True
  page=1
  while pursue:
    response = retrieve_jazzhr_categories_per_page(page)
    categories = categories + response
    page = page +1
    if len(response)<100 : pursue=False
  return categories

def post_jazzhr_category(category_data):
  authenticated_endpoint = "{}categories".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json= category_data).json()
  return api_response

current_categories=retrieve_all_categories()

new_categories=[]
i=0
while i<5:
  category_data = {
  "name": fake.text(10),
  "status": np.random.randint(1, 3),
  "apikey": JAZZHR_KEY
  }
  invalid = any(current_category==category_data['name'] for current_category in current_categories)
  if invalid:
    i=i-1
  else:
    response= post_jazzhr_category(category_data)
    print(response)
  i=i+1