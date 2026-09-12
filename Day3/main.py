import json
import datetime

file = "task.json"


def load_task():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_task(task):
    desc = input("enter task :\n").strip()

    priority = input("enter priority(H,L,M)\n").strip().lower()

    if priority not in ["h", "m", "l", "high", "medium", "low"]:
        priority = "medium"

    tasks = {
        "Task": desc,
        "Priority": priority,
        "Status": "Pending"
    }

    task.append(tasks)
    save_task(task)

    print(f"Added {tasks}")


def save_task(task):
    with open(file, "w") as f:
        json.dump(task, f, indent=5)


def view_task(task):
    if not task:
        print("No tasks available!")
        return

    for i, t in enumerate(task, 1):
        if t["Status"] == "Done":
            ind = "done"
        else:
            ind = "pending"

        print(f"{i}: {ind} {t}")


def mark_done(task):
    if not task:
        print("No tasks available!")
        return

    view_task(task)

    try:
        num = int(input("task number to mark done: "))

        if num < 1 or num > len(task):
            print("enter correct task number")
            return

        if task[num - 1]["Status"] == "Done":
            print("Task is already completed!")
            return

        task[num - 1]["Status"] = "Done"

        save_task(task)

        print("Task marked as done!")

    except ValueError:
        print("Please enter a valid number!")


def delete(task):
    if not task:
        print("No tasks available!")
        return

    view_task(task)

    try:
        inp = int(input("enter task number to delete: "))

        if inp < 1 or inp > len(task):
            print("Invalid task number!")
            return

        deleted = task.pop(inp - 1)

        save_task(task)

        print(f"task deleted {deleted['Task']}")

    except ValueError:
        print("Please enter a valid number!")


def main():
    task = load_task()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(task)

        elif choice == "2":
            view_task(task)

        elif choice == "3":
            mark_done(task)

        elif choice == "4":
            delete(task)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()