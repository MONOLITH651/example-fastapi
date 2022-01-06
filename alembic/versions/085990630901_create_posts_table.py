"""create posts table

Revision ID: 085990630901
Revises: 
Create Date: 2021-12-30 17:47:05.957717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '085990630901'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass

