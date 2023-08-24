

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

def open_bill(name_of_user, phone_num_of_user):
    file_name = f"{name_of_user}_{phone_num_of_user}.txt"
    try:
        with open(file_name, "r") as file:
            bill_info = file.readlines()
            
        for line in bill_info:
            print(line.rstrip("\n"))
    except FileNotFoundError:
        print("No existing bill found for the user.")

def extract_total_from_file(name_of_user, phone_num_of_user):
    file_name = f"{name_of_user}_{phone_num_of_user}.txt"
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if "Total Amount: $" in line:
                    total = float(line.split("$")[1])
                    return total
        
    except FileNotFoundError:
        print("No existing bill found for the user.") 

def extract_returned_items_from_file(name_of_user, phone_num_of_user):
    file_name = f"{name_of_user}_{phone_num_of_user}.txt"
    returned_items = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            found_items_section = False
            for line in lines:
                if "Items Details" in line:
                    found_items_section = True
                elif found_items_section and not line.strip():
                    break  # Stop processing when reaching an empty line
                elif found_items_section:
                    item_data = line.strip().split('\t\t\t')
                    if len(item_data) >= 4 and item_data[1]:  # Ensure there are at least 4 elements and non-empty quantity
                        item_name = item_data[0]
                        item_quantity = item_data[1].strip()
                        returned_items.append((item_name, item_quantity))
    except FileNotFoundError:
        print("No existing bill found for the user.")
    return returned_items

        