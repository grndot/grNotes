"""inserting I18Name

Revision ID: f248833e33df
Revises: ab318b14dd8a
Create Date: 2022-12-01 11:08:36.433393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f248833e33df'
down_revision = 'ab318b14dd8a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
            "Languages",
            sa.Column("I18Name", sa.VARCHAR(6)))


def downgrade():
    op.drop_column(
            "Languages",
            "I18Name")
