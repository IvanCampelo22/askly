"""add passive delete nas tabelas

Revision ID: 42b5b58d7aba
Revises: 8183abc1d954
Create Date: 2024-06-13 10:15:42.868505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42b5b58d7aba'
down_revision: Union[str, None] = '8183abc1d954'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.drop_constraint('text_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'text_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

    with op.batch_alter_table('scale', schema=None) as batch_op:
        batch_op.drop_constraint('scale_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'scale_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

    
    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.drop_constraint('email_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'email_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

    with op.batch_alter_table('document', schema=None) as batch_op:
        batch_op.drop_constraint('document_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'document_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

    with op.batch_alter_table('multiple_choice', schema=None) as batch_op:
        batch_op.drop_constraint('multiple_choice_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'multiple_choice_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

    with op.batch_alter_table('single_choice', schema=None) as batch_op:
        batch_op.drop_constraint('single_choice_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'single_choice_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete='CASCADE'
        )

    with op.batch_alter_table('multi_question_multi', schema=None) as batch_op:
        batch_op.drop_constraint('multi_question_multi_multi_choice_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'multi_question_multi_multi_choice_id_fkey',
            'multiple_choice',
            ['multi_choice_id'], ['id'],
            ondelete='CASCADE'
        )

    with op.batch_alter_table('multi_question_single', schema=None) as batch_op:
        batch_op.drop_constraint('multi_question_single_single_choice_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'multi_question_single_single_choice_id_fkey',
            'single_choice',
            ['single_choice_id'], ['id'],
            ondelete='CASCADE'
        )

def downgrade() -> None:
    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.drop_constraint('text_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'text_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )


    with op.batch_alter_table('scale', schema=None) as batch_op:
        batch_op.drop_constraint('scale_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'scale_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )


    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.drop_constraint('email_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'email_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )

    with op.batch_alter_table('document', schema=None) as batch_op:
        batch_op.drop_constraint('document_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'document_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )


    with op.batch_alter_table('multiple_choice', schema=None) as batch_op:
        batch_op.drop_constraint('multiple_choice_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'multiple_choice_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )


    with op.batch_alter_table('single_choice', schema=None) as batch_op:
        batch_op.drop_constraint('single_choice_survey_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'single_choice_survey_id_fkey',
            'survey',
            ['survey_id'], ['id'],
            ondelete=None
        )

    with op.batch_alter_table('multi_question_multi', schema=None) as batch_op:
        batch_op.drop_constraint('multi_question_multi_multi_choice_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'multi_question_multi_multi_choice_id_fkey',
            'multiple_choice',
            ['multi_choice_id'], ['id'],
            ondelete=None
        )

    with op.batch_alter_table('multi_question_single', schema=None) as batch_op:
        batch_op.drop_constraint('multi_question_single_single_choice_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'multi_question_single_single_choice_id_fkey',
            'single_choice',
            ['single_choice_id'], ['id'],
            ondelete=None
        )