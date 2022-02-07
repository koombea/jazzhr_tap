import os
taps = [
  "activities",
  "applicants_details",
  "applicants",
  "applicants2jobs",
  "categories",
  "categories2applicants",
  "contacts",
  "files",
  "hires",
  "jobs",
  "questionnaire_answers",
  "questionnaire_questions",
  "tasks",
  "users"]
for tap in taps:
  os.system(f'python3 taps/{tap}_tap.py | target-stitch --config config.json')
