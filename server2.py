#start server uvicorn server2:app chmod +x run2.sh
from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save
app = FastAPI()

# http://localhost:8000/
@app.get('/')
def hello_world():
    #run other code here
    return {'hello': 'world'}


# http://localhost:8000/abc
@app.get('/abc')
def abc_view():
    #run other code here
    return {'data': [1,2,3]}


@app.post('/box-office-mojo-scraper')

def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {'data': [1,2,3]}

