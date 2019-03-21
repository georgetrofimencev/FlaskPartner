from abc import ABCMeta, abstractmethod
from logging import getLogger
from betronic import db

logger = getLogger(__name__)


class BaseService(metaclass=ABCMeta):
    def __init__(self, args, resource_instance, result=None):
        self.args = args
        self.resource_instance = resource_instance
        self.result = result
        self.db = db

    @abstractmethod
    def get_result_handling(self):
        raise NotImplementedError()

    @abstractmethod
    def post_result_handling(self):
        raise NotImplementedError()
