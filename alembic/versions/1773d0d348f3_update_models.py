"""update models

Revision ID: 1773d0d348f3
Revises: 8ef754732150
Create Date: 2024-05-29 17:55:18.586874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1773d0d348f3'
down_revision: Union[str, None] = '8ef754732150'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criação da tabela multi_question
    op.create_table(
        'multi_question',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('text', sa.String(), nullable=False)
    )

    # Criação da tabela scale
    op.create_table(
        'scale',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('survey_id', sa.Integer(), sa.ForeignKey('survey.id'), nullable=False),
        sa.Column('type', sa.String(320), nullable=False),
        sa.Column('input_type', sa.String(320), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('scale_min', sa.Integer(), nullable=False),
        sa.Column('scale_max', sa.Integer(), nullable=False)
    )

    # Criação da tabela multiple_choice
    op.create_table(
        'multiple_choice',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('survey_id', sa.Integer(), sa.ForeignKey('survey.id'), nullable=False),
        sa.Column('type', sa.String(320), nullable=False),
        sa.Column('input_type', sa.String(320), nullable=False),
        sa.Column('text', sa.String(), nullable=False)
    )

    # Criação da tabela single_choice
    op.create_table(
        'single_choice',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('survey_id', sa.Integer(), sa.ForeignKey('survey.id'), nullable=False),
        sa.Column('type', sa.String(320), nullable=False),
        sa.Column('input_type', sa.String(320), nullable=False),
        sa.Column('text', sa.String(), nullable=False)
    )

    # Criação da tabela email
    op.create_table(
        'email',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('survey_id', sa.Integer(), sa.ForeignKey('survey.id'), nullable=False),
        sa.Column('type', sa.String(320), nullable=False),
        sa.Column('input_type', sa.String(320), nullable=False),
        sa.Column('text', sa.String(), nullable=False)
    )

    # Criação da tabela document
    op.create_table(
        'document',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('survey_id', sa.Integer(), sa.ForeignKey('survey.id'), nullable=False),
        sa.Column('type', sa.String(320), nullable=False),
        sa.Column('input_type', sa.String(320), nullable=False),
        sa.Column('text', sa.String(), nullable=False)
    )

    # Criação da tabela associativa para multiple_choice
    op.create_table(
        'multiple_choice_multi_questions',
        sa.Column('multiple_choice_id', sa.Integer(), sa.ForeignKey('multiple_choice.id'), primary_key=True, nullable=False),
        sa.Column('multi_question_id', sa.Integer(), sa.ForeignKey('multi_question.id'), primary_key=True, nullable=False)
    )

    # Criação da tabela associativa para single_choice
    op.create_table(
        'single_choice_multi_questions',
        sa.Column('single_choice_id', sa.Integer(), sa.ForeignKey('single_choice.id'), primary_key=True, nullable=False),
        sa.Column('multi_question_id', sa.Integer(), sa.ForeignKey('multi_question.id'), primary_key=True, nullable=False)
    )

def downgrade() -> None:
    # Remoção das tabelas na ordem inversa da criação para evitar problemas de chave estrangeira

    op.drop_table('single_choice_multi_questions')
    op.drop_table('multiple_choice_multi_questions')
    op.drop_table('document')
    op.drop_table('email')
    op.drop_table('single_choice')
    op.drop_table('multiple_choice')
    op.drop_table('scale')
    op.drop_table('multi_question')
