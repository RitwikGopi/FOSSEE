import thread
import time

x = 0
y = 0
s = 0


def x1():
    """
    	Checks a status variable 's' which indicates 
	that x and y have updated. Once 's' is set function
	prints multiple of x and y
    """
    while True:
        if s == 1:
            print x, '*', y, '=', x*y
            time.sleep(.2)


def x2():
    """
       It updates x and y in every onesecond
    """
    while True:
        global x
        global y
        global s
        x += 1
        y -= 1
        s = 1
        time.sleep(.1)
        s = 0
        time.sleep(1)

# Create two threads as follows
thread.start_new_thread(x1, ())
thread.start_new_thread(x2, ())
while True:
    pass
