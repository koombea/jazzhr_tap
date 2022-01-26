from jazzhr_tap import run_jazz_tap

route = "categories2applicants"
schema = {'properties': {
    'id': {'type': 'string'},
    'applicant_id': {'type': 'string'},
    'category_id': {'type': 'string'}
    },
    "primary_key": "id"
  }
stream = "jazzhr_categories2applicants"
def read_record(item):
  return {
    "id": item['id'], 
    'applicant_id': item["applicant_id"],
    'category_id': item["category_id"]
    }
run_jazz_tap(route, schema, stream, read_record)