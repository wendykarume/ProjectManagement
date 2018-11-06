"""Clean Up

Revision ID: 222099eb8bd8
Revises: 6487fba54716
Create Date: 2018-11-06 10:32:21.267592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '222099eb8bd8'
down_revision = '6487fba54716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('team_no', sa.String(), nullable=True),
    sa.Column('project_type', sa.String(), nullable=True),
    sa.Column('organization', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Register')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Register',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Register_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('team_no', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('project_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('organization', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('project_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Register_pkey')
    )
    op.drop_table('Projects')
    # ### end Alembic commands ###
