"""empty message

Revision ID: 9100aef96c32
Revises: None
Create Date: 2016-08-04 22:58:11.037045

"""

# revision identifiers, used by Alembic.
revision = '9100aef96c32'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('migrate_version')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('migrate_version',
    sa.Column('repository_id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('repository_path', sa.TEXT(), nullable=True),
    sa.Column('version', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('repository_id')
    )
    ### end Alembic commands ###
