from read import *

def update_item_quantity(updated_dictionary):
    
    with open("items-info.txt", "w") as file:
        for values in updated_dictionary.values():
            file.write(str(values[0]) + "," + str(values[1]) + ","+ str(values[2]) + ","+ str(values[3]) + "," )
            file.write("\n")
   
def write_bill_to_file(name_of_user, phone_num_of_user, rented_date, item_rented_by_user, total):
    with open(f"{name_of_user}_{phone_num_of_user}.txt", 'w') as file:
        file.write("\n")
        file.write(f"\t\t\t\t\t\t\t  Welcome to Event Equipment Rental Shop\n")
        file.write(f"\t\t\t\t\t\t\t             Kathmandu, Nepal\n")
        file.write("\n")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Customer Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write(f"Name of the customer: {name_of_user.upper()}\n")
        file.write(f"Contact number: {phone_num_of_user}\n")
        file.write(f"Date and time of renting: {rented_date}\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Items Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        file.write("Item Name \t\t\t\t\t     Quantity \t\t             Unit Price \t\t\t\t               Amount\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in item_rented_by_user:
            file.write(f"{i[0]}\t\t\t{i[1]}\t\t\t\t{i[2]}\t\t\t\t${i[3]}\n")


        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t        Total Amount: ${}\n".format(total))
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\n")
    return name_of_user, phone_num_of_user, rented_date, total

def write_bill_to_file_after_return(name_of_user, phone_num_of_user, total_with_fine, fine):
    with open(f"{name_of_user}_{phone_num_of_user}.txt", 'a') as file:
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t Fine Amount: ${}\n".format(fine))
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t Grand Total: ${}\n".format(total_with_fine))
            file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

def write_returned_items_to_file(name_of_user, phone_num_of_user, returned_items):
    file_name = f"{name_of_user}_{phone_num_of_user}_returned.txt"
    
    with open(file_name, 'w') as file:
        file.write("\n")
        file.write(f"\t\t\t\t\t\t\t  Return Details\n")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Customer Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write(f"Name of the customer: {name_of_user.upper()}\n")
        file.write(f"Contact number: {phone_num_of_user}\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Returned Items\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        file.write("Item Name \t\t\t\t\t     Quantity\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for item_name, item_quantity in returned_items:
            file.write(f"{item_name}\t\t\t{item_quantity}\n")

    print("Returned items written to file:", file_name)
    return file_name
