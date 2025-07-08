# TO DO LIST APPLICATION

from colorama import Fore  # type: ignore

tasks = []

while True:
    print()
    print(Fore.BLUE + "To Do List Application".upper())
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Tasks")
    print("4. Exit \n")
    try:
        choice = int(input("Choose an option: "))
        if choice < 1 or choice > 4:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number between 1 and 4.")
        continue

    print(Fore.RESET)
    if choice == 1:
        task = input("Enter task to add: ")
        tasks.append(task)

        i: int = 0
        for task in tasks:
            i += 1
            print(i, task, sep=" - ")
        print(Fore.GREEN + "\nTask has been added successfully")

    elif choice == 2:
        task = input("Remove a task: ")
        if task in tasks:
            tasks.remove(task)
            print(Fore.GREEN + "\nTask has been removed successfully")
        else:
            print(Fore.RED + "\nTask Not Found")

    elif choice == 3:
        if not tasks:
            print("You Have No Current Tasks")
        else:
            print("Your Current Tasks\n")
            i: int = 0
            for task in tasks:
                i += 1
                print(i, task, sep=" - ")

    elif choice == 4:
        break

print(Fore.BLUE + "\nThank you for using the To Do List Application!" + Fore.RESET)

# SAMPLE TASKS - House Chores - Jog - Laundry - Read -  Work
