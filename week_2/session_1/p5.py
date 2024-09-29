def restock_inventory(current_inventory, restock_list):
    for item in restock_list:
        if item in current_inventory:
             current_inventory[item] = current_inventory[item] + restock_list[item] 
        else:
            current_inventory[item] = restock_list[item]
    return current_inventory


def main():
    current_inventory = {"apples": 30, "bananas": 15,"oranges": 10}

    restock_list = {"oranges": 20, "apples": 10, "pears": 5}

    print(restock_inventory(current_inventory, restock_list))

main()
