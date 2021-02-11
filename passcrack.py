from pyfiglet import Figlet
import hashlib
green = '\033[1;92m'
red = '\033[31m'
blue = '\033[34m'
purple = '\033[35m'
blackbackground = "\033[1;32;40m \n"
print(blackbackground + green+ blue + """

    ____  ______   __  _____   ________ _______    
   / __ \/_  __/  / / / /   | / ____/ //_/ ___/    
  / /_/ / / /    / /_/ / /| |/ /   / ,<  \__ \     
 / _, _/ / /    / __  / ___ / /___/ /| |___/ /     
/_/ |_| /_/    /_/ /_/_/  |_\____/_/ |_/____/  

""" + blue + green + blackbackground)

flag = 0

pass_hash = input("enter md5 hash : ")

wordlist = input("file name : ")

try:
    pass_file = open(wordlist, "r")
except:
    print("no file found")
    quit()
for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    # print(word)
    # print(digest)
    # print(pass_hash)

    if digest == pass_hash:
        print("password found: ")
        print("password is " + word)
        flag = 1
        break

if flag == 0:
    print("Sorry this password is not in this txt...so you try another txt files to get password")
print(purple + """



+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+ +-+-+-+-+-+                                    
|T|H|A|N|K|S| |F|O|R| |U|S|I|N|G| |T|H|I|S| |T|O|O|L| |C|O|D|E| |B|Y| |R|T| |H|A|C|K|S|                                    
+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+ +-+-+-+-+-+
""" + purple)
