#! /usr/bin/env python

import rospy
import actionlib
import auv.msg


def find_gate_client():
	client = actionlib.SimpleActionClient('find_gate', auv.msg.find_gateAction)
	client.wait_for_server()
	
	goal = auv.msg.find_gateGoal(gate_task_completion=2)
	
	client.send_goal(goal)

	client.wait_for_result()

	return client.get_result()

def pathfinder_client():
	client = actionlib.SimpleActionClient('pathfinder', auv.msg.pathfinderAction)
	client.wait_for_server()
	
	goal = auv.msg.pathfinderGoal(pathfinding_task_completion=3)
	
	client.send_goal(goal)

	client.wait_for_result()

	return client.get_result()

def channel_client():
	client = actionlib.SimpleActionClient('channel', auv.msg.channelAction)
	client.wait_for_server()
	
	goal = auv.msg.channelGoal(channel_task_completion=2)
	
	client.send_goal(goal)

	client.wait_for_result()

	return client.get_result()


if __name__=='__main__':
	try:
		rospy.init_node('find_gate_client.py')
		gate_result = find_gate_client()
		rospy.loginfo("Gate finder returned with %d. Starting pathfinder." %gate_result) 
	except rospy.ROSInterruptException:
		rospy.loginfo("Program interrupted before completion")
	
	try:
		rospy.init_node('pathfinder_client.py')
		pathfinder_result = pathfinder_client()
		rospy.loginfo("Pathfinder returned with %d. Starting channel navigation." %pathfinder_result) 
	except rospy.ROSInterruptException:
		rospy.loginfo("Program interrupted before completion")

	try:
		rospy.init_node('channel_client.py')
		channel_result = pathfinder_client()
		rospy.loginfo("Channel returned with %d. Ending mission." %channel_result) 
	except rospy.ROSInterruptException:
		rospy.loginfo("Program interrupted before completion")

