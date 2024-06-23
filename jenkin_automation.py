import jenkins

host = "http://localhost:8080"
username = "kodewithdocker"
password = "11fb9e8494504a658f6d7fb602be6c20d5"
server = jenkins.Jenkins(host, username, password)
user = server.get_whoami()
version = server.get_version()
print(user)
print(version)
#print('Hello %s from jenkin %s' %(user['fullName'], version))




