import threading
import time

x = 0
y = 0
s = threading.Lock()
b = 0


def x1():
    """
    	Prints multiple of x and y
    """
    global b
    while x < 20:
        s.acquire()
	if b != 0:
		b = 0
		print x, '*', y, '=', x*y
	s.release()

def x2():
    """
       It updates x and y in every onesecond
    """
    global b
    global x
    global y
    while x < 20:
	s.acquire()
	if b == 0:
		b = 1
		x += 1
		y -= 1
        s.release()

# Create two threads as follows
t1 = threading.Thread(target = x1)
t2 = threading.Thread(target = x2)

t1.start()
t2.start()
