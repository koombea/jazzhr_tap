from faker import Faker
import numpy as np
import random
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

fake = Faker()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")

endpoint = "https://api.resumatorapi.com/v1/"


job_data = {
  "title": fake.job(),
  "hiring_lead_id": "usr_20220118201302_8FFMX3NBYFHWMEQ2",
  "employment_type": np.random.randint(1, 10),
  "minimum_experience": np.random.randint(1, 10),
  "description": fake.text(),
  "country": np.random.randint(110, 142),
  "job_status": np.random.randint(1, 7),
  "workflow_id": random.choice(["577352", "577477"]),
  "apikey": JAZZHR_KEY
}

applicant_data = {
  "first_name": fake.first_name(),
  "last_name": fake.last_name(),
  "email": fake.email(),
  "apikey": JAZZHR_KEY
}

def post_jazzhr_job():
  authenticated_endpoint = "{}jobs".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json= job_data).json()
  return api_response

def post_jazzhr_applicant():
  authenticated_endpoint = "{}applicants".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json= applicant_data).json()
  return api_response
# print(post_jazzhr_job())

print(post_jazzhr_applicant())