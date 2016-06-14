import os
import glob
import time
import osc

# code modified from: http://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi

# load the OS kernel modules for the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# the device file for the sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        # temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

old_temp = 0

while True:
	temp_c = read_temp()
	print(temp_c)
	print(temp_c-old_temp)
        # send the current temperature out over osc
	osc.Message("/temp",[temp_c]).sendlocal(8889)
        # sends the difference from the last recorded over osc
	osc.Message("/tempdiff",[temp_c-old_temp]).sendlocal(8889)
	old_temp = temp_c
	time.sleep(0.1)
