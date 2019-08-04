import os #importing os to give commands to os
import getpass

user = getpass.getuser()

#set method to set wallpapers
def set():

	print("setting up new wallpaper")

	#linux command to set wallpaper
	os.system("gsettings set org.gnome.desktop.background picture-uri file:////home/"+user+"/Automatic_Wallpaper_Changer/Wallpapers/walli.png")

	print("done with new wallpaper")