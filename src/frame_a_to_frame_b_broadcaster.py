#!/usr/bin/env python
import roslib
import rospy
import tf
import time
import math

if __name__ == '__main__':
    rospy.init_node('frame_a_frame_b_broadcaster_node')

    time.sleep(2)

    broadcaster = tf.TransformBroadcaster()

    while (not rospy.is_shutdown()):
        translation = (1,2,3)
        rotation_quaternion = tf.transformations.quaternion_from_euler(0.2,0.3,0.1)
        current_time = rospy.Time.now()

        broadcaster.sendTransform(
            translation,
            rotation_quaternion,
            current_time,
            'frame_b', 'frame_a'
        )
        time.sleep(0.5)

    rospy.spin()
