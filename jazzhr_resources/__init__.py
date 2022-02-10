from jazzhr_resources import activities_tap, applicants_details_tap, applicants_tap, applicants2jobs_tap, categories_tap, categories2applicants_tap, contacts_tap, files_tap, hires_tap, jobs_details_tap, jobs_tap, questionnaire_answers_tap, questionnaire_questions_tap, tasks_tap, users_details_tap, users_tap


def main():
  activities_tap.main()
  applicants_details_tap.main()
  applicants_tap.main()
  applicants2jobs_tap.main()
  categories_tap.main()
  categories2applicants_tap.main()
  contacts_tap.main()
  files_tap.main()
  hires_tap.main()
  jobs_details_tap.main()
  jobs_tap.main()
  questionnaire_answers_tap.main()
  questionnaire_questions_tap.main()
  tasks_tap.main()
  users_details_tap.main()
  users_tap.main()


if __name__ == "__main__":
  main()
