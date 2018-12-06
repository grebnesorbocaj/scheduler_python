class sched_item:
	#this object is the main object for the program
	#each sched_item object represents an instance within the Schedule
	#it will include the time, the title, and the details of the instance
	#for example:
	#	I want to read at 09:30
	#	the instance time is 0930
	#	the instance title is read
	#	the instance details are defaulted as To Do, but can be changed to Completed or something else
	def __init__(self, title, time):
		self.title = title
		self.time = time
		self.detail = "To Do!"

	#update the time by calling this method on an instance and set new_time parameter
	#example: this_instance.update_time(new_time)
	def update_time(self, new_time):
		self.time = new_time
		print("Time is now %s" %self.time)

	#update the title by calling this method on an instance and set new_title parameter
	#example: this_instance.update_title(new_title)
	def update_title(self, new_title):
		self.title = new_title
		print("Title is now %s" %self.title)

	#update the details by calling this method on an instance and set new_detail parameter
	#example: this_instance.update_detail(new_detail)
	def update_detail(self, new_detail):
		self.detail = new_detail
		print("Detail regarding %s,\n~~~~~%s" %(self.title, self.detail))


	#the following two are related to print, though I don't understand them
	def __str__(self):
		return self.time, self.title, self.detail

	def __repr__(self):
		return self.time, self.title, self.detail

# I am using this schedule array as the container for all sched_item instances
schedule = []

# this is used to return the time property, used for sorting by time
def time_return(item):
	return item.time

#this is called when choosing to add a new schedule item
def add_sched_item():
	new_title = input("What do you want to do? ")
	new_time = input("What time will you do that? ")
	new_sched_item = sched_item(new_title, new_time)
	schedule.append(new_sched_item)
	schedule.sort(key=time_return)


#this is to change some shed_item instance in the Schedule
#you can change the time or the details, I am too lazy to offer title change
def change_sched_item(time_to_change):
	to_change_what = input("What do you want to change? (Time/Details) \n")
	if to_change_what.lower() == 'time':
		new_time = input("What do you want the new time to be? ")
		for time_item in schedule:
			if time_item.time == time_to_change:
				time_item.update_time(new_time)
				schedule.sort(key=time_return)
	elif to_change_what.lower() == 'details':
		new_detail = input("What do you want the detail to say? \n")
		for time_item in schedule:
			if time_item.time == time_to_change:
				time_item.update_detail(new_detail)

#add the first item to the schedule
add_sched_item()

#loop forever until choosing the quit action
until = True
while(until):
	# ask user what he/she would like to do, and then perform based on input
	action = input("\nWhat action do you want to take? View, Add, Change\n      ")

	#obviously this is to view the schedule
	if action.lower() == 'view':
		print("Current Schedule")
		for timed_item in schedule:
			print('{0:7} > {1:10} > {2:30}'.format(timed_item.time,timed_item.title,timed_item.detail))

	#obiously this is to add a new sched_item instance
	elif action.lower() == 'add':
		add_sched_item()

	#obviously this is to change some sched_item instance
	elif action.lower() == 'change':
		to_change_which = input("Which item do you want to change? (Time of) ")
		change_sched_item(to_change_which)

	#obviously this is to quit
	elif action.lower() == 'quit':
		until = False
