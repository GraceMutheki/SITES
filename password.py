"""
#passwords format

import re
 
password = input("Password: ")

if matches:=re.search("^[A-Za-z0-9]+$", password):
    print(f"The password is format is correct")
else:
    print("Incorrect format")

with open("passwords.txt", "a") as file:
    file.write(password + "\n")

with open("passwords.txt", "r") as file:
    for line in file.readlines():
        print(line.rstrip())
"""

import random
import string
from cryptography.fernet import Fernet

lib =list(string.ascii_letters),list(string.digits)#initialize lists with lowercase alphabets
#lib =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",0,1,2,3,4,5,6,7,8,9]
"""
def write_key():
    key = Fernet.generate_key()
    file =open("passw.key","wb") #wb-write bytes
    file.write(key)
    file.close()
"""


def generate_passw():   
    password=[]
    i=5
    while(i!=0):
        letters=random.choice(lib)
        password.append(letters)
        res = ' '.join([str(s) for s in password])#converts each element in the list to a string
        i = i-1
        
    with open("passw.txt" , "a") as file:
            file.write(f"{res}\n")
        
def view_passw():
     with open("passw.txt", "r") as file:
        lines=file.readlines()
        for line in lines:
            clean_txt= " ".join(line.splitlines())#splits the string into a list of lines and then joins them back without newlines characters
            print(clean_txt)
     
def main():
    write_key()
    mode=input("Do you want to generate a new password or view the existing ones(generate/view.Press 'q' to exit: ").lower()
    if mode=="q":
        exit
    if mode=="generate":
        generate_passw()
    elif mode=="view":
        view_passw()
    else:
        print("Invalid input")

    
if __name__=="__main__":
    main()