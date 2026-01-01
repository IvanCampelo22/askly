"""add novas colunas ao survey

Revision ID: 8183abc1d954
Revises: ecdfcf884ee1
Create Date: 2024-06-12 20:32:21.320812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '8183abc1d954'
down_revision: Union[str, None] = 'ecdfcf884ee1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('survey', sa.Column('version', sa.Integer, nullable=True, default=0))
    op.add_column('survey', sa.Column('answered', sa.Boolean, nullable=True, default=False))

    op.execute('UPDATE survey SET \"version\" = 0')
    op.execute('UPDATE survey SET \"answered\" = false')

    op.alter_column('survey', 'version', nullable=False)
    op.alter_column('survey', 'answered', nullable=False)

def downgrade() -> None:
    op.drop_column('survey', 'version')
    op.drop_column('survey', 'answered')

