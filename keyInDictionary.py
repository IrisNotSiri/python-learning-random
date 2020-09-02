
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
