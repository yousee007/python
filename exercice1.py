import datetime
from pickle import TRUE
import this

'''
Exercise
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

name = input("what is your name")

year = int(input("what is your years"))


now = datetime.datetime.now()
years = now.year


print(name + "your age is " + str((years - year + 100))  )
print()

sure =input("if you wanna stop then click 0")

while True:
    if sure =='0':
        break