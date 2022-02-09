import os
from os.path import join, dirname
from faker import Faker
import numpy as np
import requests
from dotenv import load_dotenv

fake = Faker()

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"


def retrieve_jazzhr_categories_per_page(page):
  authenticated_endpoint = f"{endpoint}categories/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  # next line is necessary because when only one element the response is not
  # a list but the only object
  if not isinstance(api_response, list):
    api_response = [api_response]
  return [r["name"] for r in api_response]


def retrieve_all_categories():
  categories = []
  pursue = True
  page = 1
  while pursue:
    response = retrieve_jazzhr_categories_per_page(page)
    categories = categories + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  return categories


def post_jazzhr_category(category_data_):
  authenticated_endpoint = f"{endpoint}categories"
  api_response = requests.post(
    authenticated_endpoint, json=category_data_).json()
  return api_response


current_categories = retrieve_all_categories()

new_categories = []
i = 0
while i < 20:  # this number defines how many new items will be created
  category_data = {
    "name": fake.text(10),
    "status": np.random.randint(1, 3),
    "apikey": JAZZHR_KEY
  }
  invalid = any(current_category ==
                category_data['name'] for current_category in current_categories)
  if not invalid:
    response_ = post_jazzhr_category(category_data)
    # print(response_)
    i = i + 1
