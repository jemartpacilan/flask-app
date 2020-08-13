import os

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'postgresql://irithm:irithm@localhost:5432/irithm'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  BCRYPT_LOG_ROUNDS = 12
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'supersecret'
  PASS_SECRET_KEY = os.environ.get('PASS_SECRET_KEY') or 'pass-supersecret'
  PASS_TOKEN_AGE = 60 * 60 * 24 # 1 day age

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'postgresql://irithm_test:irithm_test@localhost:5433/irithm_test'
  TESTING = True
  BCRYPT_LOG_ROUNDS = 4
  PASS_TOKEN_AGE = 1