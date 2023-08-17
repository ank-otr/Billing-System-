from operations import *
from read import *
from write import *
from datetime import datetime



def main():
    welcome_message()

    option = input("Choose the operation you want to continue: ")

    if option == '1':
        print("\t \t \t \t \t           # You have Chosen Rent option.")
        user_info()
        print_item_list()
        rent_validation()
           
    elif option == '2':
        print("Return Items option is under construction.")
    elif option == '3':
        print("Exiting the program.")
    else:
        print("Invalid option. Please choose a valid option.")    

if __name__ == "__main__":
    main()