from flask import Flask, request
from flask import render_template
import urllib2
import json
import random
import uuid
from google.appengine.api import users
from google.appengine.api import channel
from utilities import funnames

import auth

from main import app

  
@app.route('/one_player/')
def one_player():
	return render_template(
		'one_player.html',
		html_class='one-player',
		title='Memory Game'
	)

@app.route('/two_player/')
def two_player():
	return render_template(
		'two_player.html',
		html_class='two-player',
		title='Memory Game'
	)
	
