#!/usr/bin/env python

'''
Copyright 2022 G2V Optics

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
	 this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
	 this list of conditions and the following disclaimer in the documentation 
	 and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.
'''

import os
import sys
import serial
import time
import json

from g2vsunbrick import G2VSunbrick

SUNBRICK_COM_PORT = "COM3"	## Windows port name convention
# SUNBRICK_COM_PORT = "/dev/ttyACM0"	## Linux port name convention

def example_initialize():
	'''
	Create a serial object to communicate to the Sunbrick
	and print out the ID and port name
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	brick = G2VSunbrick(serial_obj)

	print("Sunbrick {id} connected to port {port}".format(id=brick.brick_id, port=serial_obj.port))

	serial_obj.close()


def example_channel_control():
	'''
	Get the number of channels in the Sunbrick and loop through them all
	in order to set them to 0 if they are not already 0.
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	brick = G2VSunbrick(serial_obj)

	print("Sunbrick {id} has {nn} nodes and {cn} channels".format(id=brick.brick_id, nn=brick.node_count, cn=brick.channel_count))

	for channel in brick.channel_list:
		if brick.get_channel_value(channel) != 0:
			brick.set_channel_value(channel, 0)


	serial_obj.close()


def example_temperature():
	'''
	Print out the average temperature of the Sunbrick
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	brick = G2VSunbrick(serial_obj)

	print("Sunbrick {id} has an average temperature of {tmp}°C".format(id=brick.brick_id, tmp=brick.get_avg_temperature()))

	serial_obj.close()


def example_load_spectrum():
	'''
	Load a spectrum into the Sunbrick from a file and then turn it off after 10 seconds.
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	brick = G2VSunbrick(serial_obj)

	spectrum_file_name = 'test.spectrum'

	brick.set_spectrum(os.path.join(os.getcwd(), spectrum_file_name))
	print("Finished loading {sf} into Sunbrick {id}".format(id=brick.brick_id, sf = spectrum_file_name))

	time.sleep(10)
	brick.turn_off()
	print("Turned off all LEDs in Sunbrick {id}".format(id=brick.brick_id))

	serial_obj.close()


def example_save_spectrum():
	'''
	Get the current spectrum from a Sunbrick and save the file
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	brick = G2VSunbrick(serial_obj)

	spectrum_file_name = "saved.spectrum"

	spectrum_data = brick.get_spectrum()

	with open(os.path.join(os.getcwd(), spectrum_file_name), 'w') as f:
		json.dump(spectrum_data, f)

	print("Spectrum data from Sunbrick {id} has been saved to {sf}".format(id=brick.brick_id, sf=spectrum_file_name))

	serial_obj.close()


if __name__=="__main__":
	example_initialize()
	time.sleep(5)
	example_channel_control()
	time.sleep(5)
	example_temperature()
	time.sleep(5)
	example_load_spectrum()
	time.sleep(5)
	example_save_spectrum()