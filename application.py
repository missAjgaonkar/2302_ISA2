# app.py 
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hellow_world():
  return "Hellow, world!"
