import json
 
# Opening JSON file
json_schema = open('./schemas/applicants_details.json')
 
# returns JSON object as
# a dictionary
data = json.load(json_schema)
print(data)