from app.models import List

def test_list(app, db, dummy_user):
  list = List(
    title='My list',
    owner_id=dummy_user.id
  )

  assert list.title == 'My list'
  assert list.owner_id == dummy_user.id