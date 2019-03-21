from logging import getLogger

from betronic.base.service import BaseService
from betronic.user.manager import UserManager

from core.abstract_result.result import AbstractHTTPResult

logger = getLogger(__name__)


class RegisterUser(BaseService):
    def get_result_handling(self):
        pass

    def post_result_handling(self):
        user_manager = UserManager(self.db)
        logger.info(f"Try to register user in {self.__class__.__name__} "
                    f"with args: {self.args}")
        user = user_manager.register_user(args=self.args)
        result_data = {
            "user_data": {
                "UserId": user.id,
            },
            "requestData": self.args
        }
        return AbstractHTTPResult(data=result_data, msg="Success")
