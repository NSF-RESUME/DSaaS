"""updated outputs to accept a output gcs collection url

Revision ID: e6af6fccc99c
Revises: 96951d255960
Create Date: 2024-06-17 18:33:31.983577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e6af6fccc99c"
down_revision = "96951d255960"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("output", schema=None) as batch_op:
        batch_op.add_column(sa.Column("url", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("output", schema=None) as batch_op:
        batch_op.drop_column("url")

    # ### end Alembic commands ###
