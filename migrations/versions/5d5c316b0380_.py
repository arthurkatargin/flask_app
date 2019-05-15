"""empty message

Revision ID: 5d5c316b0380
Revises: 1818b0edd6ac
Create Date: 2019-05-14 13:40:01.466264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5c316b0380'
down_revision = '1818b0edd6ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gost', sa.Column('body', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gost', 'body')
    # ### end Alembic commands ###
