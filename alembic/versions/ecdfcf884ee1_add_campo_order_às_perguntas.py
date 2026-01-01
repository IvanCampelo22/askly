"""add campo order às perguntas

Revision ID: ecdfcf884ee1
Revises: 3976c1bfffce
Create Date: 2024-06-11 21:03:04.838626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecdfcf884ee1'
down_revision: Union[str, None] = '3976c1bfffce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('text', sa.Column('order', sa.Integer, nullable=True))
    op.add_column('email', sa.Column('order', sa.Integer, nullable=True))
    op.add_column('document', sa.Column('order', sa.Integer, nullable=True))
    op.add_column('single_choice', sa.Column('order', sa.Integer, nullable=True))
    op.add_column('multiple_choice', sa.Column('order', sa.Integer, nullable=True))
    op.add_column('scale', sa.Column('order', sa.Integer, nullable=True))
    
    op.execute("UPDATE text SET \"order\" = 0")
    op.execute("UPDATE email SET \"order\" = 0")
    op.execute("UPDATE document SET \"order\" = 0")
    op.execute("UPDATE single_choice SET \"order\" = 0")
    op.execute("UPDATE multiple_choice SET \"order\" = 0")
    op.execute("UPDATE scale SET \"order\" = 0")
    
    # Alterar a coluna para nullable=False
    op.alter_column('text', 'order', nullable=False)
    op.alter_column('email', 'order', nullable=False)
    op.alter_column('document', 'order', nullable=False)
    op.alter_column('single_choice', 'order', nullable=False)
    op.alter_column('multiple_choice', 'order', nullable=False)
    op.alter_column('scale', 'order', nullable=False)

def downgrade() -> None:
    op.drop_column('text', 'order')
    op.drop_column('email', 'order')
    op.drop_column('document', 'order')
    op.drop_column('single_choice', 'order')
    op.drop_column('multiple_choice', 'order')
    op.drop_column('scale', 'order')
