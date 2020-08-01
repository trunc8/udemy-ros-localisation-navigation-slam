#!/usr/bin/env python
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('frame_a_frame_b_listener_node')

    listener = tf.TransformListener()

    listener.waitForTransform('/frame_a', '/frame_b', rospy.Time(),
        rospy.Duration(4.0))
    rate = rospy.Rate(1.0)

    while (not rospy.is_shutdown()):
        try:
            (trans, quat) = listener.lookupTransform(
                '/frame_a', '/frame_b', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException,
            tfExtrapolationException):
            continue
        rpy = tf.transformations.euler_from_quaternion(quat)

        print("Transformation between frame_a and frame_b detected")
        print("Translation vector: (%f,%f,%f)" % (trans[0],trans[1],
            trans[2]))
        print("Rotation angles: roll=%f, pitch=%f, yaw=%f" % (rpy[0],
            rpy[1], rpy[2]))

        rate.sleep()
