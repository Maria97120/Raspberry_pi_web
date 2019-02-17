from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask import Response
from flask_bootstrap import Bootstrap

import DB_redis_web
import datas_for_flask

import json
import time

app = Flask(__name__)

def Response_headers(content):
	resp = Response(content)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/rasp4_data', methods={'GET', 'POST'})
def rasp4_data():
	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp
	
@app.route('/rasp3_data', methods={'GET', 'POST'})
def rasp3_data():
	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp
	
@app.route('/rasp2_data', methods={'GET', 'POST'})
def rasp2_data():
	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp
	
@app.route('/rasp1_data', methods={'GET', 'POST'})
def rasp1_data():

	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp

@app.route('/tem_hum_data', methods={'GET', 'POST'})
def tem_hum_data():
	
	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp
	
@app.route('/rain_data', methods={'GET', 'POST'})
def raining_data():
	
	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp
	
@app.route('/people_data', methods={'GET', 'POST'})
def peo_data():

	datas=datas_for_flask.Rasp_number().make_datas('01')
	
	content = json.dumps(datas)
	resp = Response_headers(content)
	return resp
	
@app.route('/index.html', methods={'GET', 'POST'})
def index():
	return render_template('index.html')
	
@app.route('/people.html', methods={'GET', 'POST'})
def people():
	return render_template('people.html')
	
@app.route('/temp_wet.html', methods={'GET', 'POST'})
def temp_hum():
	return render_template('temp_wet.html')
	
@app.route('/rain.html', methods={'GET', 'POST'})
def rain():
	return render_template('rain.html')

@app.route('/rasp1.html', methods={'GET', 'POST'})
def rasp1():
	fog=datas_for_flask.Rasp_number().fog_data('01')
	if fog:
		fog="Fogging !"
	else:
		fog="Not Fogging !"
	return render_template('rasp1.html',fog=fog)

@app.route('/rasp2.html', methods={'GET', 'POST'})
def rasp2():
	fog=datas_for_flask.Rasp_number().fog_data('01')
	if fog:
		fog="Fogging !"
	else:
		fog="Not Fogging !"
	return render_template('rasp2.html',fog=fog)
	
@app.route('/rasp3.html', methods={'GET', 'POST'})
def rasp3():
	fog=datas_for_flask.Rasp_number().fog_data('01')
	if fog:
		fog="Fogging !"
	else:
		fog="Not Fogging !"
	return render_template('rasp3.html',fog=fog)
	
@app.route('/rasp4.html', methods={'GET', 'POST'})
def rasp4():
	fog=datas_for_flask.Rasp_number().fog_data('01')
	if fog:
		fog="Fogging !"
	else:
		fog="Not Fogging !"
	return render_template('rasp4.html',fog=fog)
	
@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)