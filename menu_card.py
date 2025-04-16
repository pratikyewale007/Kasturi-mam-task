fruits = ["apple", "banana", "cherry"]

def display():
    print("Display Fruits Menu:")
    for fruit in fruits:
        print(f"{fruit}")

def update():
    fruit = input("Enter the fruit u want to update: ")
    if fruit in fruits:
        index = fruits.index(fruit) 
        new_fruit = input("Enter the new fruit: ") 
        fruits[index] = new_fruit 
        print(f"{fruit} updated to {new_fruit}")
    else:
        print(f"{fruit} not found in the menu")
    
    print("Updated Fruits Menu:")
    for fruit in fruits:
        print(f"{fruit}")

def add():
    fruit = input("Enter the fruit you want to add: ")
    if fruit not in fruits:
        fruits.append(fruit)
        print(f"{fruit} added to the menu")
    else:
        print(f"{fruit} already exists in the menu")
    print("Updated Fruits Menu:")
    for fruit in fruits:
        print(f"{fruit}")

def delete():
    fruit = input("Enter the fruit you want to delete: ")
    if fruit in fruits:
        fruits.remove(fruit)
        print(f"{fruit} deleted from the menu")
    else:
        print(f"{fruit} not found in the menu")
    print("Updated Fruits Menu:")
    for fruit in fruits:
        print(f"{fruit}")

def main():
        print("\nMenu:")
        print("1. Display Fruits Menu")
        print("2. Update Fruit")
        print("3. Add Fruit")
        print("4. Delete Fruit")
        print("5. Exit")

        choice = input("Enter your choice: ")
            
        if choice == '1':
            display()
        elif choice == '2':
            update()
        elif choice == '3':
            add()
        elif choice == '4':
            delete()
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
