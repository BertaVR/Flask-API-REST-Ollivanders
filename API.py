from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class WelcomeOllivanders(Resource):
    def get(self):
        return {'Hello' : 'Ollivanders'}

api.add_resource(WelcomeOllivanders, '/')

if __name__ == '__main__':
    app.run(debug=True)
