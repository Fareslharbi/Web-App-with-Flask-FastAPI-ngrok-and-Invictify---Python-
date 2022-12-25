#start server gunicorn ./run2.sh   ngrok http 8000
from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save
app = Flask(__name__)

# http://localhost:8000/
@app.route('/', methods=['GET'])

def hello_world():
    #run other code here
    return 'Hello, world. this is Flask'


# http://localhost:8000/abc
@app.route('/abc', methods=['GET'])

def abc_view():
    #run other code here
    return 'Hello, world. this is Flask1'


@app.route('/box-office-mojo-scraper', methods=['POST'])

def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1,2,3, 'flask']}
