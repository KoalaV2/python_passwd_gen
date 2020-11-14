#!/usr/bin/env python3
import argparse
import string 
from random import * 

#passwd_length = int(input("How many characters do you want the password to be? \n :"))
#char = string.ascii_letters + string.punctuation  + string.digits
#passwd= "".join(choice(char) for x in range(randint(passwd_length,passwd_length)))
#print(passwd)


parser = argparse.ArgumentParser(description='Generates password depending on arguments')
parser.add_argument('--length', metavar='length', type=int,help='How long you want the password to be')

args = parser.parse_args()
print(args.length)

char = string.ascii_letters
passwd = "".join(choice(char) for x  in range(randint(args.length,args.length)))
print(passwd)
