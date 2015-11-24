#!/usr/bin/env python3
# PasswordGenerator2000

# randomly generated password
# 6 to 12 characters long
# only AbcBig AbcSmall and numbers
# no symbols
# input : password length, are you sure (till sucked)
# output : "to get a generated password please buy the advanced pack for 9.99$"

import os, random
import inspect

# List of allowed characters in the password
AbcSmall = "abcdefghijklmnopqrstuvxyz"
AbcBig = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "0123456789"
total = len(AbcSmall) + len(AbcBig) + len(numbers) - 1

version = "3.3.2"

print("You are running " + inspect.getfile(inspect.currentframe()) + " version: " + version) # script filename (usually with path)

Passwordlength = input ("How long should your password be?\n")

if Passwordlength.isdigit():
	Choice1 = input ("Are you sure that your password should be " + str(Passwordlength) + " long\n")
	if Choice1 != "yes" and Choice1 != "Yes":
		os._exit(0)

	Choice2 = input ("Are you really sure?\n")
	if Choice2 != "yes" and Choice2 != "Yes" :
		os._exit(0)

	Choice3 = input ("So we continue?\n")
	if Choice3 != "yes" and Choice3 != "Yes" :
		os._exit(0)

	Choice4 = input ("Just be sure, type 'Yes' one more time\n")
	if Choice4 != "yes" and Choice4 != "Yes" :
			os._exit(0)

	Choice5 = input ("Okay last time. Type 'Yes' to continue\n")
	if Choice5 != "yes" and Choice5 != "Yes" :
		os._exot(0)

	Choice6 = input ("Are you aware that you won't be able to go back after this?\n")
	if Choice6 != "yes" and Choice6 != "Yes" :
		os._exit(0)

	finishedPassword = ""

	for x in range(int(Passwordlength)):
		randomNumber = random.randint(0,total)
		finishedPassword += (AbcBig + AbcSmall + numbers)[randomNumber]

	print(finishedPassword)