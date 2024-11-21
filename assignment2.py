# Loops.
#write a python that prints all even numbers between 1 and 20 using a for loop

def even_numbers():
    for even in range(1,21,2):
        print(even)
even_numbers()

#use a while loop to ask the user to input a number untill they provide a number greater than 10

while True:
    number = int(input("Enter a number: "))
    if number > 10:
        print("You entered a number greate than 10")
        break
    else:
        print("The number must be greater than 10. Try again.")
    
#write a programm that prints the multiplication table (from 1 to 10)for numbers  from 1 to 5 using nested for loops.

for m in range(1,6):
    print(m)
    for j in range(1,11):
        print(f"{m} * {j} = {m * j}")
        
#Given a list of integers,[4,7,2,9,12,15], write a program using a for loop to find the sum of all odd numbers and print the result


numbers = [4,7,2,9,12,15]
sum_of_odd_numbers = 0
for num in numbers:
    if num % 2 != 0:
        sum_of_odd_numbers+=num
print("sum of odd numbers:",sum_of_odd_numbers)

# Lists.
# #create a list of 5 fruits each fruit on a new line using a for loop

def fruit_lists():
    fruit_lists = ['apple', 'strawberry','banana','grapes','mango']
    for fruit in fruit_lists:
      print(f"{fruit} \n")
fruit_lists()
#write a function that takes a list of numbers and returns a new list with each number squared.example:[1,2,3] should become [1,4,9]

def square_numbers():
    return [number ** 2 for number in numbers]

numbers = [2, 4, 6, 8]
squared_numbers = square_numbers()
print(squared_numbers)

# #write a python program that takes two lists, list1 = [1,2,3] and list2 = [4,5,6]
# # and combines them into a single list, combined = [1,4,2,5,3,6].

list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

# #Given a list of numbers,[3,1,4,1,5,9,2], write a program to find and
# # print the two largest numbers in the list without using the max()function 

def two_largest():
    
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return largest, second_largest

numbers = [3, 1, 4, 1, 5, 9, 2]

largest, second_largest = two_largest()
print("The two largest numbers are:", largest, "and", second_largest")

# Dictionaries.
#Basic
# # #create a dictionary with three key-value pairs representing a student's information:name, 
# # # age and grade. print each key-value pair on a new line.

dict = {
    'name':'Patricia',
    'age':24,
    'grade':'A'
}
print(f"\nThe student name:{dict['name']}")
print(f"The student age :{dict['age']}")
print(f"The student grade :{dict['grade']}",'\n\n')

# # #write a function that takes a dictionary of people's names and their ages,
# # # {'Alice':24, 'Bob':19, 'Charlie':30}, and returns a list of names of people who are 21 or older.

dct = {'Alice':24, 'Bob':19, 'Charlie':30}
def adults():
    dict ={'Alice':24, 'Bob':19, 'Charlie':30}
    dict.pop('Bob')
    print(dict)
adults()

# #Given a dictionary representing items in a store with their prices,
# # {'apple':0.5, 'banana':0.3, 'orange':0.7},write a program that takes a list of items bought,
# # ['apple', 'orange', 'banana','banana'], and calculates the total cost.

dict = {'apple':0.5, 'banana':0.3, 'orange':0.7}
list = ['apple', 'orange', 'banana','banana']
total_cost = 0
for character in list:
    total_cost+=dict[character]
print(f"The total cost of items bought is:{total_cost}")
    

    
# # #write a program that counts the occurences of each word in a given sentence.
# # # Example: for the sentence "hello world hello" the output sould be{'hello':2, 'world':1}

def count_word():
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word,  0) + 1
    return word_count
sentence = "hello world hello"
result = count_word()
print(result)

# OPP.
#Basic
#create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

class Car:
        def __init__(self, brand, color):#we defined the attributes asked for
          self.brand = brand 
          self.color = color 

my_car = Car(brand="Range Rover", color="Pink") 

print(f"Brand: {my_car.brand}") #these are the attributes identified
print(f"Color: {my_car.color}")

    
##intermediate
#Add a method called start-engine to the Car class that prints a message saying the negine of the car started.
# Create an instance of Car and call the method.

class Car:
    def __init__(self, brand, color):
        self.brand = brand 
        self.color = color 

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.color} car has started!")
        
my_car = Car(brand="Range Rover", color="Pink")

my_car.start_engine()


#Create a class called BankAccount with attributes account-number and balance.Add methods to:
#Deposit an ammouunt
#withdraw an amount (only if suffient balance exits).
#print the account balance.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number 
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > 0:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def print_balance(self):
        print(f"Account balance: {self.balance}")

account = BankAccount(account_number="123456789")

account.deposit(500)

account.withdraw(200)

account.print_balance()

    

#implement a class called Library that manages a collection of books. Each book has a title , author, and available status.
# The Library class should have methods to:
#Add a book to the library
#Remove a book from the library
#Check if a book is available by title
#Borrow a book (mark it as unvailable if it's not  availabe)
#Return a book (mark it as available again if it was borrowed)

class Library:
    class Book:
        def __init__(self, title, author, available_status=True):
            self.title = title 
            self.author = author  
            self.available = available_status 

        def __str__(self):
            return f"'{self.title}' by {self.author}, Available: {self.available}"

    def __init__(self):
        self.books = [] 

    def add_book(self, title, author):
    
        new_book = self.Book(title, author)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def remove_book(self, title):
    
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed: {book}")
                return
        print(f"Book with title '{title}' not found.")

    def is_available(self, title):
        
        for book in self.books:
            if book.title == title:
                return book.available
        print(f"Book with title '{title}' not found.")
        return False

    def borrow_book(self, title):
        
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You borrowed: {book}")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"You returned: {book}")
                    return
                else:
                    print(f"'{title}' was not borrowed.")
                    return
        print(f"Book with title '{title}' not found.")

    def print_books(self):

        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

library = Library()

library.add_book("2006", "Jenny Nimmo")
library.add_book("Tell me your Secret", "Sidney Sheldon")
library.add_book("Tonny And Josephin", "Whitney Josephin")
library.add_book("Animal Farm", "George Orwell")

library.print_books()

library.borrow_book("2006")

print("Is '2006' available?", library.is_available("2006"))

library.return_book("2006")

library.remove_book("To Kill a Mockingbird")

library.print_book()