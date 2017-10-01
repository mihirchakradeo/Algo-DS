import thread
import random
from threading import Thread, current_thread
import time

a=[]


def main():
	n=input("Number of elements: ")
	for x in xrange(n):
		a.append(random.randint(0,10))
	print "Unsorted array"
	print a
	quicksort(a,0,n-1)
	print "Sorted array"
	print a

def partition(a,low,high):
	i=low-1
	j=low
	while j<high:
		if a[j]>=a[high]:
			j=j+1
		elif a[j]<a[high]:
			i=i+1
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
			j=j+1
	temp=a[i+1]
	a[i+1]=a[high]
	a[high]=temp
	return(i+1)

def quicksort(a,low,high):
	t1=None
	t2=None
	if low<high:
		j = partition(a,low,high)
		t1 = Thread(target=quicksort, args=(a,0,j-1))
		try:
			t1.start()
			print current_thread().name()+"started\n"
		except Exception as e1:
			pass

		
		#quicksort(a,0,j-1)
		t2 = Thread(target=quicksort, args=(a,j+1,high))
		try:
			t2.start()
			print current_thread().name+" started\n"
		except Exception as e2:
			pass
			
		if t1 is not None:
			try:
				print current_thread().name()+"joined\n"
				t1.join()
			except Exception as e3:
				pass
		if t2 is not None:
			try:
				print current_thread().name()+"joined\n"
				t2.join()
			except Exception as e4:
				pass
		#quicksort(a,j+1,high)

if __name__=="__main__":
	main()