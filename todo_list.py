
# ------------------------------
# To-Do List Management System
# ------------------------------

# List to store tasks
tasks = []   # Each task = {"id": x, "task": "text", "status": "Pending"}

# --------------------------------------
# 1. Add Task
# --------------------------------------
def add_task(tasks):
    if len(tasks) >= 8:
        print("❌ Maximum limit reached (8 tasks). Cannot add more.")
        return

    task_desc = input("Enter task description: ")

    task_id = len(tasks) + 1  # Unique ID based on position

    new_task = {
        "id": task_id,
        "task": task_desc,
        "status": "Pending"
    }

    tasks.append(new_task)
    print("✔ Task added successfully!")


# --------------------------------------
# 2. View Tasks
# --------------------------------------
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n----- Your Tasks -----")
    for t in tasks:
        print(f"ID: {t['id']} | Task: {t['task']} | Status: {t['status']}")
    print("----------------------\n")


# --------------------------------------
# 3. Update Task
# --------------------------------------
def update_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return

    task_id = int(input("Enter Task ID to update: "))

    for t in tasks:
        if t["id"] == task_id:
            new_desc = input("Enter new description: ")
            t["task"] = new_desc
            print("✔ Task updated successfully!")
            return

    print("❌ Task ID not found.")


# --------------------------------------
# 4. Mark Task as Done
# --------------------------------------
def mark_done(tasks):
    if not tasks:
        print("No tasks available.")
        return

    task_id = int(input("Enter Task ID to mark as Done: "))

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Done"
            print("✔ Task marked as Done!")
            return

    print("❌ Task ID not found.")


# --------------------------------------
# 5. Delete Task
# --------------------------------------
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    task_id = int(input("Enter Task ID to delete: "))

    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)

            # Reassign IDs to maintain sequence
            for idx, task in enumerate(tasks, start=1):
                task["id"] = idx

            print("✔ Task deleted successfully!")
            return

    print("❌ Task ID not found.")


# --------------------------------------
# 6. Menu Function
# --------------------------------------
def menu():
    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# Start the Program
menu()
