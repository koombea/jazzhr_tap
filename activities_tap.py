from jazzhr_tap import run_jazz_tap

route = "activities"
schema = {"type": "object",
  'properties': {
    'id': {'type': 'string'},
    'category': {'type': 'string'},
    'team_id': {'type': 'string'},
    'user_id': {'type': 'string'},
    'object_id': {'type': 'string'},
    'action': {'type': 'string'},
    'date': { "type": "string", "format": "date"},
    'time': { "type": "string", "format": "time"}
    }
  }
stream = "jazzhr_activities"
key_properties=["id"]
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)