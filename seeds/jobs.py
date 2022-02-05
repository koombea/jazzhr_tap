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


def retrieve_jazzhr_jobs_per_page(page):
  authenticated_endpoint = f"{endpoint}jobs/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  if not isinstance(api_response, list):
    api_response = [api_response]
  return list(map(lambda r: r["title"], api_response))


def retrieve_all_jobs():
  jobs = []
  pursue = True
  page = 1
  while pursue:
    response = retrieve_jazzhr_jobs_per_page(page)
    jobs = jobs + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  return jobs


def post_jazzhr_job(job_data):
  authenticated_endpoint = f"{endpoint}jobs"
  api_response = requests.post(authenticated_endpoint, json=job_data).json()
  return api_response


current_jobs = retrieve_all_jobs()

i = 0
while i < 5:
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
  invalid = any(current_job == job_data['title']
                for current_job in current_jobs)
  if not invalid:
    response = post_jazzhr_job(job_data)
    print(response)
    current_jobs.append(job_data['title'])
    i = i + 1
