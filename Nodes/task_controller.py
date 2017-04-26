#!/usr/bin/env python
import rospy
import shlex
import subprocess
import roslaunch
from std_msgs.msg import Int8

gate_status = 0
pathfinder_status = 0
channel_status = 0


def gate_task_callback(msg):
    global gate_status 
    gate_status = msg.data
    rospy.loginfo(msg)

def pathfinder_task_callback(msg):
    global pathfinder_status
    pathfinder_status = msg.data
    rospy.loginfo(msg)

def channel_task_callback(msg):
    global channel_status
    channel_status = msg.data
    rospy.loginfo(msg)

def task_controller():
	#initialize task controller as a node so that it can receive task statuses	
	rospy.init_node("task_controller", anonymous=True)
	
	#declare that the variables below are the same gloabl variables as above
	global gate_status
	global pathfinder_status
	global channel_status

	#establish subscribers for the task statuses
	rospy.Subscriber("gate_task/status", Int8, gate_task_callback)
	rospy.Subscriber("pathfinder_task/status", Int8, pathfinder_task_callback)
	rospy.Subscriber("channel_task/status", Int8, channel_task_callback)
	
	#declare lists to be iterated
	args = ['rosrun auv gate_task_node.py', 'rosrun auv pathfinder_task_node.py', 'rosrun auv channel_task_node.py']
	flags = [gate_status, pathfinder_status, channel_status]
	
	#run arguments stored in command_line, terminates when subscriber recieves termination status from task nodes
	for j,proc_val in enumerate(args):
		process = subprocess.Popen(proc_val, shell=True)
		while flags[j] != 3:
			continue				
		process.kill()

	rospy.spin()
if __name__ == '__main__':
   try:
        task_controller()
   except rospy.ROSInterruptException:
           pass

