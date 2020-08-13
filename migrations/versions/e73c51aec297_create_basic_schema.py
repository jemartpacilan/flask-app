from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e73c51aec297'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=False),
    sa.Column('username', sa.Text(), nullable=False),
    sa.Column('is_admin', sa.Boolean, default=False, nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('_password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('list',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('slug', sa.Text(), nullable=False),
    sa.Column('owner_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('user_list',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('list_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'list_id')
    )
    op.create_table('card',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('list_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('owner_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('card_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_card',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('card_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'card_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_card')
    op.drop_table('comment')
    op.drop_table('card')
    op.drop_table('user_list')
    op.drop_table('list')
    op.drop_table('user')
    # ### end Alembic commands ###
