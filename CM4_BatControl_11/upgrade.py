#
# This python3 module will update the High Fuse on the ATTiny88 to 0xdf
#  which will disable the Brown Out Detector (BOD) and allow the ATTiny
#  to run with Vcc down to less than 2V
# The command line will also update the hex file to version 0x11
#
# Save this file to a USB stick as /.connectbox/update.py
# Plugging the stick into the RPi Connectbox will change the fuse, write
#  the output to file update.log and remove this file.
#
# Written 02/07/22 by DorJamJr


import subprocess
import os

# run the avrdude command to make high fuse = 0xdf and capture output
command = "sudo avrdude -P /dev/spidev0.0 -c linuxspi -p t88 -U flash:w:CM4_BatControl_11.ino.hex -U hfuse:w:0xdf:m"
output = subprocess.getoutput(command)	# run the avrdude command

# write the output text to file update.log so we have a record
logfile = open("AVR_upgrade.log", "w")
logfile.write(output)
logfile.close()

# delete this file
os.remove("upgrade.py") 