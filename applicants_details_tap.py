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
page=1

def retrieve_jazzhr_applicants():
  authenticated_endpoint = "{}{}/page/{}?apikey={}".format(endpoint, route, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return list(map(lambda r: r["id"], api_response))

def retrieve_jazzhr_applicant_details(id):
  authenticated_endpoint = "{}applicants/{}?apikey={}".format(endpoint, id, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response

schema = {'properties': {
    'id': {'type': 'string'},
    'first_name': {'type': 'string'},
    'last_name': {'type': 'string'},
    'email': {'type': 'string'},
    'address': {'type': 'string'},
    'location': {'type': 'string'},
    'linkedin_url': {'type': 'string'},
    'eeo_gender': {'type': ["string", "null"]},
    'eeo_race': {'type': ["string", "null"]},
    'eeo_disability': {'type': ["string", "null"]},
    'website': {'type': 'string'},
    'desired_salary': {'type': 'string'},
    'desired_start_date': { "type": "string", "format": "date"},
    'referrer': {'type': 'string'},
    'languages': {'type': 'string'},
    'wmyu': {'type': 'string'},
    'has_driver_license': {'type': 'string'},
    'willing_to_relocate': {'type': 'string'},
    'citizenship_status': {'type': 'string'},
    'education_level': {'type': 'string'},
    'has_cdl': {'type': 'string'},
    'over_18': {'type': 'string'},
    'can_work_weekends': {'type': 'string'},
    'can_work_evenings': {'type': 'string'},
    'can_work_overtime': {'type': 'string'},
    'has_felony': {'type': 'string'},
    'felony_explanation': {'type': 'string'},
    'twitter_username': {'type': 'string'},
    'college_gpa': {'type': 'string'},
    'college': {'type': 'string'},
    'references': {'type': 'string'},
    'notes': {'type': 'string'},
    'comments_count': {'type': 'string'},
    'source': {'type': 'string'},
    'recruiter_id': {'type': 'string'},
    'eeoc_veteran': {'type': ["string", "null"]},
    'eeoc_disability': {'type': ["string", "null"]},
    'eeoc_disability_signature': {'type': ["string", "null"]},
    'eeoc_disability_date':  { "type": ["string", "null"], "format": "date"},
    'apply_date': { "type": "string", "format": "date"},
    "resume_body": {'type': 'string'}
    },
    "primary_key": "id"
  }
singer.write_schema(stream_name="jazzhr_applicants_details", schema=schema, key_properties=[])
applicants = []
pursue=True
while pursue:
    response = retrieve_jazzhr_applicants()
    applicants = applicants + response
    page = page +1
    if len(response)<100 : pursue=False
for applicant_ in applicants:
  applicant = retrieve_jazzhr_applicant_details(applicant_)
  singer.write_record(stream_name="jazzhr_applicants_details",  
  record=applicant)