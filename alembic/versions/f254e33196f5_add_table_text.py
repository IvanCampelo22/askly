"""add table text

Revision ID: da21e840f3a6
Revises: 0053021800d0
Create Date: 2024-05-29 11:59:40.271336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da21e840f3a6'
down_revision: Union[str, None] = '0053021800d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('text', 
                    sa.Column('id', sa.Integer, index=True, nullable=False),
                    sa.Column('survey_id', sa.Integer, sa.ForeignKey('survey.id'), nullable=False),
                    sa.Column('type', sa.String(320), nullable=False),
                    sa.Column('input_type', sa.String(320), nullable=False),
                    sa.Column('text', sa.String(320), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    pass
