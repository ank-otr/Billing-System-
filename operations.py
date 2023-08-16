from read import *
from write import *
store_in_dictionary()
def welcome_message():
    print("\n")
    print("\t \t \t \t \t \t  Welcome to Event Equipment Rental Shop")
    print("\t \t \t \t \t \t             Kathmandu, Nepal")
    print("\n")
    print("\t \t \t \t            Choose a option your option you want to continue")
    print("\t \t \t \t \t \t          -> Press 1: Rent Items. ")
    print("\t \t \t \t \t \t          -> Press 2: Return Items. ")
    print("\t \t \t \t \t \t          -> Press 3: Exit.")
    print("\n")

def footer_component():
    print("\n")
    print("\t \t \t \t \t \t                Thank you.")
    print("\n")
    
def rent():
    loop = True
    while loop == True:
        userInput = (input("\t \t \t \t \t    Choose the operation you want to continue: "))
        if userInput == "1":
            print("\t \t \t \t \t    Thank you for Renting.")
            name_of_user = input("\t \t \t \t \t    Enter your name: ")
            phone_num_of_user = input("\t \t \t \t \t    Enter your phone number: ")
        bought_item_by_user = []
        want_more = True
        while want_more == True:
            print("Thank you for your name "  + name_of_user.upper())
            print("Given below are the list of item can be rented. ")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t\t  Item Name     \t\t\t      Company Name  \t\t\t       Price \t\t\t             Quantity")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
            show_item()
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
            break
