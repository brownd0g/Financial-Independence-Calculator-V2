'''

Assignment 3

Andrew Brown

'''

import random

# This function is used to make sure user inputs a valid number for each question

def validInput(question, num_type): 
    """ This function takes user input and tests whether it is in an appropriate range to be tested

    The parameters are the question you want to ask the user and the return type
    "i" for positive integer, "r" for any real number
    If the input fails any of the tests, the user will be prompted to enter again until the input satisfies


    """
    user_input = input(question)

    if num_type == 'i': # This will run until a positive integer is entered
        while True:
            try:
                num = int(user_input)
                while num < 0:
                    num = int(input("Error: Please enter a positive integer: "))          
            
            except ValueError:                                                      
                user_input = input("Error: Please enter a positive integer: ")
                continue

            else:
                return num
                break

    elif num_type == 'r': # This will run until a real number is entered
        while True:
            try:
                num = float(user_input)         
            
            except ValueError:                                                      
                user_input = input("Error: Please enter a real number: ")
                continue

            else:
                return num
                break


def modify_rate(rate, change):

    return rate + change * (1 - random.random() * 2)
    

def run_simulation(annual_spend, inflation_rate, savings_balance, interest_rate, num_years, inflation_change, interest_change):

    """ This function runs the first partmonte carlo experiment taking in all the users input and calculating the balance with a
    random change rate for both inflation and interest for each year.

    The user enters the maximum they want the rate to change and a random number generator produces a new number for each year.
    """
    
    int_list = []
    
    for x in range(0, num_years): 

        annual_spend = annual_spend + (annual_spend * inflation_rate)                                    
        savings_balance = savings_balance - annual_spend                                                 
        savings_balance = savings_balance + (savings_balance * interest_rate)
        int_list.append (format(savings_balance, '0.2f'))

        output_file.write("{0: .2f}".format(savings_balance)) # writes to the file

        inflation_rate = modify_rate(inflation_rate, inflation_change) 
        interest_rate = modify_rate(interest_rate, interest_change)

    if float(int_list[num_years - 1]) > 0:
        output_file.write(" Successful!\n")
                        
    elif float((int_list[num_years - 1])) <= 0:
        output_file.write(" Unsuccessful\n")
        
    return float(int_list[num_years - 1])


expenses = validInput("How much did you spend last year to support your current lifestyle? ", 'i')   
inf_rate = validInput("Please enter the expected inflation rate: ", 'r')
inflation_change = validInput("Please enter the maximum amount the inflation rate can change in a single year: ", 'r')
savings = validInput("How much do you currently have saved for investment? ", 'i')
interest = validInput("What is the expected average annual interest rate? ", 'r')
interest_change = validInput("What is the maximum amount the interest rate can change in a single year: ", 'r')
test_years = (validInput("How many years do you want to test? ", 'i'))
simulations = (validInput("How many simulations do you want to run? ", 'i'))

print("calculating...")


success_counter = 0

output_file = open('output.txt', 'w') # opening a text file in write mode

for x in range(0, simulations): # this is the second part of the monte carlo experiment running x amount of simulations.
    if(run_simulation(expenses, inf_rate, savings, interest, test_years, inflation_change, interest_change) > 0):
        success_counter = success_counter + 1

output_file.close() # closing text file


print("Your simulation returned", success_counter, "successful attempts")
print("Success rate = " + format(success_counter/simulations * 100, '0.1f') + "%")
    



