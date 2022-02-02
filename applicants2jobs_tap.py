from jazzhr_tap import run_jazz_tap

route = "applicants2jobs"
schema = {'properties': {
    'id': {'type': 'string'},
    'applicant_id': {'type': 'string'},
    'job_id': {'type': 'string'},
    'rating': {'type': 'integer'},
    'workflow_step_id': { "type": "string"},
    'date': { "type": "string", "format": "date"}
    }
  }
stream = "jazzhr_applicants2jobs"
def read_record(item):
  item["rating"] = int(item["rating"])
  return item
key_properties=["id"]
run_jazz_tap(route, schema, stream, read_record, key_properties)