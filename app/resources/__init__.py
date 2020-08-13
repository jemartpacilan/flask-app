from .base import api, api_bp, jwt
from .auth import Auth
from .register import Register
from .list import List
from .user import User
from .card import Card
from .comment import Comment

import app.resources.password

api.add_resource(Auth, '/auth')
api.add_resource(Register, '/auth/register')
api.add_resource(List, '/list')
api.add_resource(User, '/users')
api.add_resource(Card, '/cards')
api.add_resource(Comment, '/comments')

__all__ = [
  'api',
  'api_bp',
  'jwt',
  'Auth',
  'Register'
]