# Timing the performance of python's list data structure
# Author: SmushBall
# Date: 13 Feb, 2016
# *************************

def test1():
	l = []
	for i in range(1000):
		l = l+[i]

def test2():
	l = []
	for i in range(1000):
		l.append(i)


def test3():
    l = [i for i in range(1000)]

def test4():
	l = list(range(1000))


# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer
# timeit is used to measure cross-platform time measurements
# It takes two arguements, the first param is the python stmnt that you want to time
# the second param is the stmnt that will run once to setup the test


"""
To use timeit you create a Timer object whose parameters are 
two Python statements. The first parameter is a Python statement
 that you want to time; the second parameter is a statement 
 that will run once to set up the test. The timeit module 
 will then time how long it takes to execute the statement 
 some number of times. By default timeit will try to run the 
 statement one million times. When its done it returns the time 
 as a floating point value representing the total number of seconds.
 However, since it executes the statement a million times you can 
 read the result as the number of microseconds to execute the test
 one time. You can also pass timeit a named parameter called number 
 that allows you to specify how many times the test statement is 
 executed. 
""" 
t1 = Timer("test1()", "from __main__ import test1")
print("List by concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("List by append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("List by comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("List by list range ",t4.timeit(number=1000), "milliseconds")

