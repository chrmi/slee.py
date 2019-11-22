install:
	sudo apt-get update && apt-get install build-essential git python-dev python-pip python-imaging python-smbus vlc libjpeg-dev zlib1g-dev python-pil
	sudo pip install -r requirements.txt
	printf "\n\n(setting up service -- reboot may be required)"
	sudo chmod 644 sleepy.service
	sudo cp sleepy.service /lib/systemd/system/
	sudo systemctl daemon-reload && sudo systemctl enable sleepy.service
	printf "\n\n*** follow instructions at: https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi/usage\n\n"

run:
	sudo python sleepy/sleepy.py
