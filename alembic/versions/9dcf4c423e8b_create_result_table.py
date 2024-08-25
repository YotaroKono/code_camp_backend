"""create_result_table

Revision ID: 9dcf4c423e8b
Revises: b587ea98d65a
Create Date: 2024-08-25 02:33:31.456596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9dcf4c423e8b'
down_revision: Union[str, None] = 'b587ea98d65a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = "result"

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('category_id', sa.String(length=255), nullable=True),
        sa.Column('diagnosis_id', sa.Integer(), nullable=True),
        sa.Column('score', sa.Float(), nullable=True),
    )
    op.create_foreign_key(
        "fk_result_diagnosis", "result", "diagnosis",
        ["diagnosis_id"], ["id"]
    )


def downgrade() -> None:
    op.drop_table(table_name)
