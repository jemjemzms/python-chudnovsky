
"""
A Python script that will calculate the value of Pi to a set number of decimal places. 
"""

from decimal import Decimal, getcontext
import math as m
import time as t
import colorama
from colorama import Fore as f
colorama.init()

numberofdigits = int(input("Please enter the number of decimal places to calculate Pi to:"))
getcontext().prec = numberofdigits

start_time = t.time()
def calc(n): 
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):
        t = (Decimal(-1)**k)*(m.factorial(Decimal(6)*k))*(13591409 + 545140134*k)
        deno = m.factorial(3*k)*(m.factorial(k)**Decimal(3))*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return str(pi)

# run the calculation
print(calc(1))
print(f.RED + "\nTime taken:", t.time() - start_time)
    
