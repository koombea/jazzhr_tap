from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
  # os.system(f'python3 jazzhr_tap/jazzhr_resources | target-stitch --config jazzhr_tap/jazzhr_resources/config.json')
  subprocess.Popen(
    'cd jazzhr_tap && python -m jazzhr_resources | target-stitch --config jazzhr_resources/config.json',
    stdin=subprocess.PIPE,
    shell=True
  )
  return "done"

app.run(port=8080)

# import os
# taps = [
#   "activities",
#   "applicants_details",
#   "applicants",
#   "applicants2jobs",
#   "categories",
#   "categories2applicants",
#   "contacts",
#   "files",
#   "hires",
#   "jobs_details",
#   "jobs",
#   "questionnaire_answers",
#   "questionnaire_questions",
#   "tasks",
#   "users_details",
#   "users"
# ]
# for tap in taps:
#   os.system(
#     f'python3 {tap}_tap.py | target-stitch --config config.json')