from read import *
from write import *
from datetime import datetime

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

def user_info():
    print("\n")
   
    
    while True:
        try:
            name_of_user = input("\t \t \t \t \t    Enter your name: ")
            if not name_of_user.isalpha():
                raise ValueError("Name can only contain alphabetic characters.")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            phone_num_of_user = input("\t \t \t \t \t    Enter your phone number: ")
            if not phone_num_of_user.isdigit() or len(phone_num_of_user) != 10:
                raise ValueError("Phone number should be numeric and have 10 digits.")
            break
        except ValueError as e:
            print(e)
    
    print("Thank you for your Name and Phone Number " + name_of_user.upper())
    
    return name_of_user, phone_num_of_user

def print_item_list():
    rent_more_item = True
    while rent_more_item == True:
        print("Given below are the list of item can be rented. ")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("S.N. \t\t  Item Name     \t\t\t      Company Name  \t\t\t       Price \t\t\t             Quantity")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
        show_item()
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
        rent_more_item = False    

def rent_validation():
    myDictionary = store_in_dictionary()
    item_rented_by_user = []
   
    while True:
        valid_id = input("Enter the id of the item you want to rent (or 'exit' to finish): ")
            
        try:
            if valid_id.lower() == 'exit':
                print("\n")
                print("\t \t \t \t \t    #Enter you Name and Phone Number to Print your bill")
                break
            
            valid_id = int(valid_id)
            if valid_id < 0 or valid_id >= len(myDictionary):
                print("Enter a correct or valid id.")
                continue
            
            while True:
                try:
                    quantity = int(input("Enter the quantity of the item you want to rent: "))
                    get_quantity_of_selected_item = int(myDictionary[valid_id][3])

                    if quantity <= 0 or quantity > get_quantity_of_selected_item:
                        print("The item's quantity you want to rent doesn't appear to be available in the store.")
                    else:
                        break  # Exit the quantity input loop if valid
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    
            updated_quantity = int(get_quantity_of_selected_item) - int(quantity)
            myDictionary[valid_id][3] = str(updated_quantity)
            update_item_quantity(myDictionary)
            
            item_name = myDictionary[valid_id][0]
            user_selected_quantity = quantity
            item_price = myDictionary[valid_id][2]
            selected_item_price = item_price.replace("$", "")
            total_bill = int(selected_item_price) * int(quantity)

            item_rented_by_user.append([item_name, user_selected_quantity, item_price, total_bill])
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    today_date_and_time = datetime.now()
    name_of_user, phone_num_of_user = user_info()
    print("\n")
    print("\t \t \t \t \t \t  Welcome to Event Equipment Rental Shop")
    print("\t \t \t \t \t \t             Kathmandu, Nepal")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t             Customer Details")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name of the customer:", str(name_of_user).upper())
    print("Contact number:", str(phone_num_of_user))
    print("Date and time of renting:", str(today_date_and_time))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t             Items Details")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("Item Name \t\t\t\t\t  Total Quantity \t     Unit Price \t\t\t\t\tTotal")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    total = 0
    for i in item_rented_by_user:
        print(i[0], "\t\t\t", i[1], "\t\t\t", str(i[2]), "\t\t\t", "${}".format(i[3]))
        total += int(i[3])
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t            Grand Total: ${}".format(total))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("# Duration of Rented Item is for 5 Days.")
    print("Note: In case of Delay, you will be Fined.")  
    print("\n")
def return_item():
    print("Thank you for returning")  

def exit_program():
    print("Thank you for using our system")  

