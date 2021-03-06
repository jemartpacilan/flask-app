import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property

from .base import db, bcrypt
from .mixins.base import BaseMixin
from flask import current_app


list = db.Table('user_list',
  db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True),
  db.Column('list_id', UUID(as_uuid=True), db.ForeignKey('list.id'), primary_key=True)
)

cards = db.Table('user_card',
  db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True),
  db.Column('card_id', UUID(as_uuid=True), db.ForeignKey('card.id'), primary_key=True)
)


class User(BaseMixin, db.Model):
  __tablename__ = 'user'

  first_name = db.Column(db.Text, nullable=True)
  last_name = db.Column(db.Text, nullable=True)
  username = db.Column(db.Text, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  is_admin = db.Column(db.Boolean, default=False, nullable=False)
  _password = db.Column(db.String(128))

  comments = db.relationship('Comment', backref='author', lazy=True)
  owned_list = db.relationship('List', backref='owner', lazy=True)
  owned_cards = db.relationship('Card', backref='owner', lazy=True)

  list = db.relationship('List', secondary=list, lazy='subquery',
    backref=db.backref('user', lazy=True))

  cards = db.relationship('Card', secondary=cards, lazy='subquery',
    backref=db.backref('user', lazy=True))

  def __init__(self, email, password):
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User %r>' % self.email

  @hybrid_property
  def password(self):
    return self._password

  @password.setter
  def password(self, plaintext):
    self._password = bcrypt.generate_password_hash(
      plaintext,
      current_app.config.get('BCRYPT_LOG_ROUNDS')
    ).decode('utf-8')

  def password_match(self, plaintext):
    return bcrypt.check_password_hash(self.password, plaintext)

  @classmethod
  def get_by_email(cls, email):
    return cls.query.filter_by(email = email).first()