"""remove survey_id of the tables

Revision ID: d3d16ec515f0
Revises: 3b4be7f72771
Create Date: 2024-07-04 16:21:37.396179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3d16ec515f0'
down_revision: Union[str, None] = '3b4be7f72771'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('scale', 'survey_id')
    op.drop_column('single_choice', 'survey_id')
    op.drop_column('multiple_choice', 'survey_id')
    op.drop_column('document', 'survey_id')
    op.drop_column('email', 'survey_id')



def downgrade() -> None:
    pass
