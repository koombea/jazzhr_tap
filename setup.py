from setuptools import setup

def resources_taps():
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
  "jobs_details",
  "jobs",
  "questionnaire_answers",
  "questionnaire_questions",
  "tasks",
  "users_details",
  "users"
  ]
  return [f"jazzhr_{tap}_tap = jazzhr_resources.{tap}_tap:main" for tap in taps]

setup(name='jazzhr-tap',
      version='0.0.1',
      description="Singer tap to extract and load all data from tap jazzhr-api endpoints",
      author='Oscar Andrés Russi Porras',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['jazzhr_resources'],
      package_data={
        "schemas": ["jazzhr_resources/schemas/*.json"]
    },
      install_requires=[
          'requests>=2.20.0',
          'singer-python>=5.12.2',
          'numpy>=1.21.4',
          'python-dotenv>=0.19.2',
          'setuptools>=44.0.0'
      ],
      entry_points={
        'console_scripts': ['jazzhr_tap = jazzhr_resources:main']+resources_taps()
        },
    #   entry_points='''
    #       [console_scripts]
    #       jazzhr_tap = jazzhr_resources:main
    #   ''',
       packages=["jazzhr_resources"],
      include_package_data=True,
      # ,
      # entry_points={
      #   'console_scripts': [
      #     'jazzhr_activities_tap = load_resources:activities',
      #     'jazzhr_applicants_details_tap = load_resources:applicants_details',
      #     'jazzhr_applicants_tap = load_resources:applicants',
      #     'jazzhr_applicants2jobs_tap = load_resources:applicants2jobs',
      #     'jazzhr_categories_tap = load_resources:categories',
      #     'jazzhr_categories2applicants_tap = load_resources:categories2applicants',
      #     'jazzhr_contacts_tap = load_resources:contacts',
      #     'jazzhr_files_tap = load_resources:files',
      #     'jazzhr_hires_tap = load_resources:hires',
      #     'jazzhr_jobs_details_tap = load_resources:jobs_details',
      #     'jazzhr_jobs_tap = load_resources:jobs',
      #     'jazzhr_questionnaire_answers_tap = load_resources:questionnaire_answers',
      #     'jazzhr_questionnaire_questions_tap = load_resources:questionnaire_questions',
      #     'jazzhr_tasks_tap = load_resources:tasks',
      #     'jazzhr_users_details_tap = load_resources:users_details',
      #     'jazzhr_users_tap = load_resources:users',
      #     'jazzhr_all_resources_tap = load_resources:all_resources'
      #   ],
      # }
      )


# from setuptools import setup
# setup(name='tap-jazzhr-api',
#       version='0.0.1',
#       description="Singer tap to extract and load all data from tap jazz-api endpoints",
#       author='Oscar Andrés Russi Porras',
#       url='https://singer.io',
#       classifiers=['Programming Language :: Python :: 3 :: Only'],
#       py_modules=['load_resources'],
#       package_data={
#         "schemas": ["schemas/*.json"],
#         "env": [".env"]
#     },
#       install_requires=[
#           'requests>=2.20.0',
#           'singer-python>=5.12.2',
#           'Faker>=11.3.0',
#           'numpy>=1.21.4',
#           'python-dotenv>=0.19.2',
#           'setuptools>=44.0.0'
#       ],
#       entry_points='''
#           [console_scripts]
#           jazzhr_tap = load_resources:main
#       '''
#       # ,
#       # entry_points={
#       #   'console_scripts': [
#       #     'jazzhr_activities_tap = load_resources:activities',
#       #     'jazzhr_applicants_details_tap = load_resources:applicants_details',
#       #     'jazzhr_applicants_tap = load_resources:applicants',
#       #     'jazzhr_applicants2jobs_tap = load_resources:applicants2jobs',
#       #     'jazzhr_categories_tap = load_resources:categories',
#       #     'jazzhr_categories2applicants_tap = load_resources:categories2applicants',
#       #     'jazzhr_contacts_tap = load_resources:contacts',
#       #     'jazzhr_files_tap = load_resources:files',
#       #     'jazzhr_hires_tap = load_resources:hires',
#       #     'jazzhr_jobs_details_tap = load_resources:jobs_details',
#       #     'jazzhr_jobs_tap = load_resources:jobs',
#       #     'jazzhr_questionnaire_answers_tap = load_resources:questionnaire_answers',
#       #     'jazzhr_questionnaire_questions_tap = load_resources:questionnaire_questions',
#       #     'jazzhr_tasks_tap = load_resources:tasks',
#       #     'jazzhr_users_details_tap = load_resources:users_details',
#       #     'jazzhr_users_tap = load_resources:users',
#       #     'jazzhr_all_resources_tap = load_resources:all_resources'
#       #   ],
#       # }
#       )
