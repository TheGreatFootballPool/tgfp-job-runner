""" Schedule that will load and run whatever is included in 'jobs' """
from time import sleep


def main():
    """ Simple main loop for purposes of deployment, should be overridden in production"""
    while True:
        print("looping")
        sleep(5)


if __name__ == '__main__':
    main()
