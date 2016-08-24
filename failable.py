from requests.exceptions import HTTPError, ConnectionError, Timeout

import praw

def avoid_fail(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except praw.errors.APIException:
            logging.warning("Reddit API call failed: " + traceback.format_exc())
            return None
        except ConnectionError:
            logging.warning("Connection error: " + traceback.format_exc())
        except HTTPError:
            logging.warning("HTTP error: " + traceback.format_exc())
        except Timeout:
            logging.warning("Connection timed out: " + traceback.format_exc())
    return wrapper
