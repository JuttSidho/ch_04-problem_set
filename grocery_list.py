"""
implement a program that prompts the user for items, one per line, until the 
user inputs control-d (which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. No need to 
pluralize the items. Treat the user’s input case-insensitively.
"""
def count_items():
    grocery_list = {}

    while True:
        try:
            item = input("Enter an item: ")
        except EOFError:
            break

        item = item.lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    return grocery_list


def get_item_name(item_count):
    return item_count[0]


def print_sorted_list(grocery_list):
    sorted_items = sorted(grocery_list.items(), key=get_item_name)
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


def main():
    grocery_list = count_items()
    print_sorted_list(grocery_list)


if __name__ == "__main__":
    main()
