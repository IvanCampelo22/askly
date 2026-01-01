"""add user_id à tabela survey

Revision ID: 9f276dd84093
Revises: 42b5b58d7aba
Create Date: 2024-06-20 10:51:34.792327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '9f276dd84093'
down_revision: Union[str, None] = '42b5b58d7aba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('name', sa.String(520), nullable=False),
                    sa.Column('username', sa.String(50), nullable=False),
                    sa.Column('email', sa.String(100), nullable=False),
                    sa.PrimaryKeyConstraint('id'))

    op.create_table('survey', 
                sa.Column('id', sa.Integer, index=True, nullable=False),
                sa.Column('theme_id', sa.Integer, sa.ForeignKey('theme.id'), nullable=True),
                sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
                sa.Column('identifier_code', sa.UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False),
                sa.Column('title', sa.String(320), nullable=False),
                sa.Column('description', sa.String(520), nullable=True),
                sa.Column('version', sa.Integer, nullable=False, default=0),
                sa.Column('answered', sa.Boolean, nullable=False, default=False),
                sa.Column('updated_at', sa.DateTime(), nullable=True),
                sa.Column('created_at', sa.DateTime(), nullable=True),
                sa.PrimaryKeyConstraint('id')
                    )

def downgrade() -> None:
    op.drop_table('survey')

