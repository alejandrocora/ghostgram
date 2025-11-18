import sys
import argparse
import getpass
from selenium.common.exceptions import *

from ghostgram.utils.ig_handler import IGWebDriverHandler
from ghostgram.utils.selaux import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--firefox', dest='browser', action='store_false', help='Use Firefox.')
    parser.add_argument('--chrome', dest='browser', default=True, action='store_true', help='Use Chrome.')
    parser.add_argument('--username', dest='username', help='Username for login.')
    parser.add_argument('--password', dest='password', help='Password for login.')
    parser.add_argument('--visual', dest='headless', default=True, action='store_false', help='Show browser UI.')
    args = parser.parse_args()
    username = args.username
    password = args.password
    browser = args.browser
    headless = args.headless
    if not username:
        username = input('Account username: ')
    if not password:
        password = getpass.getpass('Account password: ')
    if browser:
        driver = chrome(headless=headless)
    else:
        driver = firefox(headless=headless)
    ig_session = IGWebDriverHandler(driver)
    print('[i] Logging in...')
    try:
        ig_session.login(username, password)
    except TimeoutException:
        print('[!] Logging failed! Aborting.')
        sys.exit(1)
    print('[i] Successfully logged in.')
    ig_session.open_comments()
    comments = True
    while comments:
        ncomments = ig_session.select_comments()
        print('[i] Deleting comments...')
        ig_session.delete_comments()
        print('[+] Deleted ' + ncomments + ' comments.')
    print('[i] No more comments found.')


if __name__ == '__main__':
    main()