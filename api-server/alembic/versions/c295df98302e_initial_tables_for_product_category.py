"""Initial tables for Product & Category

Revision ID: c295df98302e
Revises: 
Create Date: 2023-08-19 12:44:41.487088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c295df98302e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('strCategory', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('strCategory')
    )
    op.create_index(op.f('ix_categories_strCategory'), 'categories', ['strCategory'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('strName', sa.String(), nullable=False),
    sa.Column('strDescription', sa.String(), nullable=False),
    sa.Column('strImg', sa.String(), nullable=False),
    sa.Column('intPrice', sa.Integer(), nullable=False),
    sa.Column('intInventory', sa.Integer(), nullable=True),
    sa.Column('strCategory', sa.String(), nullable=True),
    sa.Column('onSale', sa.Boolean(), server_default='False', nullable=True),
    sa.ForeignKeyConstraint(['strCategory'], ['categories.strCategory'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('strDescription'),
    sa.UniqueConstraint('strImg')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_index(op.f('ix_categories_strCategory'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
