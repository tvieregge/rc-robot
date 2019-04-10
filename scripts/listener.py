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
    
GOAL_DEPTH = 0.5
ROBOT_SPEED = 0.5 # m/s
ROBOT_ANGULAR_SPEED = 1 # radians/s
ANGLE_DEAD_ZONE = 0.25 # radians

MAX_X = 0.5
MIN_X = -0.5
MAX_Y = 0.9
MIN_Y = 0.1    
    
pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)    
    
def callback(data):    
   start_time = time.time()
   minimum_depth = float("inf")    
   closest_x = 0    
   closest_y = 0    

   # use numpy to do things quickly
   # points_array = np.fromiter(pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=True), dtype=np.float32)
   # points_array = np.fromiter(chain.from_iterable(pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=False)), dtype=np.float32)
   cloud_points = list(pc2.read_points(data, skip_nans=False, field_names = ("x", "y", "z")))
   

   # print(points_array)



   # for p in pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=True):    
       # if MIN_X > p[0] or MAX_X < p[0] or MIN_Y > p[1] or MAX_Y < p[1]:    
           # continue    
    # 
       # if p[2] < minimum_depth:    
           # minimum_depth = p[2]    
           # closest_x = p[0]    
           # closest_y = p[1]    
   # angle = math.atan2(closest_x, minimum_depth)    
    # 
   # vel_msg = Twist()    
   # if minimum_depth > GOAL_DEPTH and minimum_depth != float("inf"):    
       # vel_msg.linear.x = ROBOT_SPEED    
    # 
   # if angle > ANGLE_DEAD_ZONE:    
       # vel_msg.angular.z = -ROBOT_ANGULAR_SPEED    
   # elif angle < -ANGLE_DEAD_ZONE:    
       # vel_msg.angular.z = ROBOT_ANGULAR_SPEED    
   # else:    
       # vel_msg.angular.z = 0    
    
   # pub.publish(vel_msg)    
   end_time = time.time()
   print "time elapsed for a loop:" + str(end_time - start_time)

def listener():    
    
    # In ROS, nodes are uniquely named. If two nodes with the same    
    # name are launched, the previous one is kicked off. The    
    # anonymous=True flag means that rospy will choose a unique    
    # name for our 'listener' node so that multiple listeners can    
    # run simultaneously.    
    rospy.init_node('listener', anonymous=True)    
    
    # rospy.Subscriber('camera/depth_registered/points', PointCloud2, callback)    
    rospy.Subscriber('throttled_points', PointCloud2, callback)    
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
