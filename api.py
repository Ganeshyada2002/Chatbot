from flask import Flask, request, jsonify
import simply

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("user_input", "")
    bot_response = simply.get_bot_response(user_input)
    response_data = {"bot_response": bot_response}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run()
