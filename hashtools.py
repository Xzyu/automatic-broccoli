from hasher import *
import itertools
from itertools import *

# bob = 60
test = hasher()
alphabets = [ 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
              'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
             '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']



def checks(ushash, thash):
    if ushash == thash:
        return True
    else:
        return False



def bruteForce():
    digits = int(input("How many characters are there?: "))
    keywords = list(product(alphabets, repeat=digits))
    thash = int(input("Enter other hash: "))
    vis = input("Do you want to show visuals? (yes/no): ")
    count = 0;
    for x in range(0,len(keywords)):
        temp = keywords[x]
        tempname = ""
        for x in range(0, len(temp)):
            tempname = tempname + temp[x]
        ushash = test.hashIt(tempname)
        ans = checks(ushash, thash)
        if vis.lower() == "yes":
            print ("Testing ", tempname, " ", ushash)
        if ans:
            print(tempname, " is a potential password with a hash of ", ushash, file=open("output.txt", "a"))
            print(tempname, " is a potential password with a hash of ", ushash, "Output.txt saved to current directory")
            count = count + 1
            break
    print("Done, ", count, " potential password found.", len(keywords), " combinations checked")

def creator():
    passw = input("Enter a password: ")
    ushash = test.hashIt(passw)
    print("Hash for ", passw, " is ", ushash)

def main():
    print("Welcome to Password tools")
    again = True
    while again:
        print("1. Password Hasher\n2. Password Brute Force\n3. Exit")
        try:
            userchoice = int(input())
        except Exception as e:
            print("Only numbers within the range")
        else:
            if userchoice == 1:
                creator()
            elif userchoice == 2:
                bruteForce()
            elif userchoice == 3:
                again = False


if __name__ == '__main__':
    main()

