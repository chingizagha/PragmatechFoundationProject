"""empty message

Revision ID: 0b58f310bf58
Revises: b85910759c78
Create Date: 2021-06-15 21:04:15.673992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b58f310bf58'
down_revision = 'b85910759c78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('icon', sa.String(length=20), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.String(length=75), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    # ### end Alembic commands ###