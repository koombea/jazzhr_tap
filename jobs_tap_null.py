import singer
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

JAZZHR_KEY = os.environ.get("jazzhr_key")
endpoint = "https://api.resumatorapi.com/v1/"
route = "applicants"

def retrieve_jazzhr_jobs(id):
  authenticated_endpoint = "{}{}?apikey={}".format(endpoint, route, id)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["abilities"]

schema = {'properties': {
    'title': {'type': 'string'},
    'hiring_lead_id': {'type': 'string'},
    'employment_type': {'type': 'string'},
    'country_id': {'type': 'string'},
    'city': {'type': 'string'},
    'state': {'type': 'string'},
    'zip': {'type': 'string'},
    'department': {'type': 'string'},
    'description': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="jazzhr_jobs", schema=schema, key_properties=[])

jobs = retrieve_jazzhr_jobs(j)
for job in jobs:
  singer.write_record(stream_name="jazzhr_jobs",  
  record={
    'title': job["title"],
    'hiring_lead_id': job["hiring_lead_id"],
    'employment_type': job["employment_type"],
    'minimum_experience': job["minimum_experience"],
    'description': job["description"],
    'country': job["country"],
    'job_status': job["job_status"],
    'workflow_id': job["workflow_id"],
    'apikey': job["apikey"]
    })