"""empty message

Revision ID: dda8609c1a09
Revises: 760e0b982f12
Create Date: 2024-11-20 20:17:32.968850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda8609c1a09'
down_revision = '760e0b982f12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('list_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('list_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###