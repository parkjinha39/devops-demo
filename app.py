from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps test 이게 데브옵스다"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
