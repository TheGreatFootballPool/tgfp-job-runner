""" Schedule that will load and run whatever is included in 'jobs' """

import os
import logging
from rocketry import Rocketry


logging.basicConfig(level=logging.INFO)
logging.warning("New entry point")

app = Rocketry()
SCHEDULE = os.getenv('SCHEDULE')


@app.task(SCHEDULE)
def do_something():
    """ Doing something"""
    logging.info("BING")

if __name__ == '__main__':
    app.run()
