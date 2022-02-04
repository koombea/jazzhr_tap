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
  authenticated_endpoint = "{}jobs/page/{}?apikey={}".format(
    endpoint, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return list(map(lambda r: r["title"], api_response))


def retrieve_jazzhr_applicants_per_page(page):
  authenticated_endpoint = "{}applicants/page/{}?apikey={}".format(
    endpoint, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()

  return list(map(lambda r: {"first_name": r["first_name"], "last_name": r["last_name"], "id": r["id"], "email": retrieve_applicant_email(r["id"])}, api_response))


def retrieve_applicant_email(id):
  authenticated_endpoint = "{}applicants/{}?apikey={}".format(
    endpoint, id, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["email"]


def retrieve_jobs():
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


def post_jazzhr_job(job_data):
  authenticated_endpoint = "{}jobs".format(endpoint)
  api_response = requests.post(authenticated_endpoint, json=job_data).json()
  return api_response


def post_jazzhr_applicant(applicant_data):
  authenticated_endpoint = "{}applicants".format(endpoint)
  api_response = requests.post(
    authenticated_endpoint, json=applicant_data).json()
  return api_response


def post_jazzhr_applicants2job(applicant_id, job_id):
  applicants2job_data = {
    "applicant_id": applicant_id,
    "job_id": job_id,
    "apikey": JAZZHR_KEY
  }
  authenticated_endpoint = "{}applicants2jobs".format(endpoint)
  api_response = requests.post(
    authenticated_endpoint, json=applicants2job_data).json()
  return api_response['appjob_id']


current_jobs = retrieve_jobs()
current_applicants = retrieve_applicants()

jobs = []
applicants = []
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
  if invalid:
    i = i-1
  else:
    response = post_jazzhr_job(job_data)
    print(response)
    jobs.append(response['job_id'])
  i = i+1
j = 0
while j < 75:
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
  if invalid:
    j = j-1
  else:
    response = post_jazzhr_applicant(applicant_data)
    print(response)
    applicants.append(response['prospect_id'])
  j = j+1

for applicant in applicants:
  some_jobs = random.sample(jobs, np.random.randint(0, 4))
  for some_job in some_jobs:
    response = post_jazzhr_applicants2job(applicant, some_job)
    print(response)
