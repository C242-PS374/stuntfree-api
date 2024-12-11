"""Drop food intake tables

Revision ID: 7c19d8f37971
Revises: 9fe868f8693b
Create Date: 2024-12-11 08:58:19.437134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '7c19d8f37971'
down_revision: Union[str, None] = '9fe868f8693b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("food_intakes")

def downgrade() -> None:
    pass
