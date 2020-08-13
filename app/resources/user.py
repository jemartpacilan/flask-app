from flask import jsonify
from app.models import User as UserModel


class User(Resource):
    method_decorators = [jwt_required]

    def get(self):
        users = UserModel.query.all()
        return jsonify(json_list = users)
