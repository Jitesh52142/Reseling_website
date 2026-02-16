from flask import Flask ,render_template , request
import requests



app = Flask(__name__)

@app.route("/")
def home():
    return "this my first page"






if __name__ == '__main__':
    app.run(debug=True)