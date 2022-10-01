import logging
import os
import schedule
import sentry_sdk

from .external import log_something
sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN_TGFP_BIN'),
    traces_sample_rate=1.0
)
logging.basicConfig(level=logging.INFO)
logging.warning("HELP")


def load():
    logging.info("YO")
    schedule.every(5).seconds.do(log_something)
