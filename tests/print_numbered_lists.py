# Test getting a series of entries into a list of expected length
# Test to ensure entries match separate list before being added to list


def list_creation(number_of_entries):
    list = []
    for i in range(0, number_of_entries):
        while True:
            entry = input(f"Element {i + 1}/{number_of_entries}: ")
            if entry != "":
                list.append(entry)
                break
            else:
                print("Can't add empty value to list. Try again.")

    return list


def cross_check(master_list):
    cross_checked_list = []
    while True:
        entry = input("Element to check: ")
        for element in master_list:
            if entry == element:
                print("Name entered to list!")
                cross_checked_list.append(entry)
                return cross_checked_list
            else:
                print("Element does not match, please try again from below options.")
                for element in master_list:
                    print(element)
