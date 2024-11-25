# daemon threads = a thread that runs in the background, not impoertant for program to run
#                  your program will not wait for daemon threads to complete before exiting
#                  non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                  ex. baclground tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:", count, "seconds")

x = threading.Thread(target=timer)
x.setDaemon(True)  # Set the thread as a daemon before starting it
x.start()
print(x.isDaemon())  # This will print: True

answer = input("Do you wish to exit?")