"""add data in I18Name

Revision ID: baf66bdb7eef
Revises: f248833e33df
Create Date: 2022-12-01 11:13:28.775199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import column, table


# revision identifiers, used by Alembic.
revision = 'baf66bdb7eef'
down_revision = 'f248833e33df'
branch_labels = None
depends_on = None


def upgrade():
    
    lang_table = table("Languages",
            column("ID", sa.INTEGER()),
            column("Name", sa.VARCHAR(length=25)),
            column("I18Name", sa.VARCHAR(length=6))) 
    op.execute(lang_table.update().where(
        lang_table.c.ID == 1).values(
            {"I18Name":"en"}))
    op.execute(lang_table.update().where(
        lang_table.c.ID == 2).values(
            {"I18Name":"pl"}))
    op.execute(lang_table.update().where(
        lang_table.c.ID == 3).values(
            {"I18Name":"uk"}))
    op.execute(lang_table.update().where(
        lang_table.c.ID == 4).values(
            {"I18Name":"be"}))
    op.execute(lang_table.update().where(
        lang_table.c.ID == 5).values(
            {"I18Name":"cs"}))
    op.execute(lang_table.update().where(
        lang_table.c.ID == 6).values(
            {"I18Name":"de"}))


def downgrade():
    pass
