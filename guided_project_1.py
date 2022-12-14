# -*- coding: utf-8 -*-
"""Guided_project_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bc1K2qJasBEX3dwdk6EMOizWD6DNhnew

# Chapter 1
### Your first day at your new job 👩‍💻👨‍💻

You are starting a new job as a junior software developer in an IT company. 

The company’s HR department asks you to fill out a form, so you start by assigning your personal information to corresponding variables.

📌 Create a variable for your name, surname, age, ID number, place of residence, to specify if you have active health insurance or not, and lastly one for specifying your nationality.
"""

#Please assign your personal information to variables
name = "Eylül"
surname = "Badem"
age = 19
id = 22003079
residance = "İzmir"
insurance = True
nationality = "Turkish"

"""###Meet And Greet
Introduce yourself to your new co-workers.

📌 Use a f-string to print "My name is Joey Tribbiani I am 25 years old and I live in London”.
"""

#Write a sentence using the print function to describe yourself using the variables above in the correct data type
print(f"My name is {name} {surname} I am {str(age)} years old and I live in {residance}.")

"""### Equipment starter pack
The HR department asks you to list the items you would need to improve your work efficiency

Mandatory:
* Laptop
* Headset
* Second monitor

Optional:
* Mousepad
* USB drive
* External drive


📌 Create a shopping list that contains items above and print it.
"""

#Create the item_list
itemList = ["Laptop","Headset","Second monitor","Mousepad","USB drive","External drive"]

#Print the list
print(itemList)

"""####What is mandatory and what is optional?

📌 Use list slicing to devide your list in two list: 'mandatory_item_list' and 'optional_item_list' and print both to the screen.
"""

#Use list slicing to divide the mandatory items
mandatory = itemList[0:3]

#Use list slicing to divide the optional items
optional = itemList[3:6]

#Print both to the screen
print(mandatory)
print(optional)

"""#### Go Shopping
Next, you will have to go and purchase these items, the finance department confirmed a budget of $5000.

📌 Assign 5000 to a variable called limit, so you know how much you can spend.
"""

#Assign the spending limit value to a variable called limit
limit = 5000

"""####Price dictionary

Before you start shopping yo need to find the best items that you can buy within the company budget. 

📌 Prepare a dictionary called “price_sheet” that includes the items as keys and the prices as values.  
 
"""

#Create a dictionary that contains each item and its price

priceSheet = {
    'Laptop' : 1500,
    'Headset' : 100,
    'Second monitor' : 200,
    'Mousepad' : 50,
    'USB drive' : 70,
    'External drive' : 250
}

"""####Shopping functions

You need to define three functions that will help you during shopping.

📌 First, create an empty list that  will be your shopping cart. Here you will add the items you need to purchase.

1. Define a function for both adding items to the cart and removing them from the item_list.

📌 The "add_to_cart" function should take the item name and the quantity to buy as an argument. 

2. Define a function that will create an invoice. 

📌 The "create_invoice" function should calculate the taxes of each item (18%) and add it to the total amount.

3. Define a function for the checkout. 

📌 The "checkout" function should subtract the total amount from the budget and print a statement to inform if the payment was successful. 
"""

#Initialize the cart list
cart = []

#Define the "add_to_cart" function
def add_to_cart (item,quantity) :
  cart.append((item,quantity))
  itemList.remove(item)

#Define the "create_invoice" function
def create_invoice ():
  totalTax = 0

  for item,quantity in cart :
    price = priceSheet[item]
    tax = price * 0.18 
    total = (tax + price) * quantity
    totalTax += total
    print( 'Item: ', item, '/t', 'Price: ', price, '/t', 'Quantity: ', quantity, '/t', 'Tax: ', tax, '/t', 'Total Price', total)

  print('The total amount you need to pay: ', totalTax)
  return totalTax

#Define the "checkout" function
def checkout ():
  global limit
  amount = create_invoice()

  if limit == 0:
    print('No money left')
  elif amount > limit:
    print('The amount you are trying to pay is above your limit')
  else:
    limit -= amount
    print( 'The total amount you have paid is {amount}, you have {limit} dollars left.' )

"""Let's shop!"""

#Call the "add_to_cart" function for each item
 
#Add first item to cart
add_to_cart('Laptop', 2)
 
#Add second item to cart
add_to_cart('Headset', 3)
 
#Add third item to cart
add_to_cart('Second monitor', 1)
 
#Add fourth item to cart
add_to_cart('Mousepad', 2)
 
#Add fifth item to cart
add_to_cart('USB drive', 2)
 
#Add last item to cart
add_to_cart('External drive', 1)
 
#Call the create "checkout" function to pay for all your items 
checkout()

"""###Game Night

You are back at the office and the HR department organizes a welcome party for new employees. 

You decide to create a Rock-Paper-Scissor game. 

📌 Create a Rock-Paper-Scissor game in which the user plays against the computer. The player will choose one of the actions, and the computer will choose its action randomly.

"""

#Import the random library
import random

#create a list containing the three actions of the game.
actions = ['rock', 'paper', 'scissor']

#Set the scores of players to 0
c_score = 0
p_score = 0

#Ask the user how many rounds they want to play
rounds = input('rounds? ')

#Add a round_counter that is 0 at the beginning
round_counter = 0

#Write a while loop and put the game inside
while round_counter < int(rounds) :

  #Increase round_counter by and print it
  round_counter += 1
  print(' -- round ', round_counter, '--')

  #Select a random action for computer
  c_move = random.choice(actions)

  #Ask player to choose an action
  p_move = input('your move? (rock, paper, scissor)')

  #Print the players choices
  print('computers move: ', c_move)
  print('your move: ', p_move)

  #tie condition
  if p_move == c_move:
    print('tie!')

  #Remaining conditions
  if (p_move == 'rock') & (c_move == 'scissor'):
    print('player took the point!')
    p_score += 1
  elif (p_move == 'scissor') & (c_move == 'paper'):
    print('player took the point!')
    p_score += 1
  elif (p_move == 'paper') & (c_move == 'rock'):
    print('player took the point!')
    p_score += 1
  elif (c_move == 'rock') & (p_move == 'scissor'):
    print('computer took the point!')
    c_score += 1
  elif (c_move == 'scissor') & (p_move == 'paper'):
    print('computer took the point!')
    c_score += 1
  elif (c_move == 'paper') & (p_move == 'rock'):
    print('computer took the point!')
    c_score += 1

  #Stop the while loop if the round_counter equals the number of total rounds
  


#Print the outcome of the game by using conditional statements
print('computers total score: ', c_score)
print('players total score: ', p_score)

if c_score > p_score:
  print('computer won :((')
elif p_score > c_score:
  print('you won!! :)')

"""# Your first task 

Rachel asks you to write a program to track the name and revenue each employee brings.  

* Create the "salesperson_revenue" dictionary to see the employee name as a key and the revenue as a value.

  📌 Every employee starts with 0 revenue.
* Define the "enter_revenue" function. 

  📌 The function takes the name and revenue as an argument and updates the salesperson_revenue dictionary.

"""

#Create salesperson_revenue dictionary
salesperson_revenue = {
    'Eylül' : 0,
    'Emir' : 0,
    'Ekin' : 0,
    'Engin' : 0,
    'Hülya' : 0
}

#Define enter_revenue function

def enter_revenue (name, revenue):
  global salesperson_revenue
  salesperson_revenue[name] += revenue

"""####Try out the functions
* In a while loop ask the user to give the name of the employee and for the revenue 

  📌 If the user enters “quit” the loop should break.

After that, print out the salesperson_revenue dictionary.

"""

#Asking user employee name as input
while True:
  name_answer = input('employee name: ')
  if name_answer == 'quit':
    break
  revenue_answer = int(input('revenue: '))
  enter_revenue(name_answer,revenue_answer)
  print(f"{name_answer}'s revenue is {salesperson_revenue[name_answer]}")

#Print the salesperson_revenue dictionary
print(salesperson_revenue)