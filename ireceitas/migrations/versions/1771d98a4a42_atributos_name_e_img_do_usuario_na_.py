"""atributos name e img do usuario na entidade comentario

Revision ID: 1771d98a4a42
Revises: 7ca4978bf64e
Create Date: 2021-11-24 23:50:18.448252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1771d98a4a42'
down_revision = '7ca4978bf64e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comentarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imgUser', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('nameUser', sa.String(length=70), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comentarios', schema=None) as batch_op:
        batch_op.drop_column('nameUser')
        batch_op.drop_column('imgUser')

    # ### end Alembic commands ###
