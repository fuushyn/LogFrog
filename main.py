import datetime
from threading import Lock

class PyLog:
    def __init__(self, filename= "logs.txt"):
        self.filename = filename
        self.lock = Lock()

    def write_log(self, message, log_level ="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.lock:
            with open(self.filename, 'a+') as log_file:
                log_file.write(f"{timestamp} '{log_level}' '{message}'\n")


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
            self.write_log("FUNCTION LOG", f"{func.__name__} {args} {kwargs}")
            return func()
        return wrapper
