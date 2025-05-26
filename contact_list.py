# Contact List 

contacts = {}


op = int(input("Enter what do you want to do :\n1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Quit : \n"))

while op != 4:
	if op == 1 :
		name = input("Enter the name : ")
		number = input("Enter the number : ")
		contacts.update({name : number})
	
	elif op == 2:
		name = input("Enter the name of the contact you want to delete : ")
		if name in contacts :
			contacts.pop(name)
		else :
			print("The contact ", name, " is not in the contacts ! ")
	
	elif op == 3 :
		name = input("Enter the name of the contact you want to Search : ")
		if name in contacts:
			print(contacts[name])
		else :
			print("The contact ", name, " is not present in the contacts ! ")
	elif op == 4:
		break
	else :
		print("Please enter the right option ! ")
	print("Contact list : ")
	
	for i, j in contacts.items():
		print("Name : ", i ,"\tnumber : ",j)

	op = int(input("Enter what do you want to do :\n1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Quit : \n"))
	
		






