from jazzhr_tap import run_jazz_tap

route = "tasks"
schema = {'properties': {
    'id': {'type': 'string'},
    'object_id': {'type': 'string'},
    'owner_id': {'type': 'string'},
    'opener_name': {'type': 'string'},
    'assignee_id': {'type': 'string'},
    'assignee_name': {'type': 'string'},
    'status': {'type': 'string'},
    'description': {'type': 'string'},
    'notes': {'type': 'string'},
    'date_due': { "type": "string", "format": "date"},
    'due_whenever': {'type': 'boolean'},
    'date_created': { "type": "string", "format": "date"},
    'time_created': { "type": "string", "format": "time"}
    }
  }
stream = "jazzhr_tasks"
key_properties=["id"]
def read_record(item):
  item["due_whenever"] = True if item["due_whenever"]=='Yes' else False
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)
