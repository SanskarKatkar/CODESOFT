tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i+1}. {task['task']} - {status}")

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to mark as done: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        show_tasks()
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")