"""empty message

Revision ID: ff63d47e8208
Revises: 509d6a7d4e6c
Create Date: 2016-08-05 22:27:25.317463

"""

# revision identifiers, used by Alembic.
revision = 'ff63d47e8208'
down_revision = '509d6a7d4e6c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_last_name', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'first_last_name')
    ### end Alembic commands ###
