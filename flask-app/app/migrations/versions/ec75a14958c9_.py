"""empty message

Revision ID: ec75a14958c9
Revises: 
Create Date: 2020-05-31 21:32:32.594633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec75a14958c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('algorithm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('algorithmName', sa.String(length=64), nullable=True),
    sa.Column('exceString', sa.String(length=500), nullable=True),
    sa.Column('legit', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_algorithm_algorithmName'), 'algorithm', ['algorithmName'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_algorithm_algorithmName'), table_name='algorithm')
    op.drop_table('algorithm')
    # ### end Alembic commands ###
