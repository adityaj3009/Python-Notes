# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threads
#                   multiprocessing = better for cpu boubd tasks(heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)


# The output of cpu_count() (12 in your case) indicates how many parallel processes can potentially run concurrently on your system 
# without significant overhead from context switching. This number is based on the number of physical cores and logical processors (including hyper-threading) available on your CPU.

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())

    a = Process(target=counter, args=(9,))
    b = Process(target=counter, args=(1,))
    c = Process(target=counter, args=(50,))
    d = Process(target=counter, args=(40,))


    a.start()
    b.start()
    c.start()
    d.start()
  
    a.join()
    b.join()
    c.join()
    d.join()
    
    print(f" finishes in : { time.perf_counter()} seconds")

if __name__ == "__main__":
    main()