from jazzhr_tap import run_jazz_tap

route = "applicants2jobs"
schema = {'properties': {
    'id': {'type': 'string'},
    'applicant_id': {'type': 'string'},
    'job_id': {'type': 'string'},
    'rating': {'type': 'integer'},
    'workflow_step_id': { "type": "integer"},
    'date': { "type": "string", "format": "date"}
    },
    "primary_key": "id"
  }
stream = "jazzhr_applicants2jobs"
def read_record(item):
  return {
    "id": item['id'], 
    'applicant_id': item["applicant_id"],
    'job_id': item["job_id"],
    'rating': int(item["rating"]),
    'workflow_step_id': int(item["workflow_step_id"]),
    'date': item["date"]
    }
run_jazz_tap(route, schema, stream, read_record)