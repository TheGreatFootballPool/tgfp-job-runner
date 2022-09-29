import time
import schedule
from scripts import jobs


def main():
    jobs.load()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
