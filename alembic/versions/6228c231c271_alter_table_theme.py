"""alter table theme

Revision ID: 6228c231c271
Revises: 8845f51fcc24
Create Date: 2024-06-04 10:09:56.377878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision: str = '6228c231c271'
down_revision: Union[str, None] = '8845f51fcc24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('theme', 
                    sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('description', sa.String(320), nullable=False),
                    sa.Column('updated_at', sa.DateTime, default=datetime.datetime.now),
                    sa.Column('created_at', sa.DateTime, default=datetime.datetime.now),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('theme')
