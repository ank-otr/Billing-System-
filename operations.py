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
            full_name = input("\t \t \t \t \t    Enter your full name: ")
            names = full_name.split()

            if len(names) < 2:
                raise ValueError("Please enter your full name in the format 'First [Middle] Last'.")

            if not all(name.isalpha() for name in names):
                raise ValueError("Names should only contain alphabetic characters.")
                        
            first_name = names[0]
            last_name = names[-1]
            middle_name = " ".join(names[1:-1])
            
            name_of_user = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
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
    print("\n")
    
    
    return name_of_user, phone_num_of_user

def print_item_list():
    rent_more_item = True
    while rent_more_item == True:
        print("\n")
        print("Given below are the list of item can be rented. ")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("S.N. \t\t  Item Name     \t\t\t      Company Name  \t\t\t       Price \t\t\t             Quantity")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
        show_item()
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
        rent_more_item = False    

def rent_item():
    myDictionary = store_in_dictionary()
    item_rented_by_user = []
    name_of_user, phone_num_of_user = user_info()
    print("Thank you for providing your information, " + name_of_user.title())
    print_item_list()
    while True:
        valid_id = input("Enter the id of the item you want to rent (or 'exit' to finish renting and print the bill): ")
            
        try:
            if valid_id.lower() == 'exit':
                print("\n")
                break
            
            valid_id = int(valid_id)
            if valid_id < 0 or valid_id > len(myDictionary):
                print("Enter a correct or valid id.")
                continue
            
            while True:
                try:
                    quantity = int(input("Enter the quantity of the item you want to rent: "))
                    get_quantity_of_selected_item = int(myDictionary[valid_id][3])

                    if quantity <= 0 or quantity > get_quantity_of_selected_item:
                        print("The item's quantity you want to rent doesn't appear to be available in the store.")
                        break
                    else:
                        updated_quantity = int(get_quantity_of_selected_item) - int(quantity)
                        myDictionary[valid_id][3] = str(updated_quantity)
                        update_item_quantity(myDictionary)
                        break  
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    
            
            
            item_name = myDictionary[valid_id][0]
            user_selected_quantity = quantity
            item_price = myDictionary[valid_id][2]
            selected_item_price = item_price.replace("$", "")
            total_bill = int(selected_item_price) * int(quantity)

            item_rented_by_user.append([item_name, user_selected_quantity, item_price, total_bill])
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_bill(name_of_user,phone_num_of_user,item_rented_by_user)
   
def print_bill(name_of_user,phone_num_of_user,item_rented_by_user):
    today_date_and_time = datetime.now()
    formatted_date_and_time = today_date_and_time.strftime("%Y-%m-%d %H:%M")
    rented_date = formatted_date_and_time
    
    print("\n")
    print("\t \t \t \t \t \t  Welcome to Event Equipment Rental Shop")
    print("\t \t \t \t \t \t             Kathmandu, Nepal")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t             Customer Details")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name of the customer:", str(name_of_user).upper())
    print("Contact number:", str(phone_num_of_user))
    print("Date and time of renting:", rented_date)
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
    write_bill_to_file(name_of_user, phone_num_of_user, rented_date, item_rented_by_user, total)    
    
def get_rented_days():
    while True:
        try:
            days_rented = int(input("Enter the number of days you have rented items: "))
            if days_rented >= 0:
                return days_rented
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_fine(total, days_rented):
    late_fee_per_day = 5
    days_delayed = days_rented - 5
    if days_delayed <= 0:
        fine = 0
    else:
        fine = days_delayed * late_fee_per_day
    total_with_fine = total + fine
    return total_with_fine, fine

def return_item():
    name_of_user, phone_num_of_user = user_info()
    open_bill(name_of_user, phone_num_of_user)
    total = extract_total_from_file(name_of_user, phone_num_of_user)
    days_rented = get_rented_days()
    total_with_fine, fine = calculate_fine(total, days_rented)  
    returned_items = extract_returned_items_from_file(name_of_user, phone_num_of_user)  
    
    update_inventory(returned_items) 
    write_bill_to_file_after_return(name_of_user, phone_num_of_user, total_with_fine, fine)
    write_returned_items_to_file(name_of_user, phone_num_of_user, returned_items)
    print("\n")
    try:
        print("Do you want to print the updated bill?")
        print_updated_bill = input("Enter 'Y' to Print or 'N' to skip: ")

        if print_updated_bill.lower() == 'y':
            open_bill(name_of_user, phone_num_of_user)
        else:
            print("Item returned and bill updated.\n")
    except Exception as e:
        print("An error occurred:", str(e))

def update_inventory(returned_items):
    myDictionary = store_in_dictionary()
    for item_data in returned_items:
        item_name = item_data[0]
        returned_quantity = int(item_data[1])
        
        for item_id, item_info in myDictionary.items():
            if item_info[0] == item_name:
                current_quantity = int(item_info[3])
                updated_quantity = current_quantity + returned_quantity
                item_info[3] = str(updated_quantity)
                break
        
    update_item_quantity(myDictionary)
    

    
def exit_program():
    print("Thank you for using our system")  

