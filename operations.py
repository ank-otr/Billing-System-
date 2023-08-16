from read import *
from write import *




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
    


def options():
    loop = True
    while loop == True:
        userInput = (input("\t \t \t \t \t    Choose the operation you want to continue: "))
        if userInput == "1":
            rent_item()
            
        elif userInput == "2":
            return_item()
            break
        elif userInput == "3":
            exit_program()
            break
        else: 
            print("Enter valid input")
            
            
def rent_item():
        print("\n")
        print("\t \t \t \t \t           # You have Choosen Rent option.")
        name_of_user = input("\t \t \t \t \t    Enter your name: ")
        phone_num_of_user = input("\t \t \t \t \t    Enter your phone number: ")
        print("Thank you for your name "  + name_of_user.upper())
        print("Given below are the list of item can be rented. ")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("S.N. \t\t  Item Name     \t\t\t      Company Name  \t\t\t       Price \t\t\t             Quantity")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
        show_item()
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
        rent_validation()
        



def return_item():
    print("Thank you for returning")  
    


def exit_program():
    print("Thank you for using our system")  


def rent_validation():
    
    valid_id = int(input("Enter the id of the item you want to rent."))
    myDictionary = store_in_dictionary()
    
    while valid_id < 0 or valid_id > len(myDictionary):
       print("Enter correct or valid id") 
       valid_id = int(input("Enter the id of the item you want to rent."))
    
    quantity = int(input("Enter the quantity of the item you want to rent."))
    
    get_quantity_of_selected_item = myDictionary[valid_id][3]
    while quantity <= 0 or quantity > int(get_quantity_of_selected_item):
        print("The item's quantity you want to rent doesn't appears to available in the store.")
        print("\n")
        quantity = int(input("Enter the quantity of the item you want to rent."))
    print("\n")
    
    updated_quntity= int(get_quantity_of_selected_item) - int(quantity)
    myDictionary[valid_id][3] = str(updated_quntity)
    update_item_quantity(myDictionary)
