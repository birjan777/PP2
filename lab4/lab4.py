#1. Python Iterators and Generators
#Task 1 — Generator for squares up to N
def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2

N = int(input("Enter number N: "))
for square in generate_squares(N):
    print(square)


#Task 2 — Even numbers between 0 and n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
print(",".join(str(i) for i in even_numbers(n)))


#Task 3 — Numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
for num in divisible_by_3_and_4(n):
    print(num)



#Task 4 — Generator squares(a, b)
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)



#Task 5 — Countdown generator (n → 0)
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))
for num in countdown(n):
    print(num)
#2. Python Date
#Task 1 — Subtract 5 days from current date
from datetime import date, timedelta

today = date.today()
new_date = today - timedelta(days=5)
print("Current Date:", today)
print("Date 5 days ago:", new_date)


#Task 2 — Yesterday, Today, Tomorrow
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#Task 3 — Drop microseconds
from datetime import datetime

now = datetime.now()
no_micro = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", no_micro)


#Task 4 — Difference between two dates in seconds
from datetime import datetime

date1 = datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime(2025, 10, 9, 14, 30, 0)
diff = (date2 - date1).total_seconds()
print("Difference in seconds:", diff)



#3. Python Math Library
#Task 1 — Convert degree to radian
import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))


#Task 2 — Area of a trapezoid
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = ((base1 + base2) / 2) * height
print("Area of trapezoid:", area)



#Task 3 — Area of regular polygon
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area, 2))


#Task 4 — Area of a parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Area of parallelogram:", area)

