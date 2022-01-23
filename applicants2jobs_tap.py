from jazzhr_tap import run_jazz_tap

route = "applicants2jobs"
schema = {'properties': {
    'id': {'type': 'string'},
    'applicant_id': {'type': 'string'},
    'job_id': {'type': 'string'},
    'rating': {'type': 'integer'},
    'workflow_step_id': { "type": "integer"},
    'date': { "type": "string", "format": "date"}
    },
    "primary_key": "id"
  }
stream = "jazzhr_applicants2jobs"
def read_record(item):
  return {
    "id": item['id'], 
    'applicant_id': item["applicant_id"],
    'job_id': item["job_id"],
    'rating': int(item["rating"]),
    'workflow_step_id': int(item["workflow_step_id"]),
    'date': item["date"]
    }
run_jazz_tap(route, schema, stream, read_record)

# import singer
# import requests
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# JAZZHR_KEY = os.environ.get("jazzhr_key")
# endpoint = "https://api.resumatorapi.com/v1/"
# route = "applicants2jobs"
# page=1

# def retrieve_jazzhr_applicants2jobs():
#   authenticated_endpoint = "{}{}/page/{}?apikey={}".format(endpoint, route, page, JAZZHR_KEY)
#   api_response = requests.get(authenticated_endpoint).json()
#   return api_response

# schema = {'properties': {
#     'id': {'type': 'string'},
#     'applicant_id': {'type': 'string'},
#     'job_id': {'type': 'string'},
#     'rating': {'type': 'integer'},
#     'workflow_step_id': { "type": "integer"},
#     'date': { "type": "string", "format": "date"}
#     },
#     "primary_key": "id"
#   }
# singer.write_schema(stream_name="jazzhr_applicants2jobs", schema=schema, key_properties=[])

# applicants2jobs = []
# pursue=True
# while pursue:
#   response = retrieve_jazzhr_applicants2jobs()
#   applicants2jobs = applicants2jobs + response
#   page = page +1
#   if len(response)<100 : pursue=False
# for applicants2job in applicants2jobs:
#   singer.write_record(stream_name="jazzhr_applicants2jobs",  
#   record={
#     "id": applicants2job['id'], 
#     'applicant_id': applicants2job["applicant_id"],
#     'job_id': applicants2job["job_id"],
#     'rating': int(applicants2job["rating"]),
#     'workflow_step_id': int(applicants2job["workflow_step_id"]),
#     'date': applicants2job["date"]
#     })