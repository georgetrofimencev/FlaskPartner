from abc import ABCMeta
from sqlalchemy.exc import IntegrityError


class BaseManager(metaclass=ABCMeta):

    def __init__(self, model):
        self.model = model

    def add(self, db, instance):
        db.add(instance=instance)
        try:
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise e

    def create(self, db, **kwargs):
        instance = self.model(**kwargs)
        self.add(db=db, instance=instance)
        return instance
