#!/bin/python3

admin_email = "root@email.com"
admin_password = 12345

staff_email = "staff@email.com"
staff_password = 123

input_email = input("Type your email: ") 
input_password = int(input("Type your password: ")) 

if input_email == admin_email and input_password == admin_password:
    print("Admin logged!")
    pass
elif input_email == staff_email and input_password == staff_password:
    print("Staff logged!")
    pass
else:
    print("Invalid loggin!")
    
