from time import sleep

import praw

from failable import avoid_fail

@avoid_fail
def senpai_notice(reddit, subreddit_scan, comment_limit=25):
    """Scans comments in specified subreddit for key-phrase.
    Bot replies with specified response.'
    """
    subreddit = reddit.get_subreddit(subreddit_scan)
    match_comment = 'notice me senpai'

    print("\nRetrieving recent comments...")
    while True:
        # Iterates through comments of specified subreddit for comments.
        comment_list = subreddit.get_comments(limit=comment_limit)

        for comment in comment_list:
            comment_text = comment.body.lower()
            print(comment_text)
            cache = open(r'comment_cache.txt', 'r+')

            # If comment was already dealt with, ignore it and continue with loop.
            if comment.id in cache.read():
                print('Comment already handled...')
                cache.close()
                continue

            # If comment matches key-phase and comment is not handled, add to cache,
            # Upvote comment, and reply appropriately.
            if (match_comment in comment_text) and (comment.id not in cache.read()):
                cache.write(comment.id + '\n')

                # Catches RateLimitExceeded and sleeps to avoid error
                try:
                    comment.reply("Senpai has noticed you /u/{0} -Kōhai!".format(comment.author))
                except praw.errors.RateLimitExceeded:
                    print("Sleeping to avoid RateLimitExceeded...")
                    sleep(10)

                comment.upvote()

                print("Match found, replied...")
            else:
                print("Not a match...")

            # Closes cache, and sleeps thread to avoid RateLimitExceeded.
            cache.close()
            sleep(1)
