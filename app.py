from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
api = Api(app)
CORS(app)

class Summarization(Resource):
    def post(self):
        text = request.form['text']
        classifier = pipeline('summarization')
        result = classifier(text)
        return {'result': result}

api.add_resource(Summarization, '/')

if __name__ == '__main__':
    app.run(debug=True)