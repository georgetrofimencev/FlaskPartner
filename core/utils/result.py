from werkzeug.exceptions import BadRequest
from core.abstract_result.result import AbstractHTTPResult
from logging import getLogger
from core.abstract_result.codes import WEBCodes, ErrorCode
from core.abstract_result.invalid import InvalidRequestData

logger = getLogger(__name__)


def result(resource_method):
    def wrapper(self, *args, **kwargs):
        try:
            response = resource_method(self, *args, **kwargs)
        except Exception as e:
            logger.warning(
                f"Error in {resource_method.__class__.__name__}"
                f" with exception" f": {e}"
            )
            if isinstance(e, InvalidRequestData):
                response_data = {"error_code": e.status_code,
                                 "requestData": self.args}
                response = AbstractHTTPResult(
                    http_code=400,
                    data=response_data,
                    msg=f"{e.message}",
                    status=WEBCodes.NOT_OK,
                )
            elif isinstance(e, BadRequest):
                # TODO: Добиться возврата requestData при BadRequest Exception
                response_data = {
                    "error_code": ErrorCode.INCORRECT_REQUEST_DATA,
                    "requestData": self.args,
                }
                response = AbstractHTTPResult(
                    http_code=400,
                    data=response_data,
                    msg=f"{e}",
                    status=WEBCodes.NOT_OK)
            else:
                response_data = {
                    "error_code": ErrorCode.PROGRAMMING_ERROR,
                    "requestData": self.args,
                }
                response = AbstractHTTPResult(
                    http_code=500,
                    data=response_data,
                    msg=f"{e} in {self} ",
                    status=WEBCodes.NOT_OK
                )
        return response.result

    return wrapper
