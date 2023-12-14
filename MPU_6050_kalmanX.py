# -*- coding: utf-8 -*-

from mpu6050 import mpu6050
import sys
sys.path.append('/usr/lib/python3/dist-packages')
import time

mpu = mpu6050(0x68)  

while True:
    accel_data = mpu.get_accel_data()
    gyro_data = mpu.get_gyro_data()
    temp = mpu.get_temp()

    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))

    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))

    time.sleep(1)

