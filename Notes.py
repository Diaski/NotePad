from pathlib import Path
import os
from tracemalloc import stop
WhatDoing=input("Welcome to Notepad\nWhat are you doing? To log in press 'l' to register press 'r'")
if WhatDoing.lower()=="r":
    log=input("Login:")
    str_path= "Inser path there"+log+"/login.txt"
    path=os.path.join("Inser path there",log)
    try:
        os.mkdir(path)
    except FileExistsError:
        print ("Login in use!")
        quit()
    path=Path(str_path)
    login=open(path, 'a' )
    login.writelines(log)
    password1=input("password:")
    login.close()
    str_path= ""Inser path there""+log+"/Password.txt"
    path=Path(str_path)
    password=open(path, 'a' )
    password.writelines(password1)
    password.close()
elif WhatDoing.lower()=="l":
    index=0
    exist=0
    UserLogin=input("Login : ")
    str_path= "C:"Inser path there""+UserLogin+"/login.txt"
    path=Path(str_path)
    login=open(path, 'r')
    UserPasword=input("Password: ")
    for line in login:
        index+=1
        if UserLogin in line:
            exist+=1
            break
    login.close()
    str_path= ""Inser path there""+UserLogin+"/Password.txt"
    path=Path(str_path)
    password=open(path,'r')
    for line in password:
        index+=1
        if UserPasword:
            exist+=1
            break
    password.close()
    if exist==2:
        print("zalogowano")
        while True:
            str_path= ""Inser path there""+UserLogin+"/Blog.txt"  
            path=Path(str_path)  
            answer=input("What you wanna do? \n Write = 'w' or read = 'r' or 'c' to clear or quit 'q'")
            if answer == "w":
                Text=open(path, 'a')
                Text.write(input()+"\n")
            elif answer=="r":
                Text=open(path, 'r')
                print(Text.read())
            elif answer=="q":
                break
            elif answer=="c":
                open(path, 'w').close()
                
            else:
                print("wrong command!")
            Text.close()
        
    else:
        print("Wrong password or login")
