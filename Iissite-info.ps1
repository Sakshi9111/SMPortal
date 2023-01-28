
#Set the file location for Csv and Json file

$PathCsv = "E:\Scripts\IIS-files\flow.csv"
$PathJson = "E:\Scripts\IIS-files\flow.json"

#Set the API End Point 

$Url = "http://192.168.2.101:7082/api/add/"

Get-IISSite | Select-Object Name,State,@{n='Bindings';e={$_.Bindings -Join ', '}} | 
Export-Csv $PathCsv -NoTypeInformation -Encoding utf8

Get-Content -Path $PathCsv | ConvertFrom-Csv -Delimiter ',' | ConvertTo-Json | Out-File $PathJson


$loss = Get-Content $PathJson

Invoke-RestMethod -Method Post  -Uri $Url  -Body $loss -ContentType "application/json; charset=utf-8" -Headers @{"Authorization" = "token 71d3c007361dd4036d3497a9441ea35ee4656a7d"}