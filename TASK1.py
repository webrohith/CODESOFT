from datetime import datetime, timedelta

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, hour, am_pm):
        current_time = datetime.now()
        if am_pm.lower() == 'pm' and hour != 12:
            hour += 12
        elif am_pm.lower() == 'am' and hour == 12:
            hour = 0
        scheduled_time = current_time.replace(hour=hour, minute=0, second=0, microsecond=0)
        self.tasks.append((task, scheduled_time))

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            sorted_tasks = sorted(self.tasks, key=lambda x: x[1])
            for i, (task, scheduled_time) in enumerate(sorted_tasks, 1):
                formatted_time = scheduled_time.strftime('%I:%M %p')
                print(f"{i}. {task} - {formatted_time}")

    def update_task(self, task_number, new_task, new_hour, new_am_pm):
        if 1 <= task_number <= len(self.tasks):
            current_time = datetime.now()
            if new_am_pm.lower() == 'pm' and new_hour != 12:
                new_hour += 12
            elif new_am_pm.lower() == 'am' and new_hour == 12:
                new_hour = 0
            scheduled_time = current_time.replace(hour=new_hour, minute=0, second=0, microsecond=0)
            self.tasks[task_number - 1] = (new_task, scheduled_time)
            print(f"Task {task_number} updated successfully.")
        else:
            print("Invalid task number")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            formatted_time = deleted_task[1].strftime('%I:%M %p')
            print(f"Task {task_number} deleted: {deleted_task[0]} - {formatted_time}")
        else:
            print("Invalid task number")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            hour = int(input("Enter the scheduled hour (1-12): "))
            am_pm = input("Enter 'AM' or 'PM': ")
            todo_list.add_task(task, hour, am_pm)
            print("Task added successfully.")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            new_hour = int(input("Enter the new scheduled hour (1-12): "))
            new_am_pm = input("Enter 'AM' or 'PM': ")
            todo_list.update_task(task_number, new_task, new_hour, new_am_pm)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the ToDoList application. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
