import requests as req

def test_get():
    resp=req.get("https://reqres.in/api/users?page=2/id=10")
    print(resp.json())
    status_code = resp.status_code
    print(status_code)
    assert status_code==200, "Wrong Response Code"

#print(resp)
#print(type(resp))
#print(dir(resp))
