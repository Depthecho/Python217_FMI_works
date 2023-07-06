from sqlalchemy import Column, Integer, String
from .Database import Base
from sqlalchemy.orm import relationship, backref


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(100), nullable=False)
    student = relationship('Student')

    def __repr__(self):
        return f'Id of Group: {self.id}, ' \
                f'Name of Group: {self.group_name}'