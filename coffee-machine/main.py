from coffee_machine import CoffeeMachine


def main():

    machine = CoffeeMachine()

    while True:

        coffee_list, sizes = machine.picking()

        coffee_list_len = len(coffee_list)
        sizes_len = len(sizes)

        print("\nPick your coffee\n")

        while True:
            for index, coffee in enumerate(coffee_list, 1):
                print(index, coffee)

            print("Pick coffee (1-{})".format(coffee_list_len))

            coffee_entry = input()
            if validate_coffee_selection_input(coffee_entry, coffee_list_len):
                break
            else:
                continue

        coffee_type = coffee_list[int(coffee_entry)-1]

        while True:
            for index, size in enumerate(sizes, 1):
                print(index, size)

            print("Pick size (1-{})".format(sizes_len))

            size_entry = input()
            if validate_coffee_selection_input(size_entry, sizes_len):
                break
            else:
                continue

        coffee_size = sizes[int(size_entry)-1]

        machine.transition('coffee_picked')

        while True:
            print("\nYour coffee is {size} {coffee}.\n"
                  "Brew - y || Back to selection - b || Quit - q\n".format(size=coffee_size, coffee=coffee_type))
            entry = input().lower()

            if validate_navigation_input(entry):
                break
            else:
                continue

        if entry == 'b':
            machine.transition('back')
            continue
        if entry == 'q':
            break

        print("\nBrewing...\n")
        brewed_coffee = machine.brewing(coffee_type, coffee_size)

        machine.transition('serve')
        machine.serving(brewed_coffee)

        while True:
            print("\nCoffee is ready to serve! Do you want another?\n"
                  "Back to selection - y/b || Quit - q\n")
            entry = input()

            if validate_navigation_input(entry):
                break
            else:
                continue

        if entry == 'y' or entry == 'b':
            machine.transition('back')
            continue
        if entry == 'q':
            break

    print("\nThank you! Shutting down\n")


def validate_coffee_selection_input(entry, list_len):
    try:
        if 1 <= int(entry) <= list_len:
            return True
        else:
            print("Not between range, try again")
            return False
    except ValueError:
        print("Invalid input, try again")
        return False


def validate_navigation_input(entry):
    if entry == 'y' or entry == 'b' or entry == 'q':
        return True
    else:
        print("Invalid input, try again")
        return False


if __name__ == '__main__':
    main()
