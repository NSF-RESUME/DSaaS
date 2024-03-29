"""renamed source_id to output_id in output_version

Revision ID: a4b17797b8de
Revises: b2d49a4da3c2
Create Date: 2024-02-21 00:29:06.253304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a4b17797b8de"
down_revision = "b2d49a4da3c2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("output_version", schema=None) as batch_op:
        batch_op.add_column(sa.Column("output_id", sa.Integer(), nullable=True))
        batch_op.drop_constraint("output_version_source_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(None, "output", ["output_id"], ["id"])
        batch_op.drop_column("source_id")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("output_version", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("source_id", sa.INTEGER(), autoincrement=False, nullable=True)
        )
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "output_version_source_id_fkey", "output", ["source_id"], ["id"]
        )
        batch_op.drop_column("output_id")

    # ### end Alembic commands ###
