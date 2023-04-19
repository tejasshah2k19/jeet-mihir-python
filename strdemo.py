#email-admin@gmail.com password:admin -> correct - > otherwise not 


#in password you can only input alphabets a-zA-Z

def authenticate(email,password):
    if password.isalpha() == False : #isdigit() isalnum() 
        print("Invalid Password Format")
        return;
    if(email.lower().endswith("@gmail.com")):
        print("Invalid Email Format")
        return;

    if(email.lower() == "admin@gmail.com" and password == "admin"):
        print("Correct Credentials")
    else:
        print("Invalid Credentials")
    


e = input("Enter Email")#"  admin@gmail.com "
p = input("Enter Password")
authenticate(e.strip(),p) #strip > remove space from string from beg--end
#lstrip() left 
#rstrip() right 

#string immutable 
data ="@@@@hi####"
print(data.lstrip("@"))
print(data.rstrip("####"))

print(data) # @@@@hi####

data = "royal"

data= "jony jony yes papa"

str = "value"
if str in data:
    print(str," found")


if str not in data:
    print(str," not found")


print(data[0])
print(data[0:7])
print(data[-1])
print(data[::])
print(data[::2])
print(data[::-1])





""" 
    string-> 
    1) jony jony yes papa
       JonY JonY YeS PapA 
    2) palindrome
    3)    

""" 


''' 
    multiline comment 
'''





































