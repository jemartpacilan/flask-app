from app.models import User

def test_user(app):
  user = User(
    email='bruce@irithm.com',
    password='password123'
  )

  user.first_name = 'Bruce'
  user.last_name = 'Wayne'

  assert user.first_name == 'Bruce'
  assert user.last_name == 'Wayne'
  assert user.email == 'bruce@irithm.com'
  assert user._password != 'password123'