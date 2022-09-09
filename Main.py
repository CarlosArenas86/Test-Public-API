from crypt import methods
from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Succesfully loaded he home page', 'Timestamp':time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user', methods['GET'])
def request_page():
    user_query = str()

    #https://www.youtube.com/watch?v=5ZMpbdK0uqU&ab_channel=Indently 4:10min

    data_set = {'Page': 'Home', 'Message': 'Succesfully loaded he home page', 'Timestamp':time.time()}
    json_dump = json.dumps(data_set)

    return json_dump