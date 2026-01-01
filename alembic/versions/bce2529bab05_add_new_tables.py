"""add new tables

Revision ID: bce2529bab05
Revises: 74347180ab13
Create Date: 2024-06-03 22:47:20.142919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bce2529bab05'
down_revision: Union[str, None] = '74347180ab13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'multiple_choice',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('survey_id', sa.Integer(), sa.ForeignKey('survey.id'), nullable=False),
        sa.Column('type', sa.String(320), nullable=False),
        sa.Column('input_type', sa.String(320), nullable=False),
        sa.Column('text', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('multiple_choice')
    op.drop_table('multiple_choice_multi_questions')
    op.drop_table('single_choice_multi_questions')