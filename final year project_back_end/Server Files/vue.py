from flask import Flask
from flask import request, jsonify
from flask_cors import CORS  # 解决跨域问题
import string
import hashlib  # encrypt
import json
import pymysql  # interactive with mysql
import mysql
from mysql import is_number, check_number_exist, check_letter_exist, check_total
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_mail import Message, Mail
import random
import time


import random
import base64
from urllib.parse import quote
import requests
import os

app = Flask(__name__)  # 创建程序实例
cors = CORS(app)  # 解决跨域问题

@app.route("/")
def index():
    return '<h1>This is a internshiop project designed by Jacky.</h1>'

@app.route("/upload_data")
def upload_data():
    return 0





if __name__ == '__main__':
    app.run()

app.run(host="127.0.0.2", port=4444, debug=True)
