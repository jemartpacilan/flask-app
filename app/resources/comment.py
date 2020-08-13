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
from app.models import Comment as CommentModel

parser = reqparse.RequestParser()
parser.add_argument('content', help='Required', required=True)

permitted = {
  'id': fields.String,
  'content': fields.String,
}

class Comment(Resource):
  method_decorators = [jwt_required]

  def post(self):
    # Create Comment
    data = parser.parse_args()
    name = data['content']

    try:
      new_comment = CommentModel(
        name=name,
      )

      new_comment.save()

      return {
        'comment': marshal(new_comment, permitted)
      }, HTTPStatus.CREATED
    except Exception as error:
      return {
        'message': str(error)
      }, HTTPStatus.INTERNAL_SERVER_ERROR

  @api_bp.route('/<int:comment_id>/update_comment/', methods=['PATCH'])
  def update_comment(self):
    data = parser.parse_args()
    comment_model = CommentModel.query.get(comment_id)
    comment_model.update(
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

  @api_bp.route('/<int:comment_id>/delete_comment/', methods=['DELETE'])
  def delete_comment(self):
    data = parser.parse_args()
    comment_model = CommentModel.query.get(comment_id)
    comment_model.delete()
    return make_response(
      jsonify({
        'message': {
          'comment': 'Successfully deleted'
        }
      }),
      HTTPStatus.DELETED
    )

  @api_bp.route('/<int:comment_id>/get_comment/', methods=['GET'])
  def get_comment(self):
    comment_model = CommentModel.query.get(comment_id)
    return jsonify(json_comment = comment_model)

  def get(self):
    comments = CommentModel.query.all()
    return jsonify(json_comment = comments)