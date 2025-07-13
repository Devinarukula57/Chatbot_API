from flask import Flask, request, jsonify, render_template
import cohere
import os
from dotenv import load_dotenv

load_dotenv()  # Load COHERE_API_KEY from .env file

app = Flask(__name__)

# ✅ Use your actual Cohere API key (from https://dashboard.cohere.com)
co = cohere.Client(os.getenv("COHERE_API_KEY"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        print(f"🟡 User message: {user_message}")  # debug log

        response = co.generate(
            model='command',
            prompt=user_message,
            max_tokens=100
        )

        bot_reply = response.generations[0].text.strip()
        print(f"🟢 Bot reply: {bot_reply}")  # debug log

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("🔴 FULL ERROR:", str(e))  # print full error to terminal
        return jsonify({"reply": f"Sorry, something went wrong.\n\n{str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
