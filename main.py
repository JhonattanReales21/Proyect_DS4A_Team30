from flask import Flask
from flask import jsonify
from flask import request
import json

def create_app():
    app = Flask(__name__)
    return app


app = create_app()

@app.route('/api/v1/suggest/', methods=['POST'])
def get_suggestion():
    form = json.loads(request.data)
    response = {'message': 'success {}'.format(form['name'])}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)