"""new survey_id for document, single_choice, multiple_choice table

Revision ID: 5e80d50b1e2c
Revises: 3b733cf08d95
Create Date: 2024-07-04 16:47:37.863808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e80d50b1e2c'
down_revision: Union[str, None] = '3b733cf08d95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('document', schema=None) as batch_op:
        batch_op.add_column(sa.Column('survey_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(
            'document_survey_id_fkey',
            'survey', 
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )


def downgrade() -> None:
    pass
