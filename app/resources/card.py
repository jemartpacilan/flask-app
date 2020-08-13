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
from app.models import Card as CardModel

parser = reqparse.RequestParser()
parser.add_argument('title', help='Required', required=True)
parser.add_argument('description', help='Required', required=True)
parser.add_argument('owner_id', help='Required', required=True)

permitted = {
  'id': fields.String,
  'title': fields.String,
  'description': fields.String,
  'owner_id': fields.String
}

class Card(Resource):
  method_decorators = [jwt_required]

  def post(self):
    # Create Card
    data = parser.parse_args()
    title = data['title']
    description = data['description']
    owner_id = data['owner_id']

    try:
      new_card = CardModel(
        title=title,
        description=description,
        owner_id=uuid.UUID(owner_id)
      )

      new_card.save()

      return {
        'card': marshal(new_card, permitted)
      }, HTTPStatus.CREATED
    except Exception as error:
      return {
        'message': str(error)
      }, HTTPStatus.INTERNAL_SERVER_ERROR

  @api_bp.route('/<int:card_id>/update_card/', methods=['PATCH'])
  def update_card(self):
    data = parser.parse_args()
    card_model = CardModel.query.get(card_id)
    card_model.update(
      title=data['title'],
      description=data['description']
    )
    return make_response(
      jsonify({
        'message': {
          'card': 'Successfully changed'
        }
      }),
      HTTPStatus.CREATED
    )

  @api_bp.route('/<int:card_id>/delete_card/', methods=['DELETE'])
  def delete_card(self):
    data = parser.parse_args()
    card_model = CardModel.query.get(card_id)
    card_model.delete()
    return make_response(
      jsonify({
        'message': {
          'card': 'Successfully deleted'
        }
      }),
      HTTPStatus.DELETED
    )

  @api_bp.route('/<int:card_id>/get_card/', methods=['GET'])
  def get_card(self):
    card_model = CardModel.query.get(card_id)
    return jsonify(json_card = card_model)

  def get(self):
    cards = CardModel.query.all()
    return jsonify(json_card = cards)