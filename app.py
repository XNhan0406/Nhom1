from flask import Flask

app = Flask(__name__)  # Chỉnh sửa đúng từ "name" → "__name__"

@app.route("/")
def hello():
    return "Hello from Azure!"
