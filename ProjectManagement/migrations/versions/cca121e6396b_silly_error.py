"""Silly error

Revision ID: cca121e6396b
Revises: 2a4b4c67456e
Create Date: 2018-10-17 18:07:11.181590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cca121e6396b'
down_revision = '2a4b4c67456e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('first_name', sa.String(length=10), nullable=True))
    op.add_column('User', sa.Column('surname', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'surname')
    op.drop_column('User', 'first_name')
    # ### end Alembic commands ###
