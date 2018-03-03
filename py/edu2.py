
import requests

response = requests.get('https://httpbin.org/get')
print(response.content)
print("-------------------json")
print(response.json())
print("-------------------headers")
print(response.headers)
print("------------------.get('Server'")
print(response.headers.get('Server'))
print(response.json().get('headers').get('Host'))
print("-------------------")



"""
 print("---------------NEXT_auth")
response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))

print(response.content)
print("-------------------json")
print(response.json())
print("-------------------headers")
print(response.headers)
print("------------------.get('Server'")
print(response.headers.get('Server'))
print("-------------------")
"""
print("------------------MAILRU")
r = requests.get('https://e.mail.ru/messages/')
print(r.headers)
#print(r.text)