import requests
import re
import json

pages = [
        'https://moodle.nu.edu.kz/course/view.php?id=8329',
        'https://moodle.nu.edu.kz/course/view.php?id=8323',
        'https://moodle.nu.edu.kz/course/view.php?id=7424',
        'https://moodle.nu.edu.kz/course/view.php?id=7181',
        'https://moodle.nu.edu.kz/course/view.php?id=7911',
        'https://moodle.nu.edu.kz/course/view.php?id=7871',
        'https://moodle.nu.edu.kz/course/view.php?id=7857',
        'https://moodle.nu.edu.kz/course/view.php?id=8107',
        ]

def login_to_moodle():
    username = ""
    password = ""
    url = "https://moodle.nu.edu.kz/login/index.php"
    session = requests.Session()
    payload = {
          'username': username,
          'password': password,
          'remeberusername': 0
          }
    session.post(url, data=payload, timeout=5)
    return session

def updateLastSeenTime(sess, page):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
        "Referer": "https://moodle.nu.edu.kz/my/",
        "Upgrade-Insecure-Requests": "1",
    }
    success = 0
    try:
        sess.get(page, headers=headers)
        success += 1
    except:
        print('[!] Timeout error. Failed for {}'.format(page))
    return success

def attendPages():
    try:
        sess = login_to_moodle()
        completed = 0
        for page in pages:
            completed += updateLastSeenTime(sess, page)
        print('[*] Success for {} courses out of {}'.format(completed, len(pages)))
    except:
        print('[!] Timeout error. Moodle is probably down.')

def main():
    attendPages()

if __name__ == "__main__":
    main()
