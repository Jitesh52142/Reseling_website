from flask import Flask , render_templet , request
import requests



app = (__name__)

@app.route("/")
def home():
    return "this my first page"



if __name__ == '__main__':
    app.run(debug=True)