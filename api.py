import os
from api import app
from api.util import load_config


# The path is relative to the top of the project.
cfg = load_config('api/config.yml')

# Run with
# $ IP=0.0.0.0 PORT=8080 python run.py
# or similar
if os.getenv('IP'):
  IP = os.getenv('IP')
else:
  IP = '0.0.0.0'

if os.getenv('PORT'):
  PORT = int(os.getenv('PORT'))
else:
  PORT = 8080

print ("Running at http://{0}:{1}/".format(IP, PORT))

app.tag = cfg['tag']

app.run(host = IP, port = PORT, debug = True, threaded = True)
