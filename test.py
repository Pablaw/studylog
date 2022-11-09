from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://github.com/Pablaw', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

log_all = soup.select_one('body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > g:nth-child(53) > rect:nth-last-child(1)')

month1 = soup.select_one('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(62)')
month2 = soup.select('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(63)')
month3 = soup.select('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(64)')
month4 = soup.select('#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(65)')
print(month1, month2, month3, month4)

# today = log_all['data-date']
# work = log_all['data-level']

#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(62)
#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(65)
#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(65)

#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(54)
#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(65)
#user-profile-frame > div > div.mt-4.position-relative > div.js-yearly-contributions > div > div > div > svg > g > text:nth-child(64)