"""empty message

Revision ID: 91bee87336a9
Revises: b35d1a9b9d87
Create Date: 2023-01-14 02:14:55.508329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91bee87336a9'
down_revision = 'b35d1a9b9d87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('username')

    # ### end Alembic commands ###