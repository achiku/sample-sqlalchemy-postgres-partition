"""add account_next_id

Revision ID: 7b4be0bd0427
Revises: 3a9238c817e5
Create Date: 2016-08-19 16:36:45.370894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b4be0bd0427'
down_revision = '3a9238c817e5'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account', 'id',
               existing_type=sa.BIGINT(),
               server_default=sa.text('account_next_id()'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account', 'id',
               existing_type=sa.BIGINT(),
               server_default=sa.text("nextval('account_id_seq1'::regclass)"))
    ### end Alembic commands ###
