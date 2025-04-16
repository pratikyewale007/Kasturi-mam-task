cart=[]

def add_item(item):
    cart.append(item)
    print(f"{item} added to the cart.")

def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from the cart.")
    else:
        print(f"{item} not found in the cart.")

def count_items():
    return len(cart)

def main():
    add_item=input("Enter the item you want to add to the cart: ")
    remove_item=input("Enter the item you want to remove from the cart: ")

    print(f"Total items in the cart: {count_items()}")
    print("Items in the cart:", cart)

if __name__ == "__main__":
    main()