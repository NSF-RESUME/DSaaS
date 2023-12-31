"""Moving proxy relations to source_version

Revision ID: d237b106bea3
Revises: 969383c23726
Create Date: 2023-07-31 19:55:34.752519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd237b106bea3'
down_revision = '969383c23726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('provenance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('source_version_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('provenance_proxy_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'source_version', ['source_version_id'], ['id'])
        batch_op.drop_column('proxy_id')

    with op.batch_alter_table('provenance_derivation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('previous_source_version_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('provenance_derivation_previous_proxy_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'source_version', ['previous_source_version_id'], ['id'])
        batch_op.drop_column('previous_proxy_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('provenance_derivation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('previous_proxy_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('provenance_derivation_previous_proxy_id_fkey', 'proxy', ['previous_proxy_id'], ['id'])
        batch_op.drop_column('previous_source_version_id')

    with op.batch_alter_table('provenance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('proxy_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('provenance_proxy_id_fkey', 'proxy', ['proxy_id'], ['id'])
        batch_op.drop_column('source_version_id')

    # ### end Alembic commands ###
