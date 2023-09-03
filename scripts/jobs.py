"""
   Runs all the jobs,
   this is a placeholder and should be overwritten by mounting the scripts folder
"""

import logging
import schedule


def log_something():
    """ Sample method """
    logging.info("This is a method that says 'log something'")


def load():
    """ Loads the basic job"""
    logging.info("YO")
    schedule.every(5).seconds.do(log_something)
