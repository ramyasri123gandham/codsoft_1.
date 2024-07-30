class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i+1}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number-1]["task"] = new_task
            print(f"Task {task_number} updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number-1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def mark_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number-1]["completed"] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()

    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

    while True:
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.mark_complete(task_number)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
