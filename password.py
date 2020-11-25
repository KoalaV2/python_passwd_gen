#!/usr/bin/env python3
import argparse
import string 
from random import  choice, randint

parser = argparse.ArgumentParser(description='Generates password depending on arguments')
parser.add_argument('-len','--length', metavar='length', type=int,help='How long you want the password to be')
parser.add_argument('-n','--numbers',  action='store_true', help="If you want numbers or not in the generated password")
parser.add_argument('-l','--letters', action='store_true', help="If you want letters or not in the generated password")
parser.add_argument('-c','--characters', action='store_true', help="If you want to add special characters like @ to the password")

args = parser.parse_args()
char = ""
if args.numbers:
    char += string.digits 
if args.letters:
    char += string.ascii_letters
if args.characters:
    char += string.punctuation

passwd = "".join(choice(char) for _  in range(randint(args.length,args.length)))
print(passwd)
