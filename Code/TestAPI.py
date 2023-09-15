import requests

res = requests.get("http://ddragon.leagueoflegends.com/cdn/13.14.1/data/en_US/tft-tactician.json")
data_item = res.json()
runing = True

def StartMenu(data_item):
    global runing
    print("<----- Select options ----->")
    print("[1] Find By ID")
    print("[2] Find By Name")
    print("[3] Find By Tier")
    print("[0] Exit...")
    menu = input("Type number to select : ")
    if menu == "1":
        findByName(data_item)
    elif menu == "2":
        print("menu 2")
    elif menu == "3":
        print("menu 3")
    elif menu == "0":
        print("Good Bye!..")
        runing = False
    else :
        print("Invalid input!")
        print("Please try again..")

def findByName(data_item):
    name = ""
    name = input("Name : ")
    item = []
    for id , item_data in data_item["data"].items():
     if item_data.get("name") == name :
        item.append({
            "id":id,
            "name":item_data["name"],
            "tier":item_data["tier"]
        })
    if name:
        print(f"Items with name {name}:")
        for data in item:
            print(f"ID: {data['id']}, Name: {data['name']} ,Tier:{data['tier']}")
    else:
        print(f"No items found with tier {item}.")
    
    if item :
        print(item)
    else :
        print("Not found....")
        

while runing == True:
    StartMenu(data_item)
    
