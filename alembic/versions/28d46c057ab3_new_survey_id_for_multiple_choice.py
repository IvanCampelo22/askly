"""new survey_id for multiple_choice



Revision ID: 28d46c057ab3
Revises: ec971c859161
Create Date: 2024-07-04 16:50:25.514721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28d46c057ab3'
down_revision: Union[str, None] = 'ec971c859161'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('multiple_choice', schema=None) as batch_op:
        batch_op.add_column(sa.Column('survey_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(
            'multiple_choice_survey_id_fkey',
            'survey', 
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )


def downgrade() -> None:
    pass
