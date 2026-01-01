"""new survey_id for questions

Revision ID: d35b13827930
Revises: d3d16ec515f0
Create Date: 2024-07-04 16:29:43.501239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd35b13827930'
down_revision: Union[str, None] = 'd3d16ec515f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('scale', schema=None) as batch_op:
        batch_op.add_column(sa.Column('survey_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'scale_survey_id_fkey',
            'survey', 
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )


def downgrade() -> None:
    pass
