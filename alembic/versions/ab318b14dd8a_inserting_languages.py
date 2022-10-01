"""inserting languages

Revision ID: ab318b14dd8a
Revises: 0dcc17710f69
Create Date: 2022-10-01 15:27:48.006493

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import column, table


# revision identifiers, used by Alembic.
revision = 'ab318b14dd8a'
down_revision = '0dcc17710f69'
branch_labels = None
depends_on = None


def upgrade():
    
    lang_table = table("Languages",
            column("ID", sa.INTEGER()),
            column("Name", sa.VARCHAR(length=25)))
    
    op.bulk_insert(lang_table,
            [
                {
                    "ID": 1,
                    "Name": "English"},
                {
                    "ID": 2,
                    "Name": "Polish"},
                {
                    "ID": 3,
                    "Name": "Ukranian"},
                {
                    "ID": 4,
                    "Name": "Belarussian"},
                {
                    "ID": 5,
                    "Name": "Czech"},
                {
                    "ID": 6,
                    "Name": "Deusch"},
                ])



def downgrade():
    pass
