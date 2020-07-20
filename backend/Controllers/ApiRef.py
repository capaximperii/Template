from flask import jsonify
from flask_restful import Api
from sqlalchemy.exc import IntegrityError

class RootApi(Api):
    def handle_error(self, e):
        if isinstance(e, IntegrityError):
            return jsonify({'message': 'Entry already exists'}), 409
        return jsonify({'message': str(e)}), 500
