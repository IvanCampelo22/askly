"""add user_id ao survey

Revision ID: 0666982756ad
Revises: ae71efe7973d
Create Date: 2024-07-04 14:50:41.741090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0666982756ad'
down_revision: Union[str, None] = 'ae71efe7973d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('survey', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'survey_user_id_fkey',
            'users', 
            ['user_id'], ['id'],
            ondelete='CASCADE'
        )

def downgrade() -> None:
    pass
