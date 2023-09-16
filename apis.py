from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import uuid

app = Flask(__name__, "/static")
CORS(app)

port_number = 7001

#Reads the content of the json file and assigns to a variable
with open("./static/bookings.json") as my_file:
    jsonFile = my_file.read()
    data = json.loads(jsonFile)


# To allow headers/cors
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response

# GET method to retrieve all items
@app.route('/', methods=['GET'])
def get_items():
    return jsonify(data), 200

# GET method to retrieve a specific item by ID
@app.route('/<item_id>', methods=['GET'])
def get_item(item_id):
    print(item_id)
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return "Item not found", 404
    return jsonify(item)

# POST method to create a new item
@app.route('/add_room', methods=['POST'])
def create_item():
    new_item = request.json
    id = str(uuid.uuid4())
    new_item["id"] = id
    data.append(new_item)
    with open("./static/bookings.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    return jsonify(new_item), 201

# DELETE method to delete an item by ID
@app.route('/delete_room', methods=['DELETE'])
def delete_item():
    item_id = request.json
    print(item_id)
    for item in data:
        if item["id"] == item_id['ident']:
            data.remove(item)
    with open("./static/bookings.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    return jsonify({"message": "Item deleted"})

#Runs the server
if __name__ == '__main__':
    app.run(debug = True, port = port_number)