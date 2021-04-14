import re
strings = "This is a random string to check regex"
email = "my email is something123@gmail.com of google next is asian@gmail.com or A-s.ian_@gmail.com"
pattern = re.compile("a random string")
emailCheck = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

emailResult = emailCheck.findall(email)

result = pattern.findall(strings)
print(result)
print(emailResult)
