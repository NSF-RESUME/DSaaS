"""Adding modifier and flow kind

Revision ID: 2cf5303eb175
Revises: d237b106bea3
Create Date: 2023-08-03 17:12:47.006762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cf5303eb175'
down_revision = 'd237b106bea3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modifier', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('flow_kind', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_column('flow_kind')
        batch_op.drop_column('modifier')

    # ### end Alembic commands ###
