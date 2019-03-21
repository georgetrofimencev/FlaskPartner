from betronic.base.resource import BaseResource
from logging import getLogger
from betronic.user.services.register import RegisterUser

from core.utils.result import result
logger = getLogger(__name__)


class RegisterAPI(BaseResource):
    def __init__(self):
        super().__init__()
        self.r_parser.add_argument('email', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('login', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('phone', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('password', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('name', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('surname', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('currency', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('country', type=str, required=True,
                                   location='json')
        self.r_parser.add_argument('language', type=str, required=False,
                                   default='RUS', location='json')
        self.r_parser.add_argument('skype', type=str, required=False,
                                   location='json')

    @result
    def post(self):
        self.args = self.r_parser.parse_args()
        logger.info(f'Got request to {self.__class__.__name__} '
                    f'with payload data: {self.args}')
        service = RegisterUser(dict(self.args), self)
        result_data = service.post_result_handling()
        return result_data
