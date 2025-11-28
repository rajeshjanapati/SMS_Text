from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/send-sms", methods=["POST"])
def receive_sms():
    body = request.get_json()  # get full raw JSON body

    # Pretty-print the JSON data
    print("\n=== Full JSON Body Received ===")
    print(json.dumps(body, indent=4))
    print("================================\n")

    return jsonify({
        "message": "Full JSON received successfully",
        "data_received": body
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
