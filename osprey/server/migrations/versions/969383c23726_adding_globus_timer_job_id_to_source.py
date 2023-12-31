"""Adding Globus Timer Job Id to Source

Revision ID: 969383c23726
Revises: 29e2a4c8947b
Create Date: 2023-07-26 16:28:10.981802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '969383c23726'
down_revision = '29e2a4c8947b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timer_job_id', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_column('timer_job_id')

    # ### end Alembic commands ###
