fibo=[0,1]
n=0
fibolist=[]
while n<=10:
  fibo.append(fibo[0]+fibo[1])
  n += 1
  del fibo[0]

print (fibo)