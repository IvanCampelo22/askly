"""remove user_id of the survey

Revision ID: ae71efe7973d
Revises: 9f276dd84093
Create Date: 2024-07-04 14:13:23.189140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae71efe7973d'
down_revision: Union[str, None] = '9f276dd84093'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('survey', "survey_id")


def downgrade() -> None:
    pass
