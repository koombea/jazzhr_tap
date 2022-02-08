from jazzhr_details_tap import run_jazz_tap

route = "applicants"
key_properties = ["id"]


def read_record(item):
  lists = [
    "activities",
    "jobs",
    "feedback",
    "messages",
    "questionnaire",
    "evaluation",
    "categories",
    "comments"]
  for lst in lists:
    if not isinstance(item[lst], list):
      item[lst] = [item[lst]]
  for i in range(len(item["jobs"])):
    item["jobs"][i]["hiring_lead_rating"] = int(
      item["jobs"][i]["hiring_lead_rating"])
    item["jobs"][i]["average_rating"] = float(
      item["jobs"][i]["average_rating"])
  for i in range(len(item["evaluation"])):
    item["evaluation"][i]["rating"] = int(
      item["evaluation"][i]["rating"])
  return item


run_jazz_tap(route, read_record, key_properties)
