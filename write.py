from read import *

def update_item_quantity(updated_dictionary):
    
    with open("items-info.txt", "w") as file:
        for values in updated_dictionary.values():
            file.write(str(values[0]) + "," + str(values[1]) + ","+ str(values[2]) + ","+ str(values[3]) + "," )
            file.write("\n")
        
    
def write_bill_to_file(name_of_user, phone_num_of_user, formatted_date_and_time, item_rented_by_user, total):
    with open(f"{name_of_user}_{phone_num_of_user}.txt", 'w') as file:
        file.write("\n")
        file.write(f"\t\t\t\t\t\t\t\tWelcome to Event Equipment Rental Shop\n")
        file.write(f"\t\t\t\t\t\t\t             Kathmandu, Nepal\n")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Customer Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write(f"Name of the customer: {name_of_user.upper()}\n")
        file.write(f"Contact number: {phone_num_of_user}\n")
        file.write(f"Date and time of renting: {formatted_date_and_time}\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Items Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        file.write("Item Name \t\t\t\t\t\t\t\t\t Total Quantity \t     Unit Price \t\t\t\t  Total\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in item_rented_by_user:
            file.write(f"{i[0]}\t\t\t   {i[1]}\t\t\t\t   {str(i[2])} ${i[3]}\n")

        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t     Grand Total: ${}\n".format(total))
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("# Duration of Rented Item is for 5 Days.\n")
        file.write("Note: In case of Delay, you will be Fined.\n")
        file.write("\n")


