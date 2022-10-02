"""create permission

Revision ID: 954db358e316
Revises: e6043fabd4fd
Create Date: 2022-09-22 17:58:03.854627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '954db358e316'
down_revision = 'e6043fabd4fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_permission_group',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('permission_group_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['permission_group_id'], ['permission_group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_permission_group_id'), 'user_permission_group', ['id'], unique=False)
    op.drop_constraint('user_permission_permission_group_id_fkey', 'user_permission', type_='foreignkey')
    op.drop_column('user_permission', 'permission_group_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_permission', sa.Column('permission_group_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_permission_permission_group_id_fkey', 'user_permission', 'permission_group', ['permission_group_id'], ['id'])
    op.drop_index(op.f('ix_user_permission_group_id'), table_name='user_permission_group')
    op.drop_table('user_permission_group')
    # ### end Alembic commands ###
