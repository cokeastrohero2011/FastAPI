from flask import Flask, request

data= []

app = Flask(__name__)

@app.route("/flask_health_check", methods = ["GET"])
def flask_health_check():
    return "Flask is running properly"

@app.route("/post_books", methods = ["POST"])
def post_books():
    source = request.json
    data.append(source)
    return "data successfully added", 201


app.run(port=8080,debug=True)