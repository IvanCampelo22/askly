"""add identifier_code a tabela survey

Revision ID: 3976c1bfffce
Revises: e107997dfbc8
Create Date: 2024-06-10 08:19:02.836052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '3976c1bfffce'
down_revision: Union[str, None] = 'e107997dfbc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('survey', sa.Column('identifier_code', sa.UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False))


def downgrade() -> None:
    pass
