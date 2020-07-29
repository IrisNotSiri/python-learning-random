with open('stdout.txt', 'r') as stdout:
  for line in stdout:
    splitedLine = line.split()
    #print (line)
    if splitedLine[1] == "Running":
      percentage = line.split()[2]
    elif splitedLine[1] == "Requested":
      percentage = "0%"
    elif splitedLine[1] == "Done":
      percentage = "100%"
    print (percentage)

print ("Job Finished")


list1 = [1,2,3,4]
list2 = [list1[0],list1[1]]
print (list2)
"""
import netifaces
w = netifaces.ifaddresses("eth0")
print ("w:"+str(w))
"""
import re
interfaces = ["eth0", "eth0.220", "eth0.230", "eth0.240"]
for interface in interfaces:
  x=re.findall("eth0", interface)
  print(x)
  if x:
    print (interface)