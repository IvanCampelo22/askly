"""add new tables for multi_questions

Revision ID: 8845f51fcc24
Revises: bce2529bab05
Create Date: 2024-06-03 22:54:55.298090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8845f51fcc24'
down_revision: Union[str, None] = 'bce2529bab05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("multi_question_multi", 
                sa.Column("id", sa.Integer, nullable=False),
                sa.Column("multi_choice_id", sa.Integer, sa.ForeignKey("multiple_choice.id"), nullable=False),
                sa.Column("text", sa.String, nullable=False),
                sa.PrimaryKeyConstraint('id')
                )
    
    op.create_table("multi_question_single", 
                sa.Column("id", sa.Integer, nullable=False),
                sa.Column("single_choice_id", sa.Integer, sa.ForeignKey("single_choice.id"), nullable=False),
                sa.Column("text", sa.String, nullable=False),
                sa.PrimaryKeyConstraint('id')
                )


def downgrade() -> None:
    pass
