import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder='static')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": data['q']}]
    )
    return jsonify({"output": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)))
