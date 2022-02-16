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
  return [
    f"jazzhr_{tap}_tap = jazzhr_resources.{tap}_tap:main" for tap in taps]


setup(
  name='jazzhr-tap',
  version='0.0.1',
  description="Singer tap to extract and load all data from tap jazzhr-api endpoints",
  author='Oscar Andrés Russi Porras',
  url='https://singer.io',
  classifiers=['Programming Language :: Python :: 3 :: Only'],
  py_modules=['jazzhr_resources'],
  package_data={
    "schemas": ["jazzhr_resources/schemas/*.json"]},
  install_requires=[
    'requests>=2.20.0',
    'singer-python',
    'numpy>=1.21.4',
    'python-dotenv>=0.19.2',
    'setuptools>=44.0.0'],
  entry_points={
    'console_scripts': ['jazzhr_tap = jazzhr_resources:main'] + resources_taps()},
  packages=["jazzhr_resources"],
  include_package_data=True)
