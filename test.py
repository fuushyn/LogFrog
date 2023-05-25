from main import PyLog
from threading import Thread 
import random
import time  

log = PyLog('logs.txt')

@log.log_function
def update_main():
    i =0
    while(i<20):
        i+=1
        r1 = random.randint(0, 100)
        with open("master.txt", 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            content = int(content)  + r1  
            log.write_log(str(r1))       
            f.write(str(content))
        time.sleep(1)

@log.log_function
def sync_copy():
    index = 0
    while(True):
        with open('logs.txt', 'r') as f:
            logs = f.readlines()
            loglen = len(logs)
            while(index<loglen):
                lognum = int(logs[index])
                with open('copy.txt', 'r+') as f_copy:
                    oldnum = int(f_copy.read().strip())
                    oldnum += lognum 
                    f_copy.seek(0)
                    f_copy.truncate()
                    f_copy.write(str(oldnum))
                    print(f"Updated copy to {oldnum}")
                index += 1
        time.sleep(1)

@log.log_function
def hello(str):
    print(str)
    return str


if __name__== "__main__":
    thread1 = Thread(target=update_main)
    thread1.start()
    thread1.join()
    # Thread(target=update_main).start()
    # Thread(target=sync_copy).start()
    log.stop()
