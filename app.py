from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/base")
def base():
    return "<p>this is the home page</p>"
if __name__=="__main__":
   app.run(debug=True)