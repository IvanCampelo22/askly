"""alter column for cascade

Revision ID: 26286a9a92c0
Revises: c64acaf8e0d8
Create Date: 2024-07-04 15:48:13.222913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26286a9a92c0'
down_revision: Union[str, None] = 'c64acaf8e0d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.add_column(sa.Column('survey_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'text_survey_id_fkey',
            'survey', 
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

def downgrade() -> None:
    pass
