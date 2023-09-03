"""

simple scheduler that runs any pending jobs loaded in `jobs.load()`

"""
import time
import schedule
from scripts import jobs


def main():
    """ The scheduler loop that runs the jobs """
    jobs.load()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
