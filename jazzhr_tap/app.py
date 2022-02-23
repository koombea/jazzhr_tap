import subprocess
import os
from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def home():
  keys = {
    "jazzhr_key": os.environ.get('jazzhr_key')
  }

  stitch_config_json = {
    "client_id" : os.environ.get('client_id'),
    "token" : os.environ.get('token'),
    "small_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "big_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "batch_size_preferences": {}
  }
  
  with open('./jazzhr_resources/schemas/keys.json', 'w') as outfile:
    json.dump(keys, outfile)

  with open('./jazzhr_resources/config.json', 'w') as outfile:
    json.dump(stitch_config_json, outfile)
  subprocess.Popen(
    'python3 -m jazzhr_resources | target-stitch --config ./jazzhr_resources/config.json',
    stdin=subprocess.PIPE,
    shell=True)
  return "done"


port = os.environ.get("PORT", 8080)
app.run(debug=True, port=port, host='0.0.0.0')
