
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/consult", methods=["POST"])
def consult():
    data = request.get_json()
    question = data.get("question", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما یک مشاور روشنایی هستید که بر اساس اطلاعات برندهایی مثل گلنور به مشتریان پاسخ می‌دهید."},
            {"role": "user", "content": question}
        ]
    )

    return jsonify({"answer": response["choices"][0]["message"]["content"]})
