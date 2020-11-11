from flask import Flask
from flask import jsonify
from flask import request

def create_app():
    app = Flask(__name__)
    return app


app = create_app()

@app.route('/api/v1/suggest/', methods=['POST'])
def get_suggestion():
    response = {'message': 'success {}'.format(request.form['name'])}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)