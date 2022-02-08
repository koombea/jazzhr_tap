from jazzhr_tap import run_jazz_tap


def read_record(item):
  for i in range(1, 21):
    key = '0' + str(i) if i < 10 else str(i)
    item["answer_value_" + key] = item.get("answer_value_" + key, "")
    item["answer_correct_" + key] = item.get("answer_correct_" + key, "")
  return item


route = "questionnaire_answers"
key_properties = ["questionnaire_id", 'applicant_id', 'job_id']

run_jazz_tap(route, read_record, key_properties)
