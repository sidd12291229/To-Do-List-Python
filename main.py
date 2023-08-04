class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def display_tasks(self):
        print("Tasks:")
        for index, task_info in enumerate(self.tasks):
            status = " [X]" if task_info["completed"] else " [ ]"
            print(f"{index + 1}. {task_info['task']}{status}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task_info in self.tasks:
                file.write(f"{task_info['task']},{task_info['completed']}\n")

    def load_from_file(self, filename):
        self.tasks.clear()
        try:
            with open(filename, "r") as file:
                for line in file:
                    task, completed = line.strip().split(",")
                    self.tasks.append({"task": task, "completed": completed == "True"})
        except FileNotFoundError:
            pass

def main():
    todo_list = ToDoList()
    filename = "todo.txt"  # You can change this to your preferred file name.

    # Load tasks from the file (if any)
    todo_list.load_from_file(filename)

    while True:
        print("\n---- To-Do List ----")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_as_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            todo_list.save_to_file(filename)
            print("To-Do List saved. Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
