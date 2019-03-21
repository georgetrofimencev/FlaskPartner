import json
from flask import Response
from .codes import WEBCodes


class AbstractHTTPResult:
    def __init__(
        self, data: dict, msg: str,
            http_code: int = 200, status: int = WEBCodes.OK
    ):
        self.http_code = http_code
        self.data = data
        self.msg = msg
        self.status = status

    @property
    def result(self):
        result_data = {"status": self.status,
                       "data": self.data, "msg": self.msg}
        json_res = json.dumps(result_data)
        return Response(json_res, status=self.http_code,
                        mimetype="application/json")
