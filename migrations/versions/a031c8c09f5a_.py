"""empty message

Revision ID: a031c8c09f5a
Revises: 1fae0df53424
Create Date: 2017-10-17 17:13:57.908000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a031c8c09f5a'
down_revision = '1fae0df53424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('c_time', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('user', sa.Column('up_time', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'up_time')
    op.drop_column('user', 'c_time')
    # ### end Alembic commands ###