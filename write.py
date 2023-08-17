from read import *

def update_item_quantity(updated_dictionary):
    
    with open("items-info.txt", "w") as file:
        for values in updated_dictionary.values():
            file.write(str(values[0]) + "," + str(values[1]) + ","+ str(values[2]) + ","+ str(values[3]) + "," )
            file.write("\n")
        
    
    

