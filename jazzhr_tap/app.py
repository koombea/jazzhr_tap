from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
  subprocess.Popen(
    'python3 -m jazzhr_resources | target-stitch --config ./jazzhr_resources/config.json',
    stdin=subprocess.PIPE,
    shell=True
  )
  return "done"

port = os.environ.get("PORT", 8080)
app.run(debug=False, port=port, host='0.0.0.0')