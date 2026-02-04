def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Forge"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "operations"]
    ids = ["001", "002", "003", "004", "005"]

    return names, ranks, divisions, ids
init_database()

def display_menu():

    username = input("enter username: ").strip()

    print("Star Trek Fleet Management")
    print(f"logged in as {username}")
    print("1. add crew")
    print("2. remove crew")
    print("3. update crew rank")
    print("4. display roster")
    print("5. search crew")
    print("6. filter by division")
    print("7. calculate payroll")
    print("8. count officers")
    print("9. exit")

    try:
        opt = int(input("choose option: "))
        return username, opt
    except ValueError:
        print("invalid option, please try again")
        return 0
display_menu()

def add_members(names, ranks, divisions, ids):
    new_id = int(input("enter new crew id: "))
    while new_id in ids:
        print("this id already exists")
        new_id = int(input("enter new id: "))
    
    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    rank = input("enter new crew rank:")
    while rank not in valid_ranks:
        print("invalid rank")
        rank = input("please enter a valid rank: ")

    names.append(input("enter name: "))
    ranks.append(rank)
    divisions.append(input("enter division: "))
    ids.append(new_id)
add_members()

def main():
    names, ranks, divisions, ids = init_database

    username, opt = display_menu

    while opt != 9:
        if opt == 1:
            add_members(names, ranks, divisions, ids)
        elif opt == 2:
            remove_member(names, ranks, divisions, ids)

main()        