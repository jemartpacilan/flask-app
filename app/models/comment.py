import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin

class Comment(BaseMixin, db.Model):
  __tablename__ = 'comment'

  content = db.Column(db.Text, nullable=False)

  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
  card_id = db.Column(UUID(as_uuid=True), db.ForeignKey('card.id'), nullable=False)
  parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
  replies = db.relationship(
    'Comment', backref=db.backref('parent', remote_side=[id]),
    lazy='dynamic')

  def __init__(self, content):
    self.content = content

  def __repr__(self):
    return '<Comment %r>' % self.id