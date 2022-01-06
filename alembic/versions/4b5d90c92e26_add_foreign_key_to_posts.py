"""add foreign key to posts

Revision ID: 4b5d90c92e26
Revises: 4a6bbda2d705
Create Date: 2021-12-30 18:03:44.727762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b5d90c92e26'
down_revision = '4a6bbda2d705'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users",
     local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
