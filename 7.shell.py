import os
from re import X, sub
import sys
import subprocess
from multiprocessing import Process


def process1():
	global g
	f = open("Example.txt","r")
	g = f.readline()
	f.close()

	f = open('Example.txt', 'a')
	f.write(g)
	f.close
	

def process2():
	f = open('Example.txt', 'a')
	y = "Ronaldo " 
	f.write(y)
	f.close()

if __name__ == '__main__':

	while True:
		command = input("Cristiano$ ")
		if command == "7":
			Process1 = Process(target=process1)
			Process2 = Process(target=process2)

			Process1.start()
			Process2.start()

			Process1.join()
			Process2.join()
