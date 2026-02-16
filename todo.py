tasks = []

while True:
	print("\n=== TO-DO LIST MENU ===")
	print("1.View Task")
	print("2.Add Task")
	print("3.Delete Task")
	print("4.Exit")

	choice = input("Enter your choice: ")
	
	if choice == "1":
		if not tasks:
			print("Task Not Available.")
		else:
			for i, task in enumerate(tasks):
				print(f"{i+1}. {task}")
	
	elif choice == "2":
		new_task = input("Enter New Task: ")
		tasks.append(new_task)
		print("Task added")
	
	elif choice == "3":
		task_num = int(input("Enter Task Number To Delete: "))
		if 0 < task_num < len(tasks):
			removed = tasks.pop(task_num - 1)
			print("Removed Task {removed}")

	elif choice == "4":
		print("Exiting TO-DO LIST MENU")
		break

	else:
		print("Invalid choice")