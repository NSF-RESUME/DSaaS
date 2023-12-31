"""Many-to-Many Source and Tags

Revision ID: b95dbe8c0812
Revises: 37d2bc3fa266
Create Date: 2023-06-26 16:47:32.823482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b95dbe8c0812'
down_revision = '37d2bc3fa266'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proxy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('representation', sa.String(), nullable=True),
    sa.Column('source_version_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['source_version_id'], ['source_version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('proxy')
    # ### end Alembic commands ###
