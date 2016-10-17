"""empty message

Revision ID: b647ea596827
Revises: 6dbfa40bbf09
Create Date: 2016-10-17 17:00:55.115923

"""

# revision identifiers, used by Alembic.
revision = 'b647ea596827'
down_revision = '6dbfa40bbf09'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Sign_In', 'complete_registration',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Sign_In', 'complete_registration',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    ### end Alembic commands ###