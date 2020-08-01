#!/usr/bin/env python
import actionlib
import rospy

from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from math import radians, degrees
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# task: define goal location for the robot, send these goal locations
# to the navigation stack to execute the mission and make the robot
# navigate towards the goal

def moveToGoal(x_goal, y_goal):
    pass
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base action server.")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position = Point(x_goal, y_goal, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1

    rospy.loginfo("Sending goal location...")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(60))

    if(ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("Goal reached.")
        return True
    else:
        rospy.loginfo("Failed to reach goal.")
        return False

if __name__ == '__main__':
    try:
        rospy.init_node('navigate_goal_node', anonymous=False)
        x_goal = -2
        y_goal = 4
        print("Start navigation")
        moveToGoal(x_goal, y_goal)
        rospy.spin()
    except ROSInterruptException:
        rospy.loginfo("Node terminated.")
