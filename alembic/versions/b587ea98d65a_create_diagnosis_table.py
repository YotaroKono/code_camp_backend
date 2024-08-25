"""create_diagnosis_table

Revision ID: b587ea98d65a
Revises:
Create Date: 2024-08-25 02:23:11.327584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b587ea98d65a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = "diagnosis"

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("questions", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        comment="診断結果",
    )

def downgrade() -> None:
    op.drop_table(table_name)