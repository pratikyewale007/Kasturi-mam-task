class Students:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.percentage = 0.0

    def accept_details(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter student age: "))
        self.percentage = float(input("Enter student percentage: "))
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}%")

    def modify_details(self):
        modify = input("U want the student details to be modified? (y/n): ")
        if modify.lower() == "y":
            print("Select the detail to be modified:")
            print("1. Name")
            print("2. Age")
            print("3. Percentage")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                self.name = input("Enter new name: ")
            elif choice == 2:
                self.age = int(input("Enter new age: "))
            elif choice == 3:
                self.percentage = float(input("Enter new percentage: "))
            else:
                print("Invalid choice")
        
        elif modify.lower == "n":
            print("No modifications made.")
        
        else:
            print("No Modifications made.")

def main():
    student1 = Students()
    student2 = Students()

    print("""Enter details for the 1st student""")
    student1.accept_details()
    student1.display_details()
    student1.modify_details()
    student1.display_details()

    print("""Enter details for the 2nd student""")
    student2.accept_details()
    student2.display_details()
    student2.modify_details()
    student2.display_details()

if __name__ == "__main__":
    main()
