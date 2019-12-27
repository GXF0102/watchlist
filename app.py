from flask import Flask
from flask import url_for
app=Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
	return u"欢迎来的我的世界 watchlist！"
	#return '<h1>Hello Totoro!</h1><img src="http://hellflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_pagge(name):
	return 'User: %s' % name

@app.route('/test')
def test_url_for():
	print(url_for("hello"))
	print(url_for("user_pagge",name="greyli"))
	print(url_for("user_pagge","peter"))
	print(url_for('test_url_for'))
	print(url_for('test_url_for',num=2))
	return 'Test Page'


