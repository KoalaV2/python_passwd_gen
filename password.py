#!/usr/bin/env python3
import string 
from random import * 

char = string.ascii_letters
passwd= "".join(choice(char) for x in range(randint(5,5)))
print(passwd)
