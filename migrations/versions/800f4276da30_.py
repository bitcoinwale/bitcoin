"""empty message

Revision ID: 800f4276da30
Revises: 7adc828b6c7c
Create Date: 2016-10-20 01:13:36.800948

"""

# revision identifiers, used by Alembic.
revision = '800f4276da30'
down_revision = '7adc828b6c7c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('queries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('mob', sa.String(length=15), nullable=False),
    sa.Column('ques', sa.String(length=160), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_queries_email'), 'queries', ['email'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('mob', sa.String(length=15), nullable=False),
    sa.Column('comp_register', sa.Boolean(), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('pincode', sa.Integer(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mob')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('tranactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('acc_no', sa.String(length=20), nullable=False),
    sa.Column('acc_name', sa.String(length=64), nullable=False),
    sa.Column('bank', sa.String(length=64), nullable=False),
    sa.Column('ifsc', sa.String(length=20), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('type', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('bit_value', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Queries')
    op.drop_table('Sign_In')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Sign_In',
    sa.Column('user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('email_id', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('mob_no', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('complete_registration', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('password', mysql.VARCHAR(length=16), nullable=True),
    sa.Column('purchase_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('pincode', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('Queries',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('email_id', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('mob_no', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('ques', mysql.VARCHAR(length=160), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('tranactions')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_queries_email'), table_name='queries')
    op.drop_table('queries')
    ### end Alembic commands ###
