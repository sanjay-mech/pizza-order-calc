#import libraries
import json
f_path = "pizza order\pizaa_data.json"
base_data = None
toppings_data = None
size_data = None



# get pizza base
def get_pizza_base_data(abc):
    with open(abc,"r") as fp:
        data = json.load(fp)
        return data["base"]

# get toppings
def get_pizza_toppings_data(file_path):
    with open(file_path,"r") as fp:
        data = json.load(fp)
        return data["toppings"]

# get size data
def get_pizza_size_data(file_path):
    with open(file_path,"r") as fp:
        data = json.load(fp)
        return data["size"]
# calculate price



def calculate_pricing(pizza_data):
    price = base_data[pizza_data['base']]["price"]
    estimate_time = base_data[pizza_data['base']]["preparation_time"]
    price += toppings_data[pizza_data['topping']]["price"]
    price = price * size_data[pizza_data['size']]
    return price,estimate_time
# ask Base
def ask_base_data():
    print("Please select base of your pizza")
    for k in base_data.keys():
        print(k)
    print("#############")
    base = input("Enter choice")
    while base not in base_data:
        print("Wrong Choice")
        base = input("Enter choice")
    return base
# ask toppings
def ask_toppings():
    print("Please select Toppings of your pizza")
    for k in toppings_data.keys():
        print(k)
    print("#############")
    topping = input("Enter choice")
    while topping  not in toppings_data:
        print("Wrong Choice")
        topping = input("Enter choice")
    return topping
# ask Size
def ask_size():
    print("Please select Size of your pizza")
    for k in size_data.keys():
        print(k)
    print("#############")
    topping = input("Enter choice")
    while topping  not in size_data:
        print("Wrong Choice")
        topping = input("Enter choice")
    return topping
# confirm
def is_confirm(pizza_data):
    print("Below is your order summary")
    for k,v in pizza_data.items():
        print(k,":",v)
    print("")    
    choice = input("Do you want to confirm")
    if choice == "y":
        return True
    else:
        return False
# store
def store_order(pizza_data):
    with open("orders.json","w") as fp:
        json.dump(pizza_data,fp)


base_data = get_pizza_base_data(f_path)
toppings_data = get_pizza_toppings_data(f_path)
size_data = get_pizza_size_data(f_path)
pizza_choice = {}
pizza_choice["base"]=ask_base_data()
pizza_choice["topping"]=ask_toppings()
pizza_choice["size"]=ask_size()
pizza_choice["price"],pizza_choice["estimate_time"] = calculate_pricing(pizza_choice)
if is_confirm(pizza_choice):
    store_order(pizza_choice)






    
