from core.utils.result import result
from core.abstract_result.invalid import InvalidRequestData
from core.abstract_result.codes import ErrorCode
from core.abstract_result.result import AbstractHTTPResult
from betronic.base.resource import BaseResource


class ResourceForTesting(BaseResource):
    def __init__(self):
        super().__init__()
        self.r_parser.add_argument('test', type=str, required=True,
                                   location='json')

    @result
    def post(self):
        self.args = self.r_parser.parse_args()
        assert self.args
        args_dict = dict(self.args)
        if args_dict["test"] == 'invalid_data':
            raise InvalidRequestData(status_code=ErrorCode.PROGRAMMING_ERROR,
                                     message='FAIL')
        return AbstractHTTPResult(data={"requestData": args_dict}, msg='OK')
