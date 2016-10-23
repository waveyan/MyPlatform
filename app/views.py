from flask import render_template, request, jsonify, make_response

from app import app
from config import ARTICLES_NAME
from app.controls import robot, oauth
from app.models.articles import get_articles

@app.route('/', methods=['GET', 'POST'])
def receive_msg():
	#oauth验证微信
    if not oauth.oauth(request): return 'Hello world!'
    if request.method == 'GET': return request.args.get('echostr', 'Please use post to send msg!')
    response = make_response(robot.deal_with_msg(request.data))
    response.content_type = 'application/xml'
    return response

@app.route('/dgpk/')
def show_articles_list():
    return render_template('tabs.html')

@app.route('/dgpk/contents/')
def json_contents():
    return jsonify(response=get_articles(ARTICLES_NAME))
