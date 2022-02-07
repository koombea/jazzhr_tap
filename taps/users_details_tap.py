import os
from os.path import join, dirname
import json
import singer
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
schema_path = join(dirname(__file__), '../schemas/users_details.json')
with open(schema_path, encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
load_dotenv(dotenv_path)
stream="jazzhr_users_details"

JAZZHR_KEY = os.environ.get("jazzhr_key")
endpoint = "https://api.resumatorapi.com/v1/"
page = 1


def retrieve_jazzhr_users():
  authenticated_endpoint = f"{endpoint}users/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  return [r["id"] for r in api_response]


def retrieve_jazzhr_users_details(index):
  authenticated_endpoint = f"{endpoint}users/{index}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  return api_response


singer.write_schema(
  stream_name=stream,
  schema=schema,
  key_properties=["id"])
users = []
pursue = True
while pursue:
  response = retrieve_jazzhr_users()
  users = users + response
  page = page + 1
  if len(response) < 100:
    pursue = False
for user_ in users:
  applicant = retrieve_jazzhr_users_details(user_)
  if not isinstance(applicant["user_activity"], list):
    applicant["user_activity"] = [applicant["user_activity"]]
  singer.write_record(stream_name=stream,
                    record=applicant)
