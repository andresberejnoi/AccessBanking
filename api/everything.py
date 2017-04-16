######################################################
# IMPORTS
######################################################
# Python 2/3 compat
from __future__ import print_function
import os, pprint
# We need a bunch of Flask stuff
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import json
from flask import url_for
from flask import g
from flask import session
from flask import jsonify
from flask import send_from_directory
from flask import flash
from flask import abort

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


######################################################
# SETUP
######################################################
# Set up the Flask app
base_path = os.path.dirname(__file__)
app = Flask(__name__)

from api.util import load_config

# cfg = load_config('/var/www/html/urcpp-flask/api/config.yaml')
cfg = load_config(os.path.join(base_path, 'config.yml'))
app.config['SECRET_KEY'] = open(os.path.join(base_path, 'secret_key'), 'rb').read()
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER