"""add content to posts table

Revision ID: 748461b71d94
Revises: 085990630901
Create Date: 2021-12-30 17:51:05.614707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '748461b71d94'
down_revision = '085990630901'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
