"""add user table

Revision ID: 4a6bbda2d705
Revises: 748461b71d94
Create Date: 2021-12-30 17:52:49.955107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a6bbda2d705'
down_revision = '748461b71d94'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
            server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        # 2 ways to setup primary key
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
