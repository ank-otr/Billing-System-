

def store_in_dictionary():
   myDictionary = {}
   with open("items-info.txt", "r") as file:
        item_id = 1
        
        for line in file: 
            line = line.replace("\n","")
            myDictionary[item_id] = line.split(",")
            item_id = item_id +1 
        return myDictionary   
        
    
def show_item():
    with open("items-info.txt", "r") as file:
        i = 1 
        for line in file:
            print(i, "\t\t"+ line.replace(",","\t\t"))
            i = i+1
        
