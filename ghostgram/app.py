#!/usr/bin/env python3

# Ghostgram

import sys
import argparse
import getpass
from selenium.common.exceptions import *

from ghostgram.utils.ig_handler import IGWebdriverHandler
from ghostgram.utils.selaux import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--firefox', dest='browser', action='store_false', help='Use Firefox.')
    parser.add_argument('--chrome', dest='browser', default=True, action='store_true', help='Use Chrome.')
    parser.add_argument('--username', dest='username', help='Username for login.')
    parser.add_argument('--password', dest='password', help='Password for login.')   
    args = parser.parse_args()
    username = args.username
    password = args.password
    browser = args.browser
    if not username:
        username = input('Account username: ')
    if not password:
        password = getpass.getpass('Account password: ')
    if browser:
        driver = headless_chrome()
    else:
        driver = headless_firefox()
    ig_session = IGWebdriverHandler(driver)
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
        ig_session.select_mode()
        comments = ig_session.select_all()
        print('[i] Deleting comments...')
        ig_session.delete_comments()
    print('[i] No more comments found.')


if __name__ == '__main__':
    main()