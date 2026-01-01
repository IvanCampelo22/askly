"""add tabela para cliente

Revision ID: e107997dfbc8
Revises: 6228c231c271
Create Date: 2024-06-05 18:45:48.198597

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid
import datetime

# revision identifiers, used by Alembic.
revision: str = 'e107997dfbc8'
down_revision: Union[str, None] = '6228c231c271'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('client', 
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('client_code', sa.UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False),
                    sa.Column('email', sa.String(320), unique=True, nullable=False),
                    sa.Column('updated_at', sa.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
                    sa.Column('created_at', sa.DateTime, default=datetime.datetime.now),
                    sa.PrimaryKeyConstraint('id')
                )


def downgrade() -> None:
    pass
