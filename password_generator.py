import random

lowercases = "abcdefghijklmnñopqrstuvwxyz"
upcases = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&/?¡"

use_for = lowercases + upcases + numbers + symbols

length_password = 8

password = "".join(random.sample(use_for, length_password))

print("Your password generated is: " + password)