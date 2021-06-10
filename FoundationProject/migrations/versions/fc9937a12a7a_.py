"""empty message

Revision ID: fc9937a12a7a
Revises: af363e9d8f04
Create Date: 2021-06-10 17:02:55.833211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc9937a12a7a'
down_revision = 'af363e9d8f04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('icon', sa.String(length=20), nullable=True),
    sa.Column('desc', sa.String(length=50), nullable=False),
    sa.Column('big_desc', sa.String(length=75), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('theme')
    op.drop_table('address')
    # ### end Alembic commands ###