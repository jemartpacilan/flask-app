from app.models import Comment

def test_comment(app):
  comment = Comment(
    content='Some awesome comment'
  )

  assert comment.content == 'Some awesome comment'