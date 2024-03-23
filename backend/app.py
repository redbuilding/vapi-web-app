# Copyright (c) [2024] [The Red Building Group LLC]
# This source code is licensed under the MIT License found in the
# LICENSE file in the root directory of this source tree.
#

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

VAPI_API_KEY = os.environ.get("VAPI_API_KEY")
VAPI_BASE_URL = os.environ.get("VAPI_BASE_URL")

@app.route('/create-assistant', methods=['POST'])
def create_assistant():
    assistant_data = request.json
    headers = {
        'Authorization': f'Bearer {VAPI_API_KEY}',
        'Content-Type': 'application/json',
    }
    response = requests.post(f"{VAPI_BASE_URL}/assistant", json=assistant_data, headers=headers)
    #print(response.text)

    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({"error": "Failed to create/update assistant"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
