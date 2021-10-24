from flask import Flask, jsonify, request
import requests
import json
# creating a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def is_user_eligible():

    if 'ip' in request.args:
        response = requests.get('http://ip-api.com/json/'+request.args["ip"])

    else:
        response = request.get('http://ip-api.com/json')


    if 'city' in request.args:

        result = json.loads(response.content.decode())
        if result['city'] == request.args['city']:
            return jsonify({'status': True,'message':'IP address is of allowed city'})
        else:
            return jsonify({'status': False,'message':'IP address is not allowed'})
    else:
        return jsonify({'status': False,'message':'No City passed in the URL'})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})


# driver function
if __name__ == '__main__':
    app.run(debug=True)
