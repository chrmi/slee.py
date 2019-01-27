install:
	sudo apt-get update && apt-get install build-essential git python-dev python-pip python-imaging python-smbus vlc
	sudo pip install -r requirements.txt
	printf "\n\n*** follow instructions at: https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi/usage\n\n"

run:
	sudo python sleepy.py
