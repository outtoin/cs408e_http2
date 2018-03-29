import datetime

from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String, DateTime
from Settings.database import Base

class Map_status(Base):
    __tablename__ = 'map_status'
    idx = Column(INTEGER(unsigned=False), primary_key=True, autoincrement=True)
    round = Column(Integer)
    district_id = Column(String(50))
    team_id = Column(Integer)
    up_date = Column(DateTime, default=datetime.datetime.utcnow())
    status = Column(String(100))

    def __init__(self, round, district_id, team_id, up_date, status):
        self.round = round
        self.district_id = district_id
        self.team_id = team_id
        self.up_date = up_date
        self.status = status

    def __repr__(self):
        return '<Map Status %r>' % (self.round)