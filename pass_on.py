from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
import requests
import json

connection = "http://34.227.115.205:5000/"

app = Flask(__name__, static_url_path="")
api = Api(app)

task_fields = {
    'id' : fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean
}

class HealthCheck(Resource):
    def get(self):
        return 200

class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        con = requests.get(connection+"tasks").json()
        return jsonify(con)
    
    # def post(self):
    #     args = self.reqparse.parse_args()
    #     task = {
    #         'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
    #         'title': args['title'],
    #         'description': args['description'],
    #         'done': False
    #     }
    #     tasks.append(task)
    #     return {'task': marshal(task, task_fields)}, 201

api.add_resource(TaskListAPI, '/tasks', endpoint='tasks')
api.add_resource(HealthCheck, '/healthcheck/', endpoint='healthcheck')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


