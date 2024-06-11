tasks = []

while True:
    print("\n----Welcome to my mini Project 'To-do List'----\n")

    choice = int(input(' 1. Create a task \n 2. Update a task \n 3. View to-do list\n 4. Delete a task\n 5. Exit \n Enter your choice (1-5): '))
    if choice == 1:
        new_task = input('\nEnter the task you want to add: ').strip()
        if new_task in tasks:
            print('Task already added in the list.')
        else:
            tasks.append(new_task)
            print(f"Task '{new_task}' is added to the list.")

    elif choice == 2:
        try:
            update_task = int(input('\nEnter the task number you want to update '))
            if update_task <= len(tasks) and update_task > 0: 
                New_task = input('\nEnter the updated task ').strip()
                tasks[update_task-1] = New_task
                print(f'Task {update_task} updated successfully.')
            else:
                print('Such task is not exist in the list.')
        except:
            print('Invalid input! Please enter a valid integer number.')

    elif choice == 3:
        if not tasks:
            print('The To-do list is empty.')
        else:
            print('Current tasks: ')
            for i, task in enumerate(tasks):
                print(f'Task {i+1}. {task}')

    elif choice == 4:
        try:
            delete_task = int(input('\nEnter the task number you want to delete '))
            if delete_task <= len(tasks) and delete_task > 0:
                deleted_task = tasks.pop(delete_task - 1)
                print(f'Task {delete_task} "{deleted_task}" is deleted from the list.')
            else:
                print(f'Task number {delete_task} does not exist in the list.')
        except:
            print('Invalid input! Please enter a valid integer number.')

    elif choice == 5:
        print('Program exit. Thanks for using!')
        break
    else:
        print('Invalid choice! Please enter a valid choice(1-5).')