"""empty message

Revision ID: 4755d9a63086
Revises: 55fc5375c598
Create Date: 2021-06-21 14:21:46.442245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4755d9a63086'
down_revision = '55fc5375c598'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('icon')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('icon',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('icon', sa.VARCHAR(length=20), nullable=True),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('desc', sa.VARCHAR(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
