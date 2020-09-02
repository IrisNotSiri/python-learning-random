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

 # regular expression
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
