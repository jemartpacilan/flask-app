import uuid
from http import HTTPStatus

from flask_restful import Resource, reqparse, fields, marshal

from flask_jwt_extended import (
  create_access_token,
  create_refresh_token,
  jwt_required,
  jwt_refresh_token_required,
  get_jwt_identity,
  get_raw_jwt
)
from flask import current_app, request, make_response, jsonify
from app.models import List as ListModel

parser = reqparse.RequestParser()
parser.add_argument('title', help='Required', required=True)
parser.add_argument('owner_id', help='Required', required=True)

permitted = {
  'id': fields.String,
  'title': fields.String,
  'owner_id': fields.String
}

class List(Resource):
  method_decorators = [jwt_required]

  def post(self):
    # Create List
    data = parser.parse_args()
    title = data['title']
    owner_id = data['owner_id']

    try:
      new_list = ListModel(
        title=title,
        owner_id=uuid.UUID(owner_id)
      )

      new_list.save()

      return {
        'list': marshal(new_list, permitted)
      }, HTTPStatus.CREATED
    except Exception as error:
      return {
        'message': str(error)
      }, HTTPStatus.INTERNAL_SERVER_ERROR

  @api_bp.route('/<int:list_id>/update_list/', methods=['PATCH'])
  def update_list(self):
    data = parser.parse_args()
    list_model = ListModel.query.get(list_id)
    list_model.update(
      title=data['title']
    )
    return make_response(
      jsonify({
        'message': {
          'title': 'Successfully changed'
        }
      }),
      HTTPStatus.CREATED
    )

  @api_bp.route('/<int:list_id>/delete_list/', methods=['DELETE'])
  def delete_list(self):
    data = parser.parse_args()
    list_model = ListModel.query.get(list_id)
    list_model.delete()
    return make_response(
      jsonify({
        'message': {
          'list': 'Successfully deleted'
        }
      }),
      HTTPStatus.DELETED
    )

  @api_bp.route('/<int:list_id>/get_list/', methods=['GET'])
  def get_list(self):
    list_model = ListModel.query.get(list_id)
    return jsonify(json_list = list_model)

  def get(self):
    lists = ListModel.query.all()
    return jsonify(json_list = lists)