from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
hint = "Don't forget to include the correct units! \nExiting..."
option = input("Enter C for Circle or T for Triangle: ").upper()

print("Calculator started...")
print('%s/%s/%s ' '%s:%s' % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)

if option == 'C':
  radius = float(input("Enter radius: "))
  area = pi * radius ** 2
  print("The pie is baking...")
  sleep(1)
  print("%.2f" % (area))

elif option == 'T':
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = base * height / 2
  print("Uni Bi Tri...") 
  print(hint)
  sleep(1)
  print("%.2f" % (area))
  
elif option == 'S':
  side = float(input("Enter side: "))
  area = side ** 2
  print("Deng...")
  sleep(1)
  print(f"the area of square is {area}a.")
  
elif option == 'TR':
  print("Your calculating the area of Trapezoid")
  sleep(1)
  base1 = float(input("Enter base: "))
  base2 = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = (base1 + base2) / 2 * height
  print("a few more sec...")
  sleep(1)
  print(f"the area of Trapezoid is {area}a.")
  
else:
  print("You entered garbage! Exiting...")
  sleep(3)
