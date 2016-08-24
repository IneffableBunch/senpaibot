import threading
from time import sleep

import praw

from events.notice import senpai_notice
import bot


# Logs into specified account
r = praw.Reddit(bot.USER_AGENT)
print("Logging in...")
r.login(bot.USERNAME, bot.PASSWORD, disable_warning=True)

noticer = threading.Thread(target=senpai_notice, args=(r, 'test'))

if __name__ == '__main__':
    noticer.start()