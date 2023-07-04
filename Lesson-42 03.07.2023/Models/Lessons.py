from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .Database import Base
from sqlalchemy.orm import relationship


association_table = Table('association', Base.metadata,
                          Column('lesson_id', Integer, ForeignKey('lessons_id')),
                          Column('group_id', Integer, ForeignKey('groups_id')))


class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_title = Column(String(100), nullable=False)
    groups = relationship('Group', secondary='association', backref='lessons')

    def __repr__(self):
        return f' Id of lesson: {self.id}, ' \
               f'Name of lesson: {self.name}'
