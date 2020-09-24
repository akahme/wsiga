from flask import Flask, request
from datetime import datetime
import re, sys

name = sys.argv[1]

app = Flask(__name__)
@app.route('/')
@app.route('/<path>')
def hello(path=''):
    html = open('index.html').read()
    html = re.sub('{{name}}', name, html)
    date = datetime.now()

    html = re.sub('{{date}}', date.strftime('%d/%m/%Y  %H:%M'), html)

    mounth = int(date.strftime('%m'))
    year = int(date.strftime('%Y'))
    subyear = 0

    if mounth > 6:
        subyear = 1
    ad = subyear
    for p in range(10,0,-1):
        subyear += 1
        html = re.sub('{{p' + str(p) + '}}', str(year-(5-int((ad + p)/2))) + '.' + str(subyear), html)
        subyear %= 2
    
    html = re.sub('{{admission}}', str(year-4) + '.1', html)


    return html



app.run(port=80)


