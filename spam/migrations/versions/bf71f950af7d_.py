"""empty message

Revision ID: bf71f950af7d
Revises: 9ead449e06b4
Create Date: 2018-02-14 23:21:37.872700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf71f950af7d'
down_revision = '9ead449e06b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('is_desk', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('location', 'is_desk')
    # ### end Alembic commands ###