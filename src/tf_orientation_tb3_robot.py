#!/usr/bin/env python

# task: subscribe to odom topic and get the position and orientation of the robot
import rospy
from nav_msgs.msg import Odometry
import tf
import math

def odomCallback(odom_msg):
    x_pos = odom_msg.pose.pose.position.x
    y_pos = odom_msg.pose.pose.position.y
    qx = odom_msg.pose.pose.orientation.x
    qy = odom_msg.pose.pose.orientation.y
    qz = odom_msg.pose.pose.orientation.z
    qw = odom_msg.pose.pose.orientation.w
    rpy = tf.transformations.euler_from_quaternion([qx,qy,qz,qw])
    yaw = math.degrees(rpy[2])
    print("X: %f\tY: %f\tOrientation: %f" % (x_pos, y_pos, yaw))

if __name__ == '__main__':
    try:
        rospy.init_node('turtlebot_orientation_node', anonymous=True)

        position_topic = '/odom'
        pose_subscriber = rospy.Subscriber(position_topic, Odometry, odomCallback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
