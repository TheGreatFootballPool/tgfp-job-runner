""" Schedule that will load and run whatever is included in 'jobs' """
import os
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

SCHEDULE = os.getenv('SCHEDULE')
TZ = 'US/Pacific'
DAY_OF_WEEK = 'thu'
GAME_START_TIME = '17:15'

h, m = GAME_START_TIME.split(':')
h: int = int(h)
m: int = int(m)
min_since_midnight = (h*60)+m

h, m = divmod(min_since_midnight-60, 60)
first_warn_trigger = CronTrigger(day_of_week=DAY_OF_WEEK, hour=h, minute=m)
h, m = divmod(min_since_midnight-30, 60)
second_warn_trigger = CronTrigger(day_of_week=DAY_OF_WEEK, hour=h, minute=m)
h, m = divmod(min_since_midnight-10, 60)
third_warn_trigger = CronTrigger(day_of_week=DAY_OF_WEEK, hour=h, minute=m)

all_triggers = OrTrigger([
    first_warn_trigger, second_warn_trigger, third_warn_trigger
])
logging.basicConfig(level=logging.INFO)

scheduler = BlockingScheduler()
scheduler.configure(timezone=TZ)


time_interval = IntervalTrigger(seconds=5)
day_of_week = CronTrigger(day_of_week='thu')


def do_something():
    """ Doing something"""
    logging.info("BING")


if __name__ == '__main__':
    scheduler.add_job(do_something, 'interval', seconds=5)
    scheduler.start()
