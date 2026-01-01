"""create table survey

Revision ID: 0053021800d0
Revises: 1b00195af61a
Create Date: 2024-05-28 21:48:50.716492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0053021800d0'
down_revision: Union[str, None] = '1b00195af61a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('survey', 
                sa.Column('id', sa.Integer, index=True, nullable=False),
                sa.Column('theme_id', sa.Integer, sa.ForeignKey('theme.id'), nullable=True),
                sa.Column('title', sa.String(320), nullable=False),
                sa.Column('description', sa.String(520), nullable=True),
                sa.Column('updated_at', sa.DateTime(), nullable=True),
                sa.Column('created_at', sa.DateTime(), nullable=True),
                sa.PrimaryKeyConstraint('id')
                    )
    
    op.add_column('theme', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('theme', sa.Column('created_at', sa.DateTime(), nullable=True))


def downgrade() -> None:
    pass
