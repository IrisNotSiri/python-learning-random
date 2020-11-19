cat = {}
result1 = {"mark": "1", "vlan": "2"}
result2 = {"mark2": "3", "vla2n": "1"}
cat.update(result1)
print(cat)
cat.update(result2)
print(cat)

cat["u"] = "o"
print(cat)

index = {1: "catalogue", 2: "fingerprint", 3: "vulnerability"}
print (index[1])

print(len(index.keys()))

JOB_OK = 1
JOB_FAIL = 2
def sendResult(data, jobStatus):
  print (jobStatus,JOB_OK)

sendResult(2,JOB_OK)  

hostset = {"a","b"}
hostset.update("c")
for host in hostset:
  print(host)

jobRequest = {"jobdata":"dump", "jobid":"1234","savetodb": {}}
jobRequest["savetodb"].update({"jobdata":"dunk"})

print(jobRequest)

hostlist = list(hostset)
#print(hostlist)

import re

url = "https://eft.lanaware.com/api"
re.findall('')
txt = url.split("/")
print(txt)
