"""first migration

Revision ID: bac8f9228512
Revises: 
Create Date: 2024-04-10 22:22:59.281829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bac8f9228512'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pictures',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='Идентификатор картинки'),
    sa.Column('path', sa.String(), nullable=True, comment='Путь к картинке в хранилище'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='Идентификатор тега'),
    sa.Column('name', sa.String(), nullable=True, comment='Имя тега'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='Идентификатор пользователя'),
    sa.Column('username', sa.String(), nullable=True, comment='Имя пользователя'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('collections',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='Идентификатор коллекции'),
    sa.Column('author_id', sa.Integer(), nullable=True, comment='Идентификатор автора'),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('picture_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'picture_id')
    )
    op.create_table('tag_to_pic_enrol',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('picture_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'picture_id')
    )
    op.create_table('col_to_pic_enrol',
    sa.Column('collection_id', sa.Integer(), nullable=False),
    sa.Column('picture_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], ),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ),
    sa.PrimaryKeyConstraint('collection_id', 'picture_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('col_to_pic_enrol')
    op.drop_table('tag_to_pic_enrol')
    op.drop_table('likes')
    op.drop_table('collections')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('pictures')
    # ### end Alembic commands ###