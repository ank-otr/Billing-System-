def store_in_dictionary():
    file= open("items-info.txt", "r")
    item_id = 1
    myDictionary = {}

    for line in file: 
        line = line.replace("\n","")
        myDictionary[item_id] = line.split(",")
        item_id = item_id +1    
    file.close()
def show_item():
    file = open("items-info.txt", "r")
    i = 1 
    for line in file:
        print(i, "\t\t"+ line.replace(",","\t\t"))
        i = i+1
    file.close()
    