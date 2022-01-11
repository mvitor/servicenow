import json
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("youruser@yourcompany.com", "Y#urPwd1234")
uri = "https://myservicenowinstance.service-now.com/incident.do?JSONv2"

# define http headers for request
headers = {
    "Accept": "application/json;charset=utf-8",
    "Content-Type": "application/json"
}

# define payload for request, note we are passing the sysparm_action variable in the body of the request
# http://wiki.servicenow.com/index.php?title=JSONv2_Web_Service#insert
payload = {
    'sysparm_action': 'insert',
    'category': 'Infrastructure',
    'impact': '1',
    'urgency': '2',
    'short_description': 'Automated ticket Short Description',
    'description': 'Automated ticket Description',
    'cmdb_ci': 'Email',
	'caller_id': 'Arnold Schwarzenegger',
    'contact_type': 'Email',
    'company_name': 'CompanyName',
}

r = requests.post(url=uri, data=json.dumps(payload), auth=auth, verify=False, headers=headers)
content = r.json()
assert (r.status_code == 200)
print ("Response Status Code: " + str(r.status_code))
print ("Response JSON Content: " + str(content))