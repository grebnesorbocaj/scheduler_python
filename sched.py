class sched_item:
	def __init__(self, title, time):
		self.title = title
		self.time = time
		self.detail = "To Do!"

	def update_time(self, new_time):
		self.time = new_time
		print("Time is now %s" %self.time)

	def update_title(self, new_title):
		self.title = new_title
		print("Title is now %s" %self.title)

	def update_detail(self, new_detail):
		self.detail = new_detail
		print("Detail regarding %s,\n~~~~~%s" %(self.title, self.detail))

	def __str__(self):
		return self.time, self.title, self.detail

	def __repr__(self):
		return self.time, self.title, self.detail

schedule = []

def time_return(item):
	return item.time

def add_sched_item():
	new_title = input("What do you want to do? ")
	new_time = input("What time will you do that? ")
	new_sched_item = sched_item(new_title, new_time)
	schedule.append(new_sched_item)
	schedule.sort(key=time_return)
	
add_sched_item()
until = True
while(until):
	


	action = input("\nWhat action do you want to take? View, Add, Change\n      ")
# 	if not ((action.lower() != 'view') or (action.lower() != 'add') or (action.lower() != 'change')):
# 		print("Please enter a valid command!! ~~~~~~~")
# 		continue
	if action.lower() == 'view':
		print("Current Schedule")
		for timed_item in schedule:
			print('{0:7} > {1:10} > {2:30}'.format(timed_item.time,timed_item.title,timed_item.detail))
	elif action.lower() == 'add':
		add_sched_item()
	elif action.lower() == 'change':
		to_change = input("Change time of which item? ")
		new_time = input("What do you want the new time to be? ")
		for time_item in schedule:
			if time_item.time == to_change:
				time_item.update_time(new_time)



	
