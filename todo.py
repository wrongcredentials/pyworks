import json
import sys

def read():
	try:
		with open("data.json","r") as f:
			d = json.load(f)
			if d:
				count = 1
				for i in d:
					result = """{}. {}""".format(count, i)
					print(result)
					count += 1
			else:
				print(">> File is empty. Start adding new tasks using -a")
	
	except ValueError:
		print(">> ERROR: Cannot read file. Use -a to create new")


def add(task):	
	try:
		with open("data.json","r") as f:
			d = json.load(f)
	
	except:
		print(">> WARNING: File is broken or does not exist. Creating new now... Done")
		d = []
	
	finally:
		with open("data.json","w") as f:
  			d.append(task)
  			json.dump(d, f)


def remove(id):
	if id > 0:
		with open("data.json","r+") as f:
			d = (json.load(f))
			try:
				del d[id-1]
				with open("data.json", "w") as f:
					json.dump(d, f)
		
			except IndexError:
				print(">> ERROR: No task with index", id)
	else:
		print(">> ERROR: Invalid index")	


def up(id):
	if id > 1:
		with open("data.json","r") as f:
			try:
				d = (json.load(f))	
				d[id-2], d[id-1] = d[id-1], d[id-2]	
				with open("data.json", "w") as f:
					json.dump(d, f)			
	
			except IndexError:
				print(">> ERROR: No task with index", id)

	else:
		print(">> ERROR: Invalid index")		


def down(id):
	try:
		with open("data.json","r") as f:
			d = (json.load(f))
			if id > 0 and id < len(d):
				d[id], d[id-1] = d[id-1], d[id]	
				with open("data.json", "w") as f:
					json.dump(d, f)
			else:
				print(">> ERROR: Invalid index")
	
	except IndexError:
		print(">> ERROR: No task with index", id)


def help():
	text = """      Simple To Do List v.1.0.1:
-l              receieve a to do list
-a task_name	add new task to list 
-r task_id      remove task from list
-u task_id      raise a priority of task
-d task_id      low a priority of task
-h              help (you already see it)"""
	print(text)


def main(option, value):
	try:
		task = " ".join(value)

		if option == "-l" or option == "list":
			read()			

		elif option == "-a" or option == "add":
			if task:
				add(task)
			else:
				print(">> ERROR: You have to name the task when use 'add'")

		elif option == "-r" or option == "remove":
			remove(int(task))

		elif option == "-u" or option == "up":
			up(int(task))


		elif option == "-d" or option == "down":
			down(int(task))

		else:
			help()	

	except FileNotFoundError:
		print(">> ERROR: You don't have active to do list. Create new using -a")
	
	except ValueError:
		print(">> ERROR: You have to pass the index of task when use '" + str(option) + "'")

try:
	main(sys.argv[1], sys.argv[2:])
except:
	print(">> ERROR: Unknown command. Use -h for help")