from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://github.com/Pablaw', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

log1 = soup.select('body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > g:nth-child(53)')
log2 = soup.select('body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > g:nth-child(51)')

log_all = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > g:nth-child(53) > rect:nth-last-child(1)')
# today = log_all['data-date']
# work = log_all['data-level']

print(log_all);

# 1, 2~3, 4~5, 6