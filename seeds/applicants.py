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

def retrieve_jazzhr_applicants_per_page(page):
  authenticated_endpoint = "{}applicants/page/{}?apikey={}".format(endpoint, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  if type(api_response)!=list: api_response=[api_response] 
  return list(map(lambda r: {"first_name": r["first_name"], "last_name": r["last_name"], "id": r["id"], "email": retrieve_applicant_email(r["id"])}, api_response))

def retrieve_applicant_email(id):
  authenticated_endpoint = "{}applicants/{}?apikey={}".format(endpoint, id, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["email"]

def retrieve_applicants():
  applicants = []
  pursue=True
  page=1
  while pursue:
    response = retrieve_jazzhr_applicants_per_page(page)
    applicants = applicants + response
    page = page +1
    if len(response)<100 : pursue=False
  return applicants

def post_jazzhr_applicant(applicant_data):
  authenticated_endpoint = "{}applicants".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json= applicant_data).json()
  return api_response

current_applicants=retrieve_applicants()
j=0
while j<10:
  applicant_data = {
  "first_name": fake.first_name(),
  "last_name": fake.last_name(),
  "email": fake.email(),
  "apikey": JAZZHR_KEY
  }
  invalid = any(
    (current_applicant['first_name']==applicant_data['first_name'] and current_applicant['last_name']==applicant_data['last_name'])
    or (current_applicant['email']==applicant_data['email'])
    for current_applicant in current_applicants)
  if invalid == False:
    response= post_jazzhr_applicant(applicant_data)
    print(response)
    current_applicants.append(applicant_data)
    j=j+1