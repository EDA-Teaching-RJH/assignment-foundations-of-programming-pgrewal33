def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Forge"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "operations"]
    ids = [1, 2, 3, 4, 5]

    return names, ranks, divisions, ids


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

def remove_member(names, ranks, divisions, ids):
    remove_id = int(input("which id do you want to remove?" ))

    if remove_id in ids:
        index = ids.index(remove_id)

        names.pop(index)
        ranks.pop(index)
        divisions.pop(index)
        ids.pop(index)
        print("member removed")
    else:
        print("invalid id")

def update_rank(names, ranks, ids):
    
    member_id = int(input("enter member id: "))

    if member_id in ids:
        index = ids.index(member_id)

        new_rank = input(f"enter new rank for {names[index]}: ")
        ranks[index] = new_rank
        print("rank updated")
    else:
        print("id not found")

def display_roster(names, ranks, divisions, ids):
    for i in range(len(names)):
        print(f"{ids[i]}\t{names[i]}\t{ranks[i]}\t{divisions[i]}")

def search_crew(names, ranks, divisions, ids):
    
    search_term = input("enter search term: ")

    print("search results")
    for i in range (len(names)):
        if search_term.lower() in names[i].lower():
            print(f"{names[i]} - {ranks[i]} - {divisions[i]}")

def filter_by_division(names, ranks, divisions, ids):

    division = input("enter division: ")

    print(f"{division} division members: ")
    for i in range(len(names)):
        if divisions[i] == division:
            print (names[i])

def calculate_payroll(ranks):

    rank_values = {

        "Captain": 1000,
        "Commander": 800,
        "Lt. Commander": 600,
        "Lieutenant": 400,

    }
    
    total = 0
    print ("payroll breakdown: ")

    rank_counts = {}
    for rank in ranks:
        total += rank_values.get(rank, 300)
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    for rank, count in rank_counts.items():
        value = rank_values.get(rank, 300)
        print(f"{rank}: {count} x {value} = {count * value} credits")

    print(f"total payroll: {total} credits")
    return total



def main():
    names, ranks, divisions, ids = init_database()

    username, opt = display_menu()

    while opt != 9:
        if opt == 1:
            add_members(names, ranks, divisions, ids)
        elif opt == 2:
            remove_member(names, ranks, divisions, ids)
        elif opt == 3:
            update_rank(names, ranks, ids)
        elif opt == 4:
            display_roster(names, ranks, divisions, ids)
        elif opt == 5:
            search_crew(names, ranks, divisions, ids)
        elif opt == 6:
            filter_by_division(names, ranks, divisions, ranks)
        elif opt == 7:
            calculate_payroll(ranks)
        username, opt = display_menu()
        


main()        