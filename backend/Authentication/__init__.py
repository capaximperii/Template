from flask import Response
from flask_login import LoginManager
from Models import UsersModel
from functools import partial
import json
import jwt

def __before_request(request, secret=''):
    if request.method == 'OPTIONS': return
    head = request.headers.get('Authorization', 'Bearer ')[7:]
    try:
        token = jwt.decode(head, secret, algorithm='RS256', verify=False)
        user = UsersModel.query.filter_by(email=token['email']).first()
        if not user:
            user = UsersModel(name=token['name'], email=token['email'])
            user.insert()
    except Exception as e:
        print(str(e))
        user = None
    return user

def __unauthorized_handle():
    message = json.dumps({'messsage': 'You are not authorized'})
    return Response(response=message, status=403, headers={'Content-Type': 'application/json'})


def initialize(appl):
    login_manager = LoginManager(appl)
    before_request = partial(__before_request, secret=appl.config['GOOGLE_SECRET'])
    login_manager.request_loader(before_request)
    login_manager.unauthorized_handler(__unauthorized_handle)