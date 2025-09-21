tasks = []  # empty list to store tasks

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Deleted: {removed}\n")
    except (ValueError, IndexError):
        print("Invalid choice.\n")

def main():
    while True:
        print("==== To-Do List App ====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
