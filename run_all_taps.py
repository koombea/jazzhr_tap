import os
os.system('python3 activities_tap.py | target-stitch --config config.json')
os.system('python3 applicants_details_tap.py | target-stitch --config config.json')
os.system('python3 applicants_tap.py | target-stitch --config config.json')
os.system('python3 applicants2jobs_tap.py | target-stitch --config config.json')
os.system('python3 categories_tap.py | target-stitch --config config.json')
os.system('python3 categories2applicants_tap.py | target-stitch --config config.json')
os.system('python3 contacts_tap.py | target-stitch --config config.json')
os.system('python3 files_tap.py | target-stitch --config config.json')
os.system('python3 hires_tap.py | target-stitch --config config.json')
os.system('python3 jobs_tap.py | target-stitch --config config.json')
os.system('python3 questionnaire_answers_tap.py | target-stitch --config config.json')
os.system('python3 questionnaire_questions_tap.py | target-stitch --config config.json')
os.system('python3 tasks_tap.py | target-stitch --config config.json')
os.system('python3 users_tap.py | target-stitch --config config.json')