from flask import Blueprint, request
from flask_restful import Resource
from flask_login import login_required, current_user
from Models import UsersModel, UsersSchema
from werkzeug.exceptions import Forbidden

from Controllers.ApiRef import RootApi


class UsersController(Resource):
    @login_required
    def get(self):
        user = UsersModel.query.filter_by(email=current_user.email).first()
        schema = UsersSchema(many=False)
        return schema.dump(user)

    @login_required
    def put(self):
        schema = UsersSchema(many=False)
        user = schema.load(request.get_json())
        if current_user.email != user.email:
            raise Forbidden('You can only edit yourself.')
        user.update()
        return schema.dump(user)

UsersApi = Blueprint('Users', __name__, url_prefix='/api/users')
__api = RootApi(UsersApi)
__api.add_resource(UsersController, '')
