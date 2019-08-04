#!/bin/bash

# this script fires download.py and runs our service twice an hour

user=$(whoami)

while [ true ]
do

python3 /home/$user/Automatic_Wallpaper_Changer/downloader.py

sleep 1800

done

