from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi Judy"

if __name__ == "__main__":
    app.run()