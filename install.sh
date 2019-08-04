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

echo "reboot to start service"

echo "program configuration completed"
