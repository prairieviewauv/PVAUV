#!/usr/bin/env python
import rospy
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

def task_manager():
	rospy.init_node("task_manager", anonymous=True)

	rospy.Subscriber("gate_task/status", Int8, gate_task_callback)
	rospy.Subscriber("pathfinder_task/status", Int8, pathfinder_task_callback)
	rospy.Subscriber("channel_task/status", Int8, channel_task_callback)

	global gate_status
	global pathfinder_status
	global channel_status

	package = "auv"

	executable = "gate_task_node.py"
	node = roslaunch.core.Node(package, executable)
	try:
		process1 = launcher.launch(node)
	except roslaunch.RLException as e:
		rospy.logerr(e.message)
	flag1 = gate_status
	#rospy.sleep(5)
	while flag1 != 2:
		continue
	process1.stop()
		

	executable = "pathfinder_task_node.py"
	node = roslaunch.core.Node(package, executable)
	try:
		process2 = launcher.launch(node)
	except roslaunch.RLException as e:
		rospy.logerr(e.message)
	flag2 = pathfinder_status
	while flag2 != 3:
		continue
	#rospy.sleep(5)
	process2.stop()	    

		
if __name__ == '__main__':
   launcher = roslaunch.scriptapi.ROSLaunch()
   launcher.start()
   try:
        task_manager()
   except rospy.ROSInterruptException:
           pass

