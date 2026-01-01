"""add param in table theme

Revision ID: 74347180ab13
Revises: 1773d0d348f3
Create Date: 2024-06-03 18:34:45.709840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
import datetime


# revision identifiers, used by Alembic.
revision: str = '74347180ab13'
down_revision: Union[str, None] = '1773d0d348f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Reflect existing table
    metadata = MetaData()
    existing_theme = Table('theme', metadata, autoload_with=op.get_bind())

    # Redefine the table with extend_existing=True
    new_theme = Table(
        'theme',
        metadata,
        Column('id', Integer, primary_key=True, index=True),
        Column('description', String(320), nullable=False),
        Column('updated_at', DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
        Column('created_at', DateTime, default=datetime.datetime.now),
        extend_existing=True
    )

    # Update the existing table definition
    new_theme.create(op.get_bind(), checkfirst=True)


def downgrade() -> None:
    pass
