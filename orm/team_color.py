from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, String
from Settings.database import Base

class Team_color(Base):
    __tablename__ = 'team_color'
    team_idx = Column(INTEGER(unsigned=False), primary_key=True)
    color = Column(String)

    def __init__(self, team_idx=None, color=None):
        self.team_idx = team_idx
        self.color = color

    def __repr__(self):
        return '<team_color %r>' % (self.team_idx)