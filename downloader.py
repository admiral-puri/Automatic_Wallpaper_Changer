import getpass
import random  #importing random to get random prefrence seleted
import requests # requests to download wallpaper
import wallpaper_setter # script to set wallpaper
from unsplash_search import UnsplashSearch  #unsplash api to search and get images


#main function which selects the image and downloads it
def main(key,arg):

	print("@ main")

	#initialization of unsplash object
	unsplash = UnsplashSearch(key)

	#searching image from unsplash api
	img = unsplash.search_photo(arg)

	# downloading the image
	r = requests.get(img['img'])

	#writing the wallpaper from buffer to harddisk
	with open("/home/"+user+"/Automatic_Wallpaper_Changer/Wallpapers/walli.png",'wb') as f:

		f.write(r.content)

	#call to set wallpaper
	wallpaper_setter.set()


#read function to read prefrences
def read():

	print("@ read")

	#opeaning the file containing authorization key
	key_file_object = open('/home/'+user+'/Automatic_Wallpaper_Changer/key.txt','r')

	#reading the key
	key = key_file_object.readline()

	#opeaning the prefrences file
	file_object = open('/home/'+user+'/Automatic_Wallpaper_Changer/prefrences.txt','r')

	#reading the prefrences
	prefrences = file_object.readline()

	#getting list of prefrences
	prefrences_list = prefrences.split()

	#passing key and random prefrence
	main(key,prefrences_list[int(random.uniform(0,len(prefrences_list)))])

	
#call to read function

user = getpass.getuser()
read()
