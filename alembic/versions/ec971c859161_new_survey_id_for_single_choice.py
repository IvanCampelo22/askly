"""new survey_id for single_choice



Revision ID: ec971c859161
Revises: 5e80d50b1e2c
Create Date: 2024-07-04 16:49:26.659284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec971c859161'
down_revision: Union[str, None] = '5e80d50b1e2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('single_choice', schema=None) as batch_op:
        batch_op.add_column(sa.Column('survey_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(
            'single_choice_survey_id_fkey',
            'survey', 
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )


def downgrade() -> None:
    pass
