# Author Yongdong Xi (Oct 12)

P = float(input("What is the the principal investment (the initial deposit amount)"))

r = (float(input("What is the the annual interest rate (as a decimal)")) / 100) 

n = 12

t = float(input("How many years is the money invested"))

A = P * ((1 + (r / n)) ** (n * t))

print(" the future value of the investment is", A)
