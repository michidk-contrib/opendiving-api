"""Add independent unit preferences, preserving every account's existing preset

Revision ID: a8c9743e21b0
Revises: c4a8e2d6f1b3
Create Date: 2026-11-12 08:10:00.000000
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "a8c9743e21b0"
down_revision: str | None = "c4a8e2d6f1b3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("user", sa.Column("unit_preferences", sa.JSON(), server_default="{}", nullable=False))


def downgrade() -> None:
    op.drop_column("user", "unit_preferences")
