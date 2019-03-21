import unittest
import requests

from betronic import create_app, db
from core.abstract_result.codes import ErrorCode


class FlaskAPITestCase(unittest.TestCase):
    URL = "http://127.0.0.1:8888"

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_api_with_invalid_http_method(self):
        response = requests.get(self.URL + "/api/test")
        self.assertEqual(response.status_code, 405)

    def test_api_with_correct_data(self):
        data = {"test": "test"}
        response = requests.post(self.URL + "/api/test", json=data)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(data["status"], 0)
        self.assertEqual(data["msg"], "OK")
        self.assertEqual(data["data"]["requestData"], {'test': 'test'})

    def test_api_with_invalid_data(self):
        response = requests.post(self.URL + "/api/test",
                                 data={"invalid": "invalid"})
        self.assertEqual(response.reason, "BAD REQUEST")
        self.assertEqual(response.status_code, 400)

    def test_correct_request_data_in_response(self):
        response = requests.post(self.URL + "/api/test",
                                 json={"test": "test"})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["data"]['requestData'], {'test': 'test'})
        self.assertEqual(data["status"], 0)

    def test_incorrect_request_data_in_response(self):
        response = requests.post(self.URL + "/api/test",
                                 json={"invalid": "invalid"})
        data = response.json()
        self.assertEqual(response.reason, "BAD REQUEST")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["data"]['requestData'], {"invalid": "invalid"})
        self.assertEqual(data["status"], 1)

    def test_to_correctly_server_error_response(self):
        response = requests.post(self.URL + '/api/test',
                                 json={"test": "invalid_data"})
        data = response.json()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['data']['requestData'], {'test': 'invalid_data'})
        self.assertEqual(data['status'], 1)
        self.assertEqual(data['data']['error_code'],
                         ErrorCode.PROGRAMMING_ERROR)
        self.assertEqual(data['data']['message'], 'FAIL')


if __name__ == "__main__":
    unittest.main()
