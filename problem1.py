##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
username = ""
password = ""
max_guesses = 3

while max_guesses > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "12345":
        print("Access granted")
        break
    else:
        print("Access denied")
        max_guesses -= 1
        if max_guesses == 0:
            print("Too many failed atempts. Access denied.")

