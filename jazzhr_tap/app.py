from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
  subprocess.Popen(
    'python3 -m jazzhr_resources | target-stitch --config ./jazzhr_resources/config.json',
    stdin=subprocess.PIPE,
    shell=True
  )
  return "done"

app.run(port=8080, host='0.0.0.0')