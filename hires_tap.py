from jazzhr_tap import run_jazz_tap

route = "hires"
schema = {'properties': {
    'id': {'type': 'string'},
    'applicant_id': {'type': 'string'},
    'job_id': {'type': 'string'},
    'workflow_step_id': {'type': 'string'},
    'workflow_step_name': {'type': 'string'},
    'hired_date': { "type": "string", "format": "date"},
    'hired_time': { "type": "string", "format": "time"}
    },
    "primary_key": "id"
  }
stream = "jazzhr_hires"
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record)