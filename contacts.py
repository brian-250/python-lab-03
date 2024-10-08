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
    []:
        Modifys 'contacts' list with the 'full_name' list at the
        specified index,'index_modifier'.

    Returns:
        2D list: Updated 'contacts' list.

    Example:
    >>> modify_contact(contacts, first_name, last_name)
    contacts
    """
    if index >= 0 and index < len(contacts):
        full_name = []
        full_name.append(first_name)
        full_name.append(last_name)
        contacts[index] = full_name
        return contacts
    else:
        print("Invalid index number.")
        return False
    return contacts

def delete_contact(contacts, index):
    """
    Deletes element at the desired index from 'contacts'.

    Paramters:
    contacts (2D list, int): Tuffy Titan's contacts list.
    index (2D lists, int): The value that helps us identify
                           the element to remove from the
                           'contacts' list.

    Statements:
    del:
        Deletes element at desired index in 'contacts'.

    Returns:
        2D list: Updated 'contacts' list.

    Example:
    >>> delete_contact(contacts, index)
    contacts
    """
    if index >= 0 and index < len(contacts):
        del contacts[index]
        return contacts
    else:
        print("Invalid index number.")
        return False
    return contacts

def sort_contacts(contacts, column):
    if column == 0:
        contacts.sort(key=lambda x: x[0])
    elif column == 1:
        contacts.sort(key=lambda x: x[1])
    return contacts