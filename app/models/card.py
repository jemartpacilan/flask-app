import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin


class Card(BaseMixin, db.Model):
  __tablename__ = 'card'

  title = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)

  comments = db.relationship('Comment', backref='card', lazy=True)
  list_id = db.Column(UUID(as_uuid=True), db.ForeignKey('list.id'), nullable=False)
  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)

  def __init__(self, title, description, position):
    self.title = title
    self.description = description

  def __repr__(self):
    return '<Card %r>' % self.title