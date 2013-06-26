from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated

import pymysql

# subscribers
@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    request.db = pymysql.connect(user=settings['db.user'], passwd=settings['db.password'], db=settings['db.db'], host=settings['db.host'])
    request.add_finished_callback(close_db_connection)

def close_db_connection(request):
	request.db.close()

