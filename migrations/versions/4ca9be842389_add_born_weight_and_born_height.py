"""Add born_weight and born_height

Revision ID: 4ca9be842389
Revises: fec954cf6de8
Create Date: 2024-12-11 02:59:33.928636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '4ca9be842389'
down_revision: Union[str, None] = 'fec954cf6de8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user_profile", sa.Column("child_born_height", sa.Float(), nullable=True))
    op.add_column("user_profile", sa.Column("child_born_weight", sa.Float(), nullable=True))


def downgrade() -> None:
    op.drop_column("user_profile", "child_born_weight")
    op.drop_column("user_profile", "child_born_height")
