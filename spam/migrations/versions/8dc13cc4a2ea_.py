"""empty message

Revision ID: 8dc13cc4a2ea
Revises:
Create Date: 2018-02-14 19:17:02.065959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dc13cc4a2ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('map_node', sa.String(length=50), nullable=False),
    sa.Column('location_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location_name'),
    sa.UniqueConstraint('map_node')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_staff_name'), 'staff', ['name'], unique=True)
    op.create_table('problem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('origin', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=200), nullable=False),
    sa.Column('solved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['origin'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('problem')
    op.drop_index(op.f('ix_staff_name'), table_name='staff')
    op.drop_table('staff')
    op.drop_table('location')
    # ### end Alembic commands ###
