#!/usr/bin/python

from flask import Flask
from flask import render_template

import requests

client_id = '293e5c53495a034defc93aa172ea00ac'

app = Flask(__name__)

@app.route('/favorite_songs/<string:user>')
def favorite_songs(user):
	favorites = requests.get('http://api.soundcloud.com/users/' + user + '/favorites.json', params={'client_id': client_id})
	return render_template('index.html', favorites_json=favorites.json())	

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
