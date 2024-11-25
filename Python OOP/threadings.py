# threads = a flow of execution, like a seperate order of instruction
#           Lightweight processes that can run concurrently within a single program.
#           GIL = (global interpreter lock) it allows only one thread to hold the control of the python interpreter
# Multithreading: Technique that allows multiple threads to run in parallel, enhancing performance for tasks.
#
# the args parameter is used to pass arguments to the target function

import threading
import time

def eat():
    time.sleep(3)   # 3 is in sec
    print("you ate breakfast")

def drink():
    time.sleep(4)
    print("you drink water")

def hw():
    time.sleep(5)
    print("you done hw")


x = threading.Thread(target=eat, args=())   # a thread , this thread is in charge of func eat
x.start()

y = threading.Thread(target=drink, args=())  #  the args parameter is an empty tuple (). This means that no arguments will be passed to the "drink" function when the thread is started.
y.start()

z = threading.Thread(target=hw, args=())
z.start()

# threads synchronization

x.join()
y.join()
z.join()

# before using threading.Thread it took 12 sec to complete the task but 
# now its taking around 5 sec to complete whole cause all tasks are running parallel to each other
# and "threading.active_count()" and "threading.enumerate()" were called before the func because the main thread is not going to wait for these 3 threads to complete
# it has its own set of instruction to do, so it is no longer incharge of these 3 func
# the program is going to handle those three func to our three threads and our main threads is going to continue its own sets of instruction

#eat()
#drink()
#hw()

print("active count is: ",threading.active_count())
print("emumertate is ", threading.enumerate()) # prints a list of all currently active Thread objects in the program, including the main thread and any other threads that are currently running or not yet terminated.
print("perf counter is ",time.perf_counter())    #  prints the value of a high-resolution performance counter, which is useful for measuring time intervals with high accuracy.

