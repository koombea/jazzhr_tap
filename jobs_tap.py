import singer
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

JAZZHR_KEY = os.environ.get("jazzhr_key")
endpoint = "https://api.resumatorapi.com/v1/"
route = "jobs"

def retrieve_jazzhr_jobs():
  authenticated_endpoint = "{}{}?apikey={}".format(endpoint, route, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response

schema = {'properties': {
    'id': {'type': 'string'},
    'team_id': {'type': 'string'},
    'title': {'type': 'string'},
    'country_id': {'type': 'string'},
    'city': {'type': 'string'},
    'state': {'type': 'string'},
    'zip': {'type': 'string'},
    'department': {'type': 'string'},
    'description': {'type': 'string'},
    'minimum_salary': {'type': 'number'},
    'maximum_salary': {'type': 'number'},
    'notes': {'type': 'string'},
    'original_open_date': { "type": "string", "format": "date"},
    'type': {'type': 'string'},
    'status': {'type': 'string'},
    'send_to_job_boards': {'type': 'string'},
    'hiring_lead': {'type': 'string'},
    'board_code': {'type': 'string'},
    'internal_code': {'type': 'string'},
    'questionnaire': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="jazzhr_jobs", schema=schema, key_properties=[])

jobs = retrieve_jazzhr_jobs()
for job in jobs:
  singer.write_record(stream_name="jazzhr_jobs",  
  record={
    "id": job['id'], 
    'team_id': job["team_id"],
    'title': job["title"],
    'country_id': job["country_id"],
    'city': job["city"],
    'state': job["state"],
    'zip': job["zip"],
    'department': job["department"],
    'description': job["description"],
    'minimum_salary': job["minimum_salary"],
    'maximum_salary': job["maximum_salary"],
    'notes': job["notes"],
    'original_open_date': job["original_open_date"],
    'type': job["type"],
    'status': job["status"],
    'send_to_job_boards': job["send_to_job_boards"],
    'hiring_lead': job["hiring_lead"],
    'board_code': job["board_code"],
    'internal_code': job["internal_code"],
    'questionnaire': job["questionnaire"]
    })