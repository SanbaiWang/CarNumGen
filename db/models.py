# encoding=UTF-8

from sqlalchemy import Column, Boolean, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import Base, engine, session
from random import seed, sample
import re


class VIN(Base):
    __tablename__ = 'vins'

    id = Column(Integer, primary_key=True)
    val = Column(String(17), unique=True, nullable=False, index=True)
    carnum_id = Column(Integer, ForeignKey('carnums.id'))

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return '<VIN(val=%s)>' % self.val

    @staticmethod
    def validate_vin(val):
        res = re.match(r"[a-zA-Z]{3}\d{14}", val)
        if res is None:
            raise ValueError('无效的 VIN: \n'
                             '格式错误, 必须为 3位字母 + 14位数字!')
        vin = session.query(VIN).filter_by(val=val).first()
        if vin is not None:
            raise ValueError('无效的 VIN: \n'
                             'VIN已注册!')
        return True


class CarNum(Base):
    __tablename__ = 'carnums'

    RANDOM_QUAN = 10

    id = Column(Integer, primary_key=True)
    val = Column(String(4), unique=True, nullable=False, index=True)
    registered = Column(Boolean)
    vin = relationship('VIN', uselist=False, backref='carnum')

    def __init__(self, val, registered=False):
        self.val = val
        self.registered = registered

    def __repr__(self):
        return '<CarNum(val= %s, registered=%s, vin=%s)>' % (self.val, self.registered, self.vin)

    @staticmethod
    def inject(filename):
        with open(filename, 'rb') as file:
            carnumlist = [CarNum(val=line.strip('\n')) for line in file.readlines()]
            session.add_all(carnumlist)
            session.commit()

    @staticmethod
    def rand_nums():
        query = session.query(CarNum).filter_by(registered=False)
        carnum_count = query.count()
        if carnum_count < CarNum.RANDOM_QUAN:
            return query.all()
        seed()
        return sample(query.all(), 10)


Base.metadata.create_all(engine)

