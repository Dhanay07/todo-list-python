file_name = "tasks.txt"

try:
	with open (file_name,"r") as file:
		tasks = file.read().splitlines()
except FileNotFoundError:
	tasks = []

while True:
	print("\nTO-DO LIST MENU")
	print("1. View Task")
	print("2. Add Task")
	print("3. Delete Task")
	print("4. Exit")

	choice = input("Enter your choice: ")

	if choice == "1":
		if not tasks:
			print("No Task Available")
		else:
			for i, task in enumerate(tasks):
				print(f"{i+1}. {task}")
		
	elif choice == "2":
		new_task = input("Enter New Task: ")
		tasks.append(new_task)

		with open(file_name,"w") as file:
			for task in tasks:
				file.write(task + "\n")
		
		print("Task added")

	elif choice == "3":
		task_num = int(input("Enter Task number to Delete: "))
		if 0 < task_num <= len(tasks):
			removed=tasks.pop(task_num - 1)
		
			with open(file_name, "w") as file:
				for task in tasks:
					file.write(task + "\n")
	
			print(f"Removed Task: {removed}")
		else:
			print("Invalid task num")
	
	elif choice == "4":
		print("Exiting")
		break

	else:
		print("Invalid choice")
	
	