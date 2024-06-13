import http.client
import json

conn = http.client.HTTPSConnection("api.coinbase.com")
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", "api/v3/brokerage/time", payload, headers)
res = conn.getresponse()
print(res.getcode())
data = res.read()
print(data.decode("utf-8"))