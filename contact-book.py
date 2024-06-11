contacts = {}

def contact_details():
      if contacts:
        print('Names\t\t\t\tPhone Numbers')
        for name, details in contacts.items():
            print(f"{name}\t\t{details['Contact no:']}")
      else:
        print('No contacts found.')

while True:
       print("\n----Welcome to my mini Project 'Contact List'----\n")
       choice = int(input(' 1. Add new contact\n 2. View contact list\n 3. Search contact\n 4. Update contact\n 5. Delete contact\n 6. Exit \n Enter your choice (1-6): '))
       if choice == 1:
              name = input('\nEnter the contact name ').strip()
              if name in contacts:
                    print('Contact already exist.')
              else:
                phone = input('\nEnter the mobile number ')
                email = input('Enter the email address ')
                address = input('Enter the address ')
                contacts[name] = {'Contact no:':phone, 'Email:':email,'Address:':address}
                print('Contact added successfully.')

       elif choice == 2:
               if not contacts:
                     print('Empty contact list.')
               else:
                     contact_details()

       elif choice == 3:
              search_name = input('\nEnter the contact name you want to search ').strip()
              if search_name in contacts:
                    details = contacts[search_name]
                    print(f"Name: {search_name}, Number: {details['Contact no:']} ")
              else:
                    print('Contact not found.')

       elif choice == 4:
               update_name = input('\nEnter the contact name whose details you want to update ').strip()
               if update_name in contacts:
                     phone = input('Enter the mobile number ')
                     email = input('Enter the email address ')
                     address = input('Enter the address ')
                     contacts[update_name] =  {'Number': phone, 'Email': email, 'Address':address}
                     print('Contact details updated successfully.')
               else:
                     print('Contact not found.')

       elif choice == 5:
               del_cont = input('\nEnter the contact name you want to delete ').strip()
               if del_cont in contacts:
                     del contacts[del_cont]
                     print('Contact deleted successfully.')
               else:
                     print('Contact not found.')

       elif choice == 6:
               print('Program exit.')
               break
       else:
             print('Invalid choice! Please enter a valid choice.(1-6)')