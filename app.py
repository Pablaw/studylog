from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://pablaw:9dlrhd!357@cluster0.spvewgv.mongodb.net/?retryWrites=true&w=majority')
db = client.pablawsDB

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/githublog', methods=["GET"])
def getContributions():
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://github.com/Pablaw', headers=headers)

   soup = BeautifulSoup(data.text, 'html.parser')

   log_all = soup.select_one('body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > g:nth-child(53) > rect:last-child')
   today = log_all['data-date']
   work = log_all['data-level']

   return jsonify({'response': [today, work]})

if __name__ == '__main__':
   app.run('0.0.0.0',port=7778,debug=True)