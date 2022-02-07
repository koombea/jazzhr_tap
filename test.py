# import json
# with open('./../schemas/applicants.json', encoding='utf-8') as json_schema:
#   schema = json.load(json_schema)
# print(schema)
api_response = [{"id": 12, "name": "oscar"}, {"id": 24, "name": "andres"}]
print([r["id"] for r in api_response])
