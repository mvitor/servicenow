$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f "youruser@yourcompany.com", "Y#urPwd1234")))
$headers.Add("Authorization", "Basic $base64AuthInfo")
$headers.Add("Content-Type", "application/json")

$body = @"
{
	"sysparm_action": "insert",
	"category": "Software",
	"impact": "1",
	"urgency": "2",
	"short_description": "Automated ticket Short Description",
	"description": "Automated ticket Description",
	"cmdb_ci": "Email",
	"caller_id": "Arnold Schwarzenegger",
	"contact_type": "Email",
	"company_name": "CompanyName"
}
"@

$response = Invoke-RestMethod 'https://myservicenowinstance.service-now.com/incident.do?JSONv2' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json