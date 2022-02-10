import os
from os.path import join, dirname
from faker import Faker
import requests
from dotenv import load_dotenv

fake = Faker()

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"


def retrieve_jazzhr_applicants_per_page(page):
  authenticated_endpoint = f"{endpoint}applicants/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  if not isinstance(api_response, list):
    api_response = [api_response]
  return [{
    "first_name": r["first_name"],
    "last_name": r["last_name"],
    "id": r["id"],
    "email": retrieve_applicant_email(
          r["id"])} for r in api_response]


def retrieve_applicant_email(id_):
  authenticated_endpoint = f"{endpoint}applicants/{id_}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["email"]


def retrieve_applicants():
  applicants = []
  pursue = True
  page = 1
  while pursue:
    response = retrieve_jazzhr_applicants_per_page(page)
    applicants = applicants + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  return applicants


def post_jazzhr_applicant(applicant_data_):
  authenticated_endpoint = f"{endpoint}applicants"
  api_response = requests.post(
    authenticated_endpoint, json=applicant_data_).json()
  return api_response


current_applicants = retrieve_applicants()
j = 0
while j < 10:
  applicant_data = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "email": fake.email(),
    "apikey": JAZZHR_KEY
  }
  invalid = any(
    (current_applicant['first_name'] == applicant_data['first_name']
     and current_applicant['last_name'] == applicant_data['last_name'])
    or (current_applicant['email'] == applicant_data['email'])
    for current_applicant in current_applicants)
  if not invalid:
    post_jazzhr_applicant(applicant_data)
    current_applicants.append(applicant_data)
    j = j + 1
