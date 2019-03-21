import logging

from typing import Optional, List, Type
from datetime import datetime

from betronic import db


class BaseModel(db.Model):
    """Abstract Base Model"""
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(),
                           onupdate=db.func.now())

    @classmethod
    def get_all(cls, db) -> List:
        return db.session.query(cls).all()

    @classmethod
    def get_by_id(cls, db, _id) -> Optional[Type['BaseModel']]:
        return db.session.query(cls).filter_by(id=_id).one()

    def update_(self, db, fields):
        try:
            db.session.query(self.__class__).\
                filter_by(id=self.id).update(fields)
            db.session.commit()
        except Exception as e:
            logging.info(str(e))
            db.session.rollback()

    @classmethod
    def remove_by_id(cls, db, _id):
        try:
            db.session.query(cls).filter_by(id=_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(str(e))

    @classmethod
    def filter_by_multiple_filters(cls, db, **kwargs):
        return db.session.query(cls).filter_by(**kwargs).all()

    @staticmethod
    def handle_date(date: Optional[str] = None, format: str = "%Y-%m-%d"):
        return datetime.strptime(date, format).date() if date else None
