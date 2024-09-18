# Name: Brian Milian
# Date: 9/11/24
# File Purpose: Tuffy Titan's contacts list manipulation

from contacts import *

# Create 2D contacts list variabale
contacts = []
# Create boolean variable to use in while loop
quit = False

while quit != True:
        print("""           *** TUFFY TITAN CONTACT MAIN MENU
             1. Print list
             2. Add contact
             3. Modify contact
             4. Delete contact
             5. Sort list by first name
             6. Sort list by last name
             7. Exit the program""")
        choice = int(input("Enter menu choice: "))

        if choice == 1:
                contacts = print_list(contacts)
        elif choice == 2:
                first_name = input("Input a first name: ")
                last_name = input("Input a last name: ")
                contacts = add_contact(contacts, first_name, last_name)
        elif choice == 3:
                first_name = input("Input a new first name: ")
                last_name = input("Input a new last name: ")
                index = int(input("Input the index of the element in the contacts list to modify: "))
                contacts = modify_contact(contacts, first_name, last_name, index)
        elif choice == 4:
                index = input("Input the index of the element in the contacts list to delete: ")
                contacts = delete_contact(contacts, index)
        elif choice == 5:
                contacts = sort_contacts(contacts, 0)
        elif choice == 6:
                contacts = sort_contacts(contacts, 1)
        elif choice == 7:
                quit = True