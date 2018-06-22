#!/usr/bin/env python

import rospy
import roslib

rospy.init_node("driver")

def constants():
	rospy.set_param("Host", "http://localhost:8080")
	rospy.set_param("TeamID", "ASV")
	rospy.set_param("Course", "courseA")


constants()


#rospy.set_param("Challenge", "return")