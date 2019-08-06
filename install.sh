#!/bin/bash


echo "thanks for downloading "
echo "installing"

cd ../

user=$(whoami)
echo $user
sudo cp -r Automatic_Wallpaper_Changer  /home/$user/

crontab -l > new_cron
echo "@reboot /home/"$user"/Automatic_Wallpaper_Changer/executer.sh" > new_cron
crontab new_cron

echo "main installation is complete"
echo "now installing python dependencies"


pip3 getpass
pip3 random  
pip3 install requests
pip3 install UnsplashSearch 
pip3 install os


echo "reboot to start service"
echo "program configuration completed"
