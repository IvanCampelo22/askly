"""initial migration

Revision ID: 1b00195af61a
Revises: 
Create Date: 2024-05-28 21:29:42.821308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b00195af61a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('theme', sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('description', sa.String(320), nullable=False),
                    )


def downgrade() -> None:
    pass
