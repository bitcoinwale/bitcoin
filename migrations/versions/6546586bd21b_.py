"""empty message

Revision ID: 6546586bd21b
Revises: a96c1aed2e8a
Create Date: 2016-10-10 01:12:36.244577

"""

# revision identifiers, used by Alembic.
revision = '6546586bd21b'
down_revision = 'a96c1aed2e8a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Sign_In', 'complete_registration',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Sign_In', 'complete_registration',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    ### end Alembic commands ###