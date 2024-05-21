from termcolor import colored

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_completed(self, index):
        try:
            self.tasks[index].completed = True
        except IndexError:
            print(colored("🚫 The entered position does not exist in the list.", "red"))

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✅ Completed" if task.completed else "🔴 Pending"
            print(f"{i+1}. {task.description} - Status: {colored(status, 'green' if task.completed else 'yellow')}")

    def delete_task(self, index):
        try:
            del self.tasks[index]
        except IndexError:
            print(colored("🚫 The entered position does not exist in the list.", "red"))


if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n1. ➕ Add task")
        print("2. ✅ Mark task as completed")
        print("3. 📋 Show all tasks")
        print("4. ❌ Delete task")
        print("5. 🚪 Exit")

        option = input("Enter an option: ")

        if option == "1":
            description = input("Enter the task description: ")
            manager.add_task(description)
        elif option == "2":
            print("\n📋 Current tasks:")
            manager.show_tasks()
            index = int(input("\nEnter the number of the task to mark as completed: ")) - 1
            manager.mark_completed(index)
        elif option == "3":
            print("\n📋 Current tasks:")
            manager.show_tasks()
        elif option == "4":
            print("\n📋 Current tasks:")
            manager.show_tasks()
            index = int(input("\nEnter the number of the task to delete: ")) - 1
            manager.delete_task(index)
        elif option == "5":
            break
        else:
            print(colored("⚠️ Invalid option. Please enter a valid option.", "red"))
