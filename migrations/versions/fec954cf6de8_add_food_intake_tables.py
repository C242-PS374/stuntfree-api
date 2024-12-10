"""add food intake tables

Revision ID: fec954cf6de8
Revises: fd7c8711fa03
Create Date: 2024-12-09 17:58:59.221834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'fec954cf6de8'
down_revision: Union[str, None] = 'fd7c8711fa03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food_intakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_food_intakes_id'), 'food_intakes', ['id'], unique=False)
    op.create_index(op.f('ix_food_intakes_user_id'), 'food_intakes', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_food_intakes_user_id'), table_name='food_intakes')
    op.drop_index(op.f('ix_food_intakes_id'), table_name='food_intakes')
    op.drop_table('food_intakes')
    # ### end Alembic commands ###