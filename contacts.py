# Name: Brian Milian
# Date: 9/11/24
# File Purpose: Tuffy Titan's contacts list manipulation functions

def print_list(contacts):
    """
    Prints each list in 'contacts' on a new line.

    Parameters:
    contacts (2D list): The only list in the parameter.

    Methods:
    print():
        Prints a title for Tuffy Titan's 'contacts' list.
    print():
        Prints a header for the index number, first name, and last name of
        each list in 'contacts'.
    print():
        Prints each list in 'contacts' in the chronilogical format
        of: index number, first name, and last name.
    """
    print("------------TUFFY TITAN'S CONTACTS LIST-------------")
    print("#-------First Name------------Last Name-------------")
    for index in range(len(contacts)):
        print(f'{str(index):8}{contacts[index][0]:22}{contacts[index][1]:22}')
    return contacts

def add_contact(contacts, first_name, last_name):
    """
    Adds a new name to the 'contacts' list.

    Paramters:
    contacts (2D list, string, string): Tuffy Titan's contacts list.
    first_name (string, string, string): The first name of the person added to
                                         'contacts' list
    last_name (string, string, string): The last name of the person added to
                                         'contacts' list

    Methods:
    append():
        Appends 'first_name' to the 'full_name' list.
    append():
        Appends 'last_name' to the 'full_name' list.
    append():
        Appends 'full_name' list to the 'contacts' list.

    Returns:
        2D list: Updated 'contacts' list.

    Example:
    >>> add_contact(contacts, first_name, last_name)
    contacts
    """
    full_name = []
    full_name.append(first_name)
    full_name.append(last_name)
    contacts.append(full_name)
    return contacts

def modify_contact(contacts, first_name, last_name, index):
    """
    Modifys the first and last name of an index in 'contacts'.

    Paramters:
    contacts (2D list): Tuffy Titan's contacts list.

    Methods:
    append():
        Appends 'first_name' to the 'full_name' list.
    append():
        Appends 'last_name' to the 'full_name' list.
    append():
        Modifys 'contacts' list with the 'full_name' list at the
        specified index,'index_modifier'.

    Returns:
        2D list: Updated 'contacts' list.

    Example:
    >>> modify_contact(contacts)
    contacts
    """
    index_modifier = int(input("What index do you want to modify? "))
    if index_modifier >= 0 and index_modifier < len(contacts):
        first_name = input("Provide your first name: ")
        last_name = input("Provide your last name: ")
        full_name = []
        full_name.append(first_name)
        full_name.append(last_name)
        contacts[index_modifier] = full_name
    else:
        print("Invalid index number.")
    return contacts

def delete_contact(contacts):
    """
    Deletes element at the desired index from 'contacts'.

    Paramters:
    contacts (2D list): Tuffy Titan's contacts list.

    Statements:
    del:
        Deletes element at desired index in 'contacts'.

    Returns:
        2D list: Updated 'contacts' list.

    Example:
    >>> delete_contact(contacts)
    contacts
    """
    index_modifier = int(input("What index do you want to delete? "))
    if index_modifier >= 0 and index_modifier < len(contacts):
        del contacts[index_modifier]
    else:
        print("Invalid index number.")
    return contacts