"""init

Revision ID: bc9d1c310c36
Revises:
Create Date: 2025-09-28 06:37:05.224680

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bc9d1c310c36"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Integer,
            nullable=False,
            autoincrement=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name="pk_users__id",
        ),
        sa.Column(
            "name",
            sa.String(64),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
