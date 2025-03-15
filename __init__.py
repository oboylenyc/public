"""
Application factory.
For details, see the Flask tutorial:
https://flask.palletsprojects.com/en/stable/tutorial/factory/

Github:
https://github.com/blep/flaskr

"""

import os
import logging
import json
import re

import boto3
from flask import Flask, render_template, send_from_directory
from . import db
from . import apikey
from . import message_controller

# lab5 includes the image_controller.
# Load it if image_controller.py is in the current directory
# If not, this throws an error, and we set image_controller to Null
#
# For a full plug-in system, we could scan the directory for anything
# named 'plugin*.py' or '*controller.py' and dynamically load each.

try:
    from . import image_controller
except ImportError as e:
    image_controller = None

LOG_LEVEL   = logging.DEBUG
USERNAME    = 'simsong'
DBFILE_NAME = 'server_db.sqlite'

# pylint: disable=redefined-outer-name
def create_app(test_config=None):
    """create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.logger.setLevel(LOG_LEVEL)

    m = re.search(r"lab(\d)",__file__)
    if m:
        lab_number = m.group(1)
    else:
        lab_number = '?'

    # See https://flask.palletsprojects.com/en/stable/config/
    app.config.from_mapping(
        # Flask configuration variables:
        SECRET_KEY='dev',
        # For development, disable caching in Flask and browser:
        TEMPLATES_AUTO_RELOAD=True,
        SEND_FILE_MAX_AGE_DEFAULT=0,

        # Additional config for lab:
        DATABASE=os.path.join(app.instance_path, DBFILE_NAME),
        LAB_NUMBER = lab_number
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello - for testing                                                                                                                                                         
    @app.route('/message')
    def message():
        return render_template('message.html')

    # Static files
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico')

    # Route templates
    @app.route('/')
    def index():
        return render_template('index.html',lab_number=app.config['LAB_NUMBER'])

    @app.route('/about')
    def about():
        return render_template('about.html')

    # This is for lab7
    @app.route('/camera')
    def camera():
        return render_template('camera.html')


    # Initialize all of the plug-ins
    db.init_app(app)
    apikey.init_app(app)
    message_controller.init_app(app)

    # If we loaded the image_controler (lab5), initialize it:
    if image_controller is not None:
        image_controller.init_app(app)

    # Return the application object
    return app

#
# If we are run from gunicorn, create the app object
#
app = create_app()