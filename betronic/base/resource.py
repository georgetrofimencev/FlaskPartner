from flask_restful import Resource, reqparse


class BaseResource(Resource):
    def __init__(self):
        self.r_parser = reqparse.RequestParser()
        self.args = {}
