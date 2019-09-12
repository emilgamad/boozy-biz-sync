"""Library of functions that the api runs for each particular call"""
from flask import request, jsonify, Response
from flask_restful import Resource, reqparse
from flask_restful.utils import cors

parser = reqparse.RequestParser()

class Index(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        return "Boozy Biz Sync API"
