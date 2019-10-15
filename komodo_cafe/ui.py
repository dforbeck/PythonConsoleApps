import manager_repo

while True:  # want it to keep running until tell it to quit
    prompt = """
    What would you like to do?

    1) View menu
    2) Add item to menu
    3) Change item
    4) Remove item
    5) Exit
    > """
    option = int(input(prompt))  
    # there is a keyword prompt, but it is also inferred in variable
    print(option)

    if option == 5:
        quit()
    elif option == 1:
        print(manager_repo.read_menu()) # print the return
    elif option == 2:
        new_name = input("What is the new item name?")
        new_price = float(input("What is the item price?"))
        print(manager_repo.create_item(new_name,new_price))        
    elif option == 3:
        for i, item in enumerate(manager_repo.current_menu.contents): 
            # prints each item out with index number
            print(f'{i} > {item}')
        which_item = int(input("Which item number would you like to edit? >"))        
        new_name = input(f'Change name(Leave blank to not edit) >')
        new_price = (input(f'Change price (leave blank to not edit))>'))

        print(manager_repo.change_item(which_item, new_name, new_price))
        
    # Note that if want to change a copy of list, need [:] and create a copy somewhere
    
    elif option == 4:
        print("HIT OPTION 4")

    else:
        pass # go back to top