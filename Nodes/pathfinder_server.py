#! /usr/bin/env python

import rospy
import actionlib
import auv.msg
from geometry_msgs.msg import Twist
from visualizer import visualizer

class PathfinderAction(object):
	_feedback = auv.msg.pathfinderFeedback()
	_result = auv.msg.pathfinderResult()
	
	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, auv.msg.pathfinderAction, execute_cb=self.execute_cb, auto_start = False)
		
		self._as.start()
		
		self.movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
		self.motion  = Twist()

	def execute_cb(self, goal):
		
		r = rospy.Rate(10)
		success = True
		status = 0
		viz_1 = visualizer(1)
		
		while status != goal:

			if self._as.is_preempt_requested():
				rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
				break
			
			line_check = viz_1.detectLine("orange")
		    if line_check == -1:
		    	if status == 1:
		        	status = 3
		            continue
		        else:   
		            continue

		    #if the line is centered to the AUV, continue forward
		    elif line_check == 0:
		        status = 1
		        self.motion.linear.x = 1.0
		        self.motion.linear.y = 0.0
		        self.motion.linear.z = 0.0
		        self.motion.angular.x = 0.0
		        self.motion.angular.y = 0.0
		        self.motion.angular.z = 0.0

		    #if the line curves left, AUV turns left
		    elif line_check == 1:
		        status = 1
		        self.motion.linear.x = 1.0
		        self.motion.linear.y = 0.0
		        self.motion.linear.z = 0.0
		        self.motion.angular.x = 0.0
		        self.motion.angular.y = 0.0
		        self.motion.angular.z = 0.050

		    #if the line curves right, AUV turns right
		    elif line_check == 2:
		        status = 1
		        self.motion.linear.x = 1.0
		        self.motion.linear.y = 0.0
		        self.motion.linear.z = 0.0
		        self.motion.angular.x = 0.0
		        self.motion.angular.y = 0.0
		        self.motion.angular.z = -0.050
		    
		    else:
		        continue
		    
		    #publish AUV motion changes
		    rospy.loginfo(self.motion)
		    movement.publish(self.motion)
		    r.sleep()

		#after follwing line, AUV stops inorder to process next task
		self.motion.linear.x = 0.0
		self.motion.linear.y = 0.0
		self.motion.linear.z = 0.0
		self.motion.angular.x = 0.0
		self.motion.angular.y = 0.0
		self.motion.angular.z = 0.0
		
		self._feedback.end_goal_status = status
		#motion.angular.z = 0.0
		rospy.loginfo(self.motion)
		#movement.publish(motion)
		r.sleep()

		if success:
			self._result.current_goal_status = self.feedback.end_goal_status
			rospy.loginfo("%s succeeded" %self._action_name)			
			rospy.loginfo(self.motion)
			self.movement.publish(self.motion)
			viz_1.__del__()
			self._as.set_succeeded(self.result)


if __name__ == '__main__':
	rospy.init_node('pathfinder')
	server = PathfinderAction(rospy.get_name())
	rospy.spin()



		
