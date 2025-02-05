
def contact_book():
    contact = {}
    
    while True:
        print('\nContact Book Menu:')
        print('1. Add Contact')
        print('2. View Contact')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Exit')
        
        option= input('Make an Input (1-5):')
        
        if option == '1':
            name= input('Enter Contact Name:')
            age = input('Enter Contact Age:')
            email=input('Enter Contact email:')
            fav_col=input('Enter Favorite Color:')
            contact[name]={'age': age, 'email': email, 'fav_col':fav_col}
            print(f"Contact '{name}' Added Succesfully")

        elif option == '2':
            if contact:
                print('\nContacts')
                for key, value in contact.items():
                    print(f"{key}:{value}")
            else:
                print('No such Entries') 
        
        elif option == '3':
            name= input('Enter The Contact to update: ')
            if name in contact:
                nage= input('Enter New Age:')
                nemail= input('Enter New email address:')
                nfav_col= input('Enter New Fav Color: ')
                new_info={'age':nage , 'email':nemail , 'fav_col':nfav_col}
                contact[name].update(new_info)
                print(f"contact '{name}'updated successfully")
            else:
                print(f"Contact{name} not found in the contact book")
    
        elif option == '4':
            name= input('Enter the Name of Contact to Delete:')
            if name in contact:
                del contact[name]
                print(f"Contact '{name}' Deleted")
            else:
                print(f"No contact with '{name}'found")
        
        elif option == '5':
            print('Good Bye')
            break
        else:
            print('Invalid Choice , Please try again')
        
contact_book()

    