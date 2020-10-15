from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

response = http.get("https://en.wikipedia.org/w/api.php")

#dictionary
ip = 12
host = {ip: 12}
result = {}
result[ip] = {ip: host} 
print (result)
#iterate using range
for i in range(5):
  print (i)

#default argument in function
def orange(tree, static = False):
  if static:
    result = tree * 12

  return result

print (orange(12, True))

#numpy and hsv to rgb color
import colorsys
import numpy
for i in numpy.arange(0.0,1.0, 0.1):
  #print("+++"+str(i))
  r, g, b = colorsys.hsv_to_rgb(0.1, 1.0, 1.0)
  R, G, B = str(255 * r), str(255 * g), str(255 * b)
  RAINBOW_RGB = "^"+R+"*"+G+"*"+B+"*"  
  print(RAINBOW_RGB)


lilili = {}
vlan = "as"
host = ['1','we','sdf']
lilili.update({vlan:host})
vlan2 = "asdfzxdf"
lilili.update({vlan2:host})
print(lilili)

set1 = {"tree","grass","sky"}
list1 = list(set1)
print (set1, list1)

lists = list()
dicts = dict()
lists.append("wer")
dicts.update({"iosdf":"uo"})
print(lists, dicts)

result = {'host':{}}
if result['host']:
  print("1")
else:
  print ("2")

if 'we' in host:
  print('yes')

list1 = [1,2,3,4]
list2= [2,4,0,1,5]
for num in list1:
  if num not in list2:
    print(num)


import re

from datetime import datetime

# datetime object containing current date and time
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
# dd/mm/YY H:M:S
#dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
print("date and time =", now)

expire = [('2', '2020/10/03', '20:50:06'), ('2', '2020/10/06', '20:53:15')]
for value in expire:
  timeDate = value[1]+value[2]
  if timeDate < now:
    print ("expired")
  else:
    print ("valid")
expired = False if (timeDate < now) else True

y = ('df', '-h', '/dev/' + '/root')
print (y)

try:
  fastestInterface
except NameError:
  interface = "eth0"
else:
  interface = 'name' 
print (interface)

try:
    thevariable
except NameError:
    print("well, it WASN'T defined after all!")
else:
    print("sure, it was defined.")


devicelist = ['/dev/ttyS1', '/dev/ttyS0', '/dev/ttyUSB0']
if "usb*" in devicelist:
  print(1)
