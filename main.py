fibo=[0,1]
n=0
fibolist=[]
while n<=10:
  fibo.append(fibo[0]+fibo[1])
  n += 1
  del fibo[0]

print (fibo)

## using deque() to mimick real_life queue
from collections import deque
queue = deque()
print (queue)
# adding element to the right of the queue
queue.append('Kim')
queue.append('Jueng')
queue.append('May')
print (queue)
# removing element from the left of queue
queue.popleft()
print (queue)


## using deque() to mimick stack
stack = deque()
# adding element from left of stack
stack.appendleft("https://realpython.com/")
stack.appendleft("https://realpython.com/pandas-read-write-files/")
stack.appendleft("https://realpython.com/python-csv/")
print(stack)
# removing element from left
stack.popleft() 
print(stack)