import jenkins

host = "http://localhost:8080"
username = "kodewithdocker"
password = "11814e34ba7339c8379a164ba35ff65066"
server = jenkins.Jenkins(host, username, password)
user = server.get_whoami()
version = server.get_version()
print(user)
print('Hello %s from jenkin %s' %(user['fullName'], version))




