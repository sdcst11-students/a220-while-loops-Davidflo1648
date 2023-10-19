#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
username = ""
password = ""
guess = True

while guess:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "12345":
        print("Access granted")
        guess = False
        break
    else:
        print("Access denied")