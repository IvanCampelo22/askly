"""new survey_id for email table

Revision ID: 3b733cf08d95
Revises: d35b13827930
Create Date: 2024-07-04 16:44:49.417295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b733cf08d95'
down_revision: Union[str, None] = 'd35b13827930'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.add_column(sa.Column('survey_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(
            'email_survey_id_fkey',
            'survey', 
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )


def downgrade() -> None:
    pass
