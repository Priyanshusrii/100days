import re
common= [
    "123456",
    "12345678",
    "123456789",
    "password",
    "password123",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "welcome123",
    "abc123",
    "iloveyou",
    "monkey",
    "dragon",
    "football",
    "master",
    "login",
    "passw0rd"

]

while True:
    count=0
    pas=input("Enter a password\n")
    if pas.lower() in common:
        print("VERY COMMON PASSWORD!!")
        break
    
    if len(pas)<8:
                print("enter 8 length minimum password!!")
                break
    else:
                count+=1
    regex = r"([A-Z]+)"
    match = re.search(regex,pas)
    if not match:
            print("PASSWORD SHOULD CONTAIN 1 UPPERCASE!!")
         
    else:
            count+=1
    res=r"([a-z]+)"
    match_small=re.search(res,pas)
    if not match_small:
            print("PASSWORD SHOULD CONTAIN 1 LOWERCASE!")
    else:
            count+=1
    res_num=r"([0-9]+)"
    match_num=re.search(res_num,pas)
    if not match_num:
                    print("PASSWORD SHOULD CONTAIN 1 NUMBER")
    else:
                    count+=1
    res_special=r"([!@#$%^&*()]+)"
    match_special=re.search(res_special,pas)
    if not match_special:
                    print("PASSWORD SHOULD CONTAIN 1 SPECIALCASE!")
    else:
                    count+=1

    if count==5:
            print("STRONG PASSWORD")
    elif 2<count<5:
            print("NORMAL PASSWORD")
    else:
            print("WEAK PASSWORD")

    r=input("wanna check again:")
    if r.lower()!="yes":
            print("exiting")
            break
    