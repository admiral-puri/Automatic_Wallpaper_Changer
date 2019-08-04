import getpass

#main metord for managing the prefrences
def menu():

	#printing the menu
	print("\n########### MENU #############\n")
	print("see prefrences         1")
	print("add prefrence          2")
	print("remove prefrence       3")
	print("exit               anything else")

	#getting the choice
	choice = int(input("now enter choice\n"))

	#selecting "see prefrence"
	if choice is 1:	

		#reading prefrences
		file_object = open('/home/'+user+'/Automatic_Wallpaper_Changer/prefrences.txt','r')
		prefrences = file_object.readline()
		file_object.close()
		prefrences_list = prefrences.split()

		print("************** prefrences ***************")

		#printing prefrences
		for i in prefrences_list:

			print(i)

		print("*****************************************")

		return True

	#selecting "add prefrence"
	if choice is 2:

		#reading prefrencess
		file_object = open('/home/'+user+'/Automatic_Wallpaper_Changer/prefrences.txt','r')
		prefrences = file_object.readline()
		file_object.close()
		prefrences_list = prefrences.split()

		#getting new prefrence to add
		new_prefrence = str(input("enter new prefrence to be added\n"))

		#checking it already exists
		for i in prefrences_list:

			if i == new_prefrence:

				return True

		#opeaning the prefrences file in append mode
		file_object = open('/home/'+user+'/Automatic_Wallpaper_Changer/prefrences.txt','a')

		# appending the file
		file_object.write(" "+new_prefrence)

		file_object.close()

		return True

	# selecting the "remove prefrence"
	if choice is 3:

		#reading the prefrences
		file_object = open('/home/'+user+'/Automatic_Wallaper_Changer/prefrences.txt','r')
		prefrences = file_object.readline()
		file_object.close()
		prefrences_list = prefrences.split()


		#removing the desired prefrence
		prefrences_list.remove(input("enter the prefrence to be removed\n"))

		#opeaning the prefrence file in write mode
		input_file = open('prefrences.txt','w')

		# adding the list
		for i in prefrences_list:

			print("added ",i)

			input_file.write(' '+i)

		input_file.close()

		return True





	return False

user = getpass.getuser()

loop_now = True

while loop_now is True:

	try:
		loop_now = menu()

	except Exception as ex:

		print(ex)
