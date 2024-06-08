import requests as req
url = "https://httpbin.org/get"
t = req.get(url)
print(t.text)

with open("j1.json", "w") as file:
    file.write(t.text)



