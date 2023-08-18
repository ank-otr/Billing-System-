from operations import *
from read import *
from write import *
from datetime import datetime



def main():
    loop = True
    while loop == True:
        welcome_message()
        option = input("Choose the operation you want to continue: ")
        if option == '1':
            print("\t \t \t \t \t           # You have Chosen Rent option.")
            rent_item()
            
            continue
        elif option == '2':
            print("\t \t \t \t \t           # You have Chosen Return option.")
            return_item()
            
        elif option == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid option.")    

main()