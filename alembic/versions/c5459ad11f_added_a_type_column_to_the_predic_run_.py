"""added a type column to the predic_run table

Revision ID: c5459ad11f
Revises: 4a4f853473ff
Create Date: 2016-02-16 23:03:24.671799

"""

# revision identifiers, used by Alembic.
revision = 'c5459ad11f'
down_revision = '4a4f853473ff'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_prediction_run', sa.Column('type', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_prediction_run', 'type')
    ### end Alembic commands ###
