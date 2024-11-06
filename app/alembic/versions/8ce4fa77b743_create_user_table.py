"""Create user table

Revision ID: 8ce4fa77b743
Revises: 0d2f7f9a703e
Create Date: 2024-10-23 11:18:48.370055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ce4fa77b743'
down_revision: Union[str, None] = '0d2f7f9a703e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
