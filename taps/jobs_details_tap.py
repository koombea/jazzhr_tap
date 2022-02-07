import os
from os.path import join, dirname
import json
import singer
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
schema_path = join(dirname(__file__), '../schemas/jobs_details.json')
with open(schema_path, encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
load_dotenv(dotenv_path)
stream="jazzhr_jobs_details"

JAZZHR_KEY = os.environ.get("jazzhr_key")
endpoint = "https://api.resumatorapi.com/v1/"
page = 1


def retrieve_jazzhr_jobs():
  authenticated_endpoint = f"{endpoint}jobs/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  return [r["id"] for r in api_response]


def retrieve_jazzhr_jobs_details(index):
  authenticated_endpoint = f"{endpoint}jobs/{index}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  return api_response


singer.write_schema(
  stream_name=stream,
  schema=schema,
  key_properties=["id"])
jobs = []
pursue = True
while pursue:
  response = retrieve_jazzhr_jobs()
  jobs = jobs + response
  page = page + 1
  if len(response) < 100:
    pursue = False
for job_ in jobs:
  job_details = retrieve_jazzhr_jobs_details(job_)
  if not isinstance(job_details["job_applicants"], list):
    job_details["job_applicants"] = [job_details["job_applicants"]]
  job_details["minimum_salary"] = float(job_details["minimum_salary"])
  job_details["maximum_salary"] = float(job_details["maximum_salary"])
  singer.write_record(stream_name=stream,
                    record=job_details)