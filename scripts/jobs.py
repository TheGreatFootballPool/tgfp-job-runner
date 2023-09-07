""" Schedule that will load and run whatever is included in 'jobs' """
import os
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

SCHEDULE = os.getenv('SCHEDULE')
TZ = os.getenv('TZ')

logging.basicConfig(level=logging.INFO)

scheduler = BlockingScheduler()
scheduler.configure(timezone=TZ)


def do_something():
    """ Doing something"""
    logging.info("BING")


if __name__ == '__main__':
    scheduler.add_job(do_something, 'interval', seconds=5)
    scheduler.start()
