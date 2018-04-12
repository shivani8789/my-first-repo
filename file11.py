import Errors

try:
	nam=(input("name u want to give"))
	if len(nam)>20:
		raise name
	else:
		nam=input("enter name")
		print(nam)
except Errors.name:
	raise
try:
	age=int(input("enter age"))
	if len(age)>2:
		raise age
	else:
		print(age)
except Errors.age:
	raise
try:
	a=("please enter 5 sports name")
	list=[]
	if len(a)>5:
		raise list
	else:
		list.append(a)
		print(list)
except Errors.list:
	raise
try:
	sport=input("give name of sport")
	if sport==list:
		print(good)
	else:
		raise sport
except Errors.sport:
	raise
	
	