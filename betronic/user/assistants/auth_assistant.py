from betronic.user.model import UserModel
from logging import getLogger

from core.abstract_result.invalid import InvalidRequestData
from core.abstract_result.codes import ErrorCode


logger = getLogger(__name__)


class AuthAssistant:
    def __init__(self, db):
        self.db = db

    def register(self, data):
        self.check_email_validity(data["email"])
        self.check_login(data["login"])

        user = UserModel(**data)
        return user

    def check_email_validity(self, email: str):
        user = UserModel.get_by_email(db=self.db, email=email)
        if user:
            logger.warning(f"In {self.__class__.__name__}. "
                           f"Can't register user. "
                           f"User with email: {email} already exists")

            raise InvalidRequestData(ErrorCode.EMAIL_ALREADY_EXISTS,
                                     message=f"User with email "
                                     f"{email} already exists")
        if '@' not in email:
            logger.warning(f"In {self.__class__.__name__}. "
                           f"Can't register user. Invalid email: {email}")

            raise InvalidRequestData(ErrorCode.INVALID_EMAIL,
                                     message="Incorrect email address")

    def check_login(self, login):
        user = UserModel.get_by_login(self.db, login)
        if user:
            logger.warning(f"Can't register user. "
                           f"User with login: {login} already exists")

            raise InvalidRequestData(ErrorCode.LOGIN_ALREADY_EXISTS,
                                     message=f"User with login "
                                     f"{login} already exists")
