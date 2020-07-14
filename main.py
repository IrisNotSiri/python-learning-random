
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


dnsVpnDict = {'port563': ["lanawarenodevpn.completelymanaged.com","563"],
                        'port443': ["lanawarenodevpn.completelymanaged.com","443"],
                        'port80': ["lanawarenodevpn.completelymanaged.com","80"]}

for key in dnsVpnDict:
  print (dnsVpnDict[key]) 

#execute command in linux using python code
#example 1: using nmap to check internet port status
def nmap(url, port):
    command = ['nmap', '-p', port, url]
    nmapResult = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    (stdout, stderr) = nmapResult.communicate()
    portOpen = False
    for line in stdout.split():
        if b"open" in line:
            portOpen = True
    return portOpen
#example 2: use code to exacute 
def systemctl(operation, service):
    command = ['systemctl',operation,service]
    err = subprocess.call(command)
    logger.info('vpn restart err {}'.format(err))
    return subprocess.call(command) ==0
operation = "start"
service = "scan.service"
startservice = systemctl(operation, service)


y = ['12','23','qwefasd']
if type(y) == list:
  print (type(y))

comment = None
noneValue = {"2qw":"wer1","wef":comment}
print (noneValue)

del y[1]