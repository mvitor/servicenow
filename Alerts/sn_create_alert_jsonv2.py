import requests
import json



url = "https://unisysmtdev.service-now.com/api/now/table/em_alert"



payload = json.dumps({
"source": "Nagios",
"node": "AZHYBWRKRW1",
"cmdb_ci": "e996db6b909c4bc9266e13961915",
"type": "bf094dbd349502d546ac2ca961993",
"severity": "3",
"description": "Service Restart",
"message_key": "Alert Ticket",
"additional_info": "vds"
})
headers = {
'Content-Type': 'application/json',
'Authorization': 'Basic ',
'Cookie': 'BIGipServerpool_unisysmtdev=578837002.44094.0000; JSESSIONID=34F99671CE3336114E454FC97B1A10BB; glide_session_store=EE20883CDB97C950B3F04641BA96197B; glide_user_route=glide.b5387b4c3f7e8d6de6b1724b4b9d9843'
}



response = requests.request("POST", url, headers=headers, data=payload)



print(response.text)