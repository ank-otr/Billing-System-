from read import *

def update_item_quantity(updated_dictionary):
    myDictionary = store_in_dictionary()
    with open("items-info.txt", "w") as file:
        for values in updated_dictionary.values():
            file.write(",".join(values))
            file.write("\n")
        
    
    

