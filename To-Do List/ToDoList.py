def task():
    tasks = []
    print("-----------WELCOME TO TASK MANAGEMENT SYSTEM-----------")

    task_total = int(input("Enter the num of tasks to be added = "))
    for i in range(1, task_total + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"The tasks are\\n{tasks}")

    while True:
        operation = int(input(" Enter 1 - Adding new task\\n Enter 2 - Updating existing task\\n Enter 3 - Deleting a task\\n Enter 4 - To show the list of tasks\\n Enter 5 - Deleting all tasks\\n Enter 6 - exit\\n"))
        
        if operation == 1:
            add = input("Enter the task to be added = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added....")

        elif operation == 2:
            up_val = input("Enter the task to be updated = ")
            if up_val in tasks:
                updated_task = input("Enter new task = ")
                ind = tasks.index(up_val)
                tasks[ind] = updated_task
                print("Task has been successfully updated")
            else:
                print("Task not found")

        elif operation == 3:
            del_val = input("Enter the task to be deleted = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print("Task has been deleted")
            else:
                print("Task not found")

        elif operation == 4:
            print(f"The tasks are :- \\n {tasks}")

        elif operation == 5:
            tasks.clear()
            print("All tasks have been deleted")

        elif operation == 6:
            print("Closing the program")
            break

        else:
            print("Invalid Input")

task()
