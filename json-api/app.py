from flask import Flask, url_for, redirect, Blueprint, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
test_api_bp=Blueprint(
    'test',
    __name__
)
test_api = Api(test_api_bp)
app.register_blueprint(test_api_bp)

@test_api.reource('/index')
class SomeApi(resource):
    def get(self):
        return 'Get Request'
    def post(self):
        return 'Post request'
