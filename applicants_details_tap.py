import singer
import requests
import os
from os.path import join, dirname
import json
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')


json_schema = open('./schemas/applicants_details.json')
load_dotenv(dotenv_path)

JAZZHR_KEY = os.environ.get("jazzhr_key")
endpoint = "https://api.resumatorapi.com/v1/"
route = "applicants"
page = 1


def retrieve_jazzhr_applicants():
  authenticated_endpoint = "{}{}/page/{}?apikey={}".format(
    endpoint, route, page, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return list(map(lambda r: r["id"], api_response))


def retrieve_jazzhr_applicant_details(id):
  authenticated_endpoint = "{}applicants/{}?apikey={}".format(
    endpoint, id, JAZZHR_KEY)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response


schema = json.load(json_schema)
singer.write_schema(
  stream_name="jazzhr_applicants_details",
  schema=schema,
  key_properties=["id"])
applicants = []
pursue = True
while pursue:
  response = retrieve_jazzhr_applicants()
  applicants = applicants + response
  page = page + 1
  if len(response) < 100:
    pursue = False
lists = [
  "activities",
  "jobs",
  "feedback",
  "messages",
  "questionnaire",
  "evaluation",
  "categories",
  "comments"]
for applicant_ in applicants:
  applicant = retrieve_jazzhr_applicant_details(applicant_)
  for lst in lists:
    if not isinstance(applicant[lst], list):
      applicant[lst] = [applicant[lst]]
  for i in range(len(applicant["jobs"])):
    applicant["jobs"][i]["hiring_lead_rating"] = int(
      applicant["jobs"][i]["hiring_lead_rating"])
    applicant["jobs"][i]["average_rating"] = float(
      applicant["jobs"][i]["average_rating"])
  for i in range(len(applicant["evaluation"])):
    applicant["evaluation"][i]["rating"] = int(
      applicant["evaluation"][i]["rating"])
  singer.write_record(stream_name="jazzhr_applicants_details",
                      record=applicant)
