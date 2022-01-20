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

def retrieve_jazzhr_applicants():
  authenticated_endpoint = "{}{}?apikey={}".format(endpoint, route, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response

schema = {'properties': {
    'id': {'type': 'string'},
    'first_name': {'type': 'string'},
    'last_name': {'type': 'string'},
    'prospect_phone': {'type': 'string'},
    'apply_date': { "type": "string", "format": "date"},
    'job_id': {'type': 'string'},
    'job_title': {'type': 'string'}
    },
    "primary_key": "id"
  }
singer.write_schema(stream_name="jazzhr_applicants", schema=schema, key_properties=[])

applicants = retrieve_jazzhr_applicants()
for applicant in applicants:
  singer.write_record(stream_name="jazzhr_applicants",  
  record={
    "id": applicant['id'], 
    'first_name': applicant["first_name"],
    'last_name': applicant["last_name"],
    'prospect_phone': applicant["prospect_phone"],
    'apply_date': applicant["apply_date"],
    'job_id': applicant["job_id"],
    'job_title': applicant["job_title"]
    })