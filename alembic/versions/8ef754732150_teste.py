"""teste

Revision ID: 8ef754732150
Revises: da21e840f3a6
Create Date: 2024-05-29 12:03:43.119896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ef754732150'
down_revision: Union[str, None] = 'da21e840f3a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
