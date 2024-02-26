import flask
from flask import Flask, jsonify, request, make_response
import flask_cors


app = Flask(__name__, static_folder='static')
cors = flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
@flask_cors.cross_origin()
def helloserver():
    return f"<h1>Local server works fine!</h1>"

@app.route('/about/', methods=['GET'])
@flask_cors.cross_origin()
def aboutme():

    with  open("AboutMe.txt") as f:
        data = f.read()
    
    return f"<p>"+data+"</p>"

@app.route('/squareinput/', methods=['POST', 'OPTIONS'])
@flask_cors.cross_origin()
def square():

    if request.method == "OPTIONS":  # CORS preflight
        return build_cors_prelight_response()

    data = request.get_json()[0]
    num_list = data.values()

    response = {}
    response['results'] = []

    for n in num_list:
        num_square = n**2
        response['results'].append(num_square)

    return jsonify(response)


def build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

if __name__ == '__name__':
    app.run(debug=True)