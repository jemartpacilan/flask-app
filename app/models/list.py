import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin
from .mixins.slug import SlugifiedMixin


class List(BaseMixin, SlugifiedMixin, db.Model):
  __tablename__ = 'list'

  title = db.Column(db.Text, nullable=False)
  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
  assigned_members = db.relationship('User', backref='users', nullable=True)
  cards = db.relationship('Card', backref='list', lazy=True)

  def __init__(self, title, owner_id):
    self.title = title
    self.owner_id = owner_id

  def __repr__(self):
    return '<Board %r>' % self.title