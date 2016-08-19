"""add id generation func

Revision ID: b1af7b0fd182
Revises:
Create Date: 2016-08-19 14:15:46.052338

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b1af7b0fd182'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SEQUENCE account_id_seq")
    op.execute("""
    CREATE OR REPLACE FUNCTION account_next_id(OUT result bigint) AS $$
    DECLARE
        our_epoch bigint := 1314220021721;
        seq_id bigint;
        now_millis bigint;
        shard_id int := 1;
    BEGIN
        SELECT nextval('account_id_seq') % 1024 INTO seq_id;

        SELECT FLOOR(EXTRACT(EPOCH FROM clock_timestamp()) * 1000) INTO now_millis;
        result := (now_millis - our_epoch) << 23;
        result := result | (shard_id << 10);
        result := result | (seq_id);
    END;
    $$ LANGUAGE PLPGSQL;
    """)


def downgrade():
    op.execute("DROP FUNCTION account_next_id(OUT result bigint)")
    op.execute("DROP SEQUENCE account_id_seq")
