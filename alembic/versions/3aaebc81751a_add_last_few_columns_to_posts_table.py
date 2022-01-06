"""add last few columns to posts table

Revision ID: 3aaebc81751a
Revises: 4b5d90c92e26
Create Date: 2021-12-30 18:06:57.176690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aaebc81751a'
down_revision = '4b5d90c92e26'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

