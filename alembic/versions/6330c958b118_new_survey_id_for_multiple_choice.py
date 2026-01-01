"""new survey_id for multiple_choice



Revision ID: 6330c958b118
Revises: 28d46c057ab3
Create Date: 2024-07-04 16:50:50.256022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6330c958b118'
down_revision: Union[str, None] = '28d46c057ab3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
