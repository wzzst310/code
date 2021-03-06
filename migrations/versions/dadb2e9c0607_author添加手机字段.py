"""Author添加手机字段

Revision ID: dadb2e9c0607
Revises: 161093c18654
Create Date: 2019-02-20 00:31:50.431235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dadb2e9c0607'
down_revision = '161093c18654'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('mobile', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_authors', 'mobile')
    # ### end Alembic commands ###
