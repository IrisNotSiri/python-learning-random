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

#try if key is in dictionary
job_request = {'lanawareId': 5, 'action': 'updateAssignment', 'partnerId': 2, 'partnerName': 'WHY', 'customerId': 2, 'customerName': 'Iris Working Lab', 'siteName': 'Fancy site'}
if 'timeZone' in job_request:
  print (1)
else:
  print(2)

#remove space between strings
hostname = ""
hostid = 2
name = "Siri Working Lab"
print (name.split())
for i in name.split():
  hostname = hostname+i
hostname += str(hostid)
print (hostname)
