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
             5. Exit the program""")
        choice = int(input("Enter menu choice: "))

        if choice == 1:
                contacts = print_list(contacts)
        elif choice == 2:
                contacts = add_contact(contacts)
        elif choice == 3:
                contacts = modify_contact(contacts)
        elif choice == 4:
                contacts = delete_contact(contacts)
        elif choice == 5:
                quit = True