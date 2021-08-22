import time
class Clock:
    def wait(amount):
        time.sleep(amount)
    def current(type = None):
        result = time.time()
        return result
