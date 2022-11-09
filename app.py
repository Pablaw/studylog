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

   log_all = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > g:nth-child(53) > rect:nth-last-child(1)')

   month3 = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(62)')
   month2 = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(63)')
   month1 = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(64)')
   month0 = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(65)')



   today = log_all['data-date']
   work = log_all['data-level']
   d_3month =  month3.text
   d_2month = month2.text
   d_1month = month1.text
   d_0month = month0.text

   print(log_all, d_0month, d_1month, d_2month, d_3month)
   return jsonify({'gitToday': [today, work], 'gitGrass': [d_0month, d_1month, d_2month, d_3month]})



if __name__ == '__main__':
   app.run('0.0.0.0',port=7778,debug=True)

