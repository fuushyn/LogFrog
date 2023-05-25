import datetime
from threading import Lock
from threading import Thread 
from queue import Queue 
import time 

class PyLog:
    def __init__(self, filename= "logs.txt"):
        self.filename = filename
        self.lock = Lock()
        self.log_queue = Queue()
        self.thread = Thread(target=self._background_logger)
        self.thread.start()

    #background logger for async logging
    def _background_logger(self):
        while(True):
            time.sleep(1)

            item = self.log_queue.get()
            print(item)
            if(item is None):
                break
            
            print(item)

            if(self.log_queue.empty()):
                continue
            log_level, message, timestamp = item
            print(item)
            with open(self.filename, 'a+') as log_file:
                print(f"{timestamp} '{log_level}' '{message}'\n")
                log_file.write(f"{timestamp} '{log_level}' '{message}'\n")

    def stop(self):
        self.log_queue.put(None)
        self.thread.join()
        
    def write_log(self, message, log_level ="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("pushing to queue")
        self.log_queue.put((log_level, message, timestamp), block=False)
        # self.log_queue.join()

    def info(self, message):
        self.write_log("INFO", message)

    def debug(self, message):
        self.write_log("DEBUG", message)

    def warning(self, message):
        self.write_log("WARNING", message)

    def error(self, message):
        self.write_log("ERROR", message)

    def critical(self, message):
        self.write_log("CRITICAL", message)

    def log_function(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.write_log("FUNCTION LOG", f"{func.__name__} {args} {kwargs} returned {result}")
            return result
        return wrapper

