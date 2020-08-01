#!/usr/bin/env python
import math
import tf

# task: Interconvert Euler angles and Quartenion using tf functions
roll = math.radians(30)
pitch = math.radians(45)
yaw = math.radians(90)

quat = tf.transformations.quaternion_from_euler(roll,pitch,yaw)

print("Conversion from rpy(in radians):(%f,%f,%f)\n\tto quaternion:(%f,%f,%f,%f)" %
    (roll, pitch, yaw, quat[0], quat[1], quat[2], quat[3]))

rpy = tf.transformations.euler_from_quaternion(quat)

print("Conversion from quaternion:(%f,%f,%f,%f)\n\tto rpy(in degrees):(%f,%f,%f)" %
    (quat[0], quat[1], quat[2], quat[3], math.degrees(rpy[0]), 
    math.degrees(rpy[1]), math.degrees(rpy[2])))
