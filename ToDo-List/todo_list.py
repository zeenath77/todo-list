tasks=[]
def show_menu():
    print("\n-- To-Do List Menu --")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
def show_tasks():
    if not tasks:
        print("no tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task}")
def add_task():
    task=input("enter a new task:")
    tasks.append(task)
    print("Task added!")
def remove_task():
    show_tasks()
    try:
        task_no=int(input("enter task number to remove:"))
        if 1<=task_no<=len(tasks):
            removed=tasks.pop(task_no -1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    show_menu()
    choice=input("Choose an option(1-4):")
    if choice=="1":
        show_tasks()
    elif choice=="2":
        add_task()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        print("Done!")
        break
    else:
        print("oops!! Invalid choice.Try again")
    
    
