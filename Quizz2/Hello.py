from flask import Flask, request, Response, jsonify

app = Flask(__name__)
global abc
abc={}

@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def post():
    abc['id'] = 1
    abc['name'] = request.form["name"]
    #name = request.form["name"]
    #line= ("Hello {}!".format(name))
    #return jsonify(line)
    return jsonify(abc),201

@app.route('/users/<id1>', methods=['GET'])
def get(id1):
    if abc['id']==int(id1):
        return jsonify(abc),200

@app.route('/users/<id1>', methods=['DELETE'])
def delete(id1):
    if abc['id']==int(id1):
        del abc['id']
        del abc['name']
        #abc.remove(abc[0])
        if abc=={}:
            return '',204
        return jsonify(abc)