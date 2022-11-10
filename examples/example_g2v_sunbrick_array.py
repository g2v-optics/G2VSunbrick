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

from g2v_sunbrick import G2VSunbrickArray

SUNBRICK_COM_PORT = "COM8"	## Windows port name convention
# SUNBRICK_COM_PORT = "/dev/ttyACM0"	## Linux port name convention

def example_initialize():
	'''
	Create a serial object to communicate to the Sunbrick Array
	and print out the ID and port name of the Master Brick
	and the IDs of all Sunbricks in the array
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	array = G2VSunbrickArray(serial_obj)

	print("Master Sunbrick {id} connected to port {port}".format(id=array.master_id, port=serial_obj.port))

	print("Array consists of {c} Sunbricks".format(c=array.brick_count))

	for brick_id in array.brick_ids:
		print("Sunbrick {id} is part of the array".format(id=brick_id))

	serial_obj.close()

def example_load_spectrum():
	'''
	Load a spectrum into the SunbrickArray from a file and then turn it off after 10 seconds.
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	array = G2VSunbrickArray(serial_obj)

	spectrum_file_name = 'test.spectrum'

	array.set_spectrum(os.path.join(os.getcwd(), spectrum_file_name))
	print("Finished loading {sf} into Array".format(sf = spectrum_file_name))

	time.sleep(10)
	array.turn_off()
	print("Turned off all LEDs in Array")

	serial_obj.close()

def example_save_spectrum():
	'''
	Get the current spectrum from a SunbrickArray and save it to a file
	'''
	serial_obj = serial.Serial(SUNBRICK_COM_PORT)

	array = G2VSunbrickArray(serial_obj)

	spectrum_file_name = "saved.spectrum"

	spectrum_data = array.get_spectrum()

	with open(os.path.join(os.getcwd(), spectrum_file_name), 'w') as f:
		json.dump(spectrum_data, f)

	print("Spectrum data from Array has been saved to {sf}".format(sf=spectrum_file_name))

	serial_obj.close()

if __name__=="__main__":
	example_initialize()
	time.sleep(5)
	example_load_spectrum()
	time.sleep(5)
	example_save_spectrum()