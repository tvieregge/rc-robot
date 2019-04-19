#!/usr/bin/env python

import numpy as np
from itertools import chain
import time
import rospy
from std_msgs.msg import String
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Twist
import math

from sensor_msgs.msg import LaserScan

GOAL_DEPTH = 0.5
ROBOT_SPEED = 0.5 # m/s
ROBOT_ANGULAR_SPEED = 1 # radians/s
ANGLE_DEAD_ZONE = 0.25 # radians

MAX_X = 0.5
MIN_X = -0.5
MAX_Y = 0.9
MIN_Y = 0.1

pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

def callback(scan):
   min_depth = scan.range_max
   current_angle = scan.angle_min
   min_range_angle = 0

   for i in scan.ranges:
     if i < min_depth and i > scan.range_min:
       min_depth = i
       min_range_angle = current_angle
     current_angle += scan.angle_increment

   print ("min_depth:       " + str(min_depth))
   print ("min_range point: " + str(min_range_angle))

   vel_msg = Twist()
   if min_depth > GOAL_DEPTH and min_depth != scan.range_max:
       vel_msg.linear.x = ROBOT_SPEED
   if min_range_angle > ANGLE_DEAD_ZONE:
       vel_msg.angular.z = -ROBOT_ANGULAR_SPEED
   elif min_range_angle < -ANGLE_DEAD_ZONE:
       vel_msg.angular.z = ROBOT_ANGULAR_SPEED
   else:
       vel_msg.angular.z = 0

   print ("vel_msg: " + str(vel_msg))

   pub.publish(vel_msg)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('camera/depth_registered/points', PointCloud2, callback)
    rospy.Subscriber('depth_scan', LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()