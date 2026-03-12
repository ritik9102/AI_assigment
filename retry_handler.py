import time

def retry(func, retries=3):

    for i in range(retries):

        try:

            return func()

        except:

            time.sleep(1)

    return None
