from flask import Flask, request, jsonify, send_file
from threading import Thread
import json
import os

app = Flask('')

DATA_FILE = "data.json"


@app.route('/')
def home():
    return send_file("index.html")



def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()

# Function to write data to the file
def update_file(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)  # Write JSON with indentation
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


# API endpoint to receive JSON and update file
@app.route('/update', methods=['POST'])
def update_data():
    if not request.is_json:
        return jsonify({"error": "Request must contain JSON"}), 400

    data = request.get_json()  # Extract JSON data from request

    success = update_file(data)  # Write data to file

    if success:
        return jsonify({
            "message": "File updated successfully",
            "data": data
        }), 200
    else:
        return jsonify({"error": "Failed to update file"}), 500


# Endpoint to read the current file contents
@app.route('/data', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "File does not exist"}), 404

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return jsonify({"data": data}), 200
    except Exception as e:
        print(f"Error reading file: {e}")
        return jsonify({"error": "Failed to read file"}), 500
    

@app.route('/dance')
def dance():
    return send_file("dance.html")




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
