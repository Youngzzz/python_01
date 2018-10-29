from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "陌上花开，可缓缓归矣～"
if __name__ == "__main__":
    app.run()
