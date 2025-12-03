# 1. Класс со строкой
class MyString:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Введите строку: ")

    def printString(self):
        print(self.text.upper())


# 2. Shape и Square
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# 3. Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# 4. Point
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# 5. Bank Account
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
        else:
            print("Not enough money!")


# 6. Filter prime numbers
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 11]
prime_nums = list(filter(lambda x: is_prime(x), nums))
print("Primes:", prime_nums)


# 7. Grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams


# 8. Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)


# 9. Chickens and rabbits
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits


# 10. Filter primes from list
def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]


# 11. All permutations of a string
import itertools
def all_permutations(s):
    return list(itertools.permutations(s))


# 12. Reverse words
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


# 13. Has 33
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False


# 14. Spy game
def spy_game(nums):
    code = [0,0,7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


# 15. Volume of sphere
def sphere_volume(r):
    return (4/3) * math.pi * (r**3)


# 16. Unique list
def unique_list(lst):
    new_list = []
    for x in lst:
        if x not in new_list:
            new_list.append(x)
    return new_list


# 17. Palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# 18. Histogram
def histogram(lst):
    for n in lst:
        print("*" * n)


# 19. Guess the number game
import random
def guess_game():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


# 20. Movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_good_movie(movie):
    return movie["imdb"] > 5.5

def good_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(category):
    return [m for m in movies if m["category"] == category]

def average_imdb(movies):
    return sum(m["imdb"] for m in movies) / len(movies)

def average_imdb_by_category(category):
    cat_movies = movies_by_category(category)
    return average_imdb(cat_movies)