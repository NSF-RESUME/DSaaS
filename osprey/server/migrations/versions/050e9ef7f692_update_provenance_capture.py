"""update provenance capture

Revision ID: 050e9ef7f692
Revises: b998244d38d5
Create Date: 2023-11-28 01:27:08.112660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '050e9ef7f692'
down_revision = 'b998244d38d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('output', schema=None) as batch_op:
        batch_op.alter_column('provenance_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('output', schema=None) as batch_op:
        batch_op.alter_column('provenance_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
