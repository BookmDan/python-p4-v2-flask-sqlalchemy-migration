"""rename address

Revision ID: b4f7571e656e
Revises: 9989c40bd475
Create Date: 2023-12-22 16:47:38.602062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4f7571e656e'
down_revision = '9989c40bd475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('departments', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('location', sa.String(), nullable=False))
    #     batch_op.drop_column('address')
    op.alter_column('departments', 'address',  new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('departments', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('address', sa.VARCHAR(), nullable=True))
    #     batch_op.drop_column('location')
    op.alter_column('departments', 'location',  new_column_name='address')

    # ### end Alembic commands ###
