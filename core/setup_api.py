from betronic.user.resources.register import RegisterAPI
from tests.app.core.resource import ResourceForTesting

URL_PREFIX = "/api/v1.0"


def setup_api(api_instance):
    api_instance.add_resource(
        RegisterAPI, URL_PREFIX + "/user/register", endpoint="register"
    )
    api_instance.add_resource(
        ResourceForTesting, '/api/test', endpoint="test"
    )
