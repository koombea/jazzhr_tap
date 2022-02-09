import random
import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv


def create_candidates(items_to_create, hire_candidate=False):
  dotenv_path = join(dirname(__file__), '../.env')
  load_dotenv(dotenv_path)
  JAZZHR_KEY = os.environ.get("jazzhr_key")
  endpoint = "https://api.resumatorapi.com/v1/"

  def retrieve_jazzhr_items_per_page(resource, page):
    authenticated_endpoint = f"{endpoint}{resource}/page/{page}?apikey={JAZZHR_KEY}"
    api_response = requests.get(authenticated_endpoint).json()
    if not isinstance(api_response, list):
      api_response = [api_response]
    return api_response

  def retrieve_all_items(resource):
    items = []
    pursue = True
    page = 1
    while pursue:
      response = retrieve_jazzhr_items_per_page(resource, page)
      items = items + response
      page = page + 1
      if len(response) < 100:
        pursue = False
    return items

  def post_jazzhr_applicants2jobs(applicants2job_data):
    authenticated_endpoint = f"{endpoint}applicants2jobs"
    api_response = requests.post(
      authenticated_endpoint, json=applicants2job_data).json()
    return api_response

  current_jobs = retrieve_all_items("jobs")
  current_applicants = retrieve_all_items("applicants")
  current_applicants2jobs = retrieve_all_items("applicants2jobs")
  i = 0
  while i < items_to_create:
    applicants2job_data = {
      "applicant_id": random.choice(current_applicants)["id"],
      "job_id": random.choice(current_jobs)["id"],
      "apikey": JAZZHR_KEY
    }
    invalid = any(current_a2j["applicant_id"] == applicants2job_data['applicant_id'] and current_a2j["job_id"]
                  == applicants2job_data['job_id'] for current_a2j in current_applicants2jobs)
    if not invalid:
      if hire_candidate:
        applicants2job_data["workflow_step_id"] = random.choice(
          ["8947217", "8947218"])
      response = post_jazzhr_applicants2jobs(applicants2job_data)
      # print(response)
      current_applicants2jobs.append(applicants2job_data)
      i = i + 1
