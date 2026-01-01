"""alter column for cascade

Revision ID: 3b4be7f72771
Revises: 26286a9a92c0
Create Date: 2024-07-04 15:48:41.876303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b4be7f72771'
down_revision: Union[str, None] = '26286a9a92c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.drop_constraint('text_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'text_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )


def downgrade() -> None:
    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.drop_constraint('text_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'text_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )
