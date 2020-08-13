from app.models import Card

def test_card(app):
  card = Card(
    title='My card',
    description='Some awesome card',
  )

  assert card.title == 'My card'
  assert card.description == 'Some awesome card'