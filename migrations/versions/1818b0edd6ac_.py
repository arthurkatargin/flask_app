"""empty message

Revision ID: 1818b0edd6ac
Revises: 98a42db07a1b
Create Date: 2019-05-12 02:50:55.404710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1818b0edd6ac'
down_revision = '98a42db07a1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_gosts',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('gost.id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gost.id'], ['gost.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_gosts')
    # ### end Alembic commands ###