from jazzhr_tap import run_jazz_tap

route = "activities"
schema = {'properties': {
    'id': {'type': 'string'},
    'category': {'type': 'string'},
    'team_id': {'type': 'string'},
    'user_id': {'type': 'string'},
    'object_id': {'type': 'string'},
    'action': {'type': 'string'},
    'date': { "type": "string", "format": "date"},
    'time': { "type": "string", "format": "time"}
    },
    "primary_key": "id"
  }
stream = "jazzhr_activities"
def read_record(item):
  return {
    "id": item['id'], 
    'category': item["category"],
    'team_id': item["team_id"],
    'user_id': item["user_id"],
    'object_id': item["object_id"],
    'action': item["action"],
    'date': item["date"],
    'time': item["time"]
    }
run_jazz_tap(route, schema, stream, read_record)