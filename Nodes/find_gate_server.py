#! /usr/bin/env python

import rospy
import actionlib
import auv.msg
from geometry_msgs.msg import Twist
from visualizer import visualizer

class GateAction(object):
	_feedback = auv.msg.find_gateFeedback()
	_result = auv.msg.find_gateResult()
	
	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, auv.msg.find_gateAction, execute_cb=self.execute_cb, auto_start = False)
		
		self._as.start()
		
		self.movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
		self.motion  = Twist()
		rospy.loginfo("initialized")

	def execute_cb(self, goal):
		rospy.loginfo("diagnostics...")
		r = rospy.Rate(10)
		success = True
		status = 1
		counter = 0
		viz_0 = visualizer(0)
		
		while status != goal:
			if self._as.is_preempt_requested():
				rospy.loginfo('%s: Preempted' % self._action_name)
				self._as.set_preempted()
				success = False
				break

			if viz_0.detectGateLeft("orange"):
				if viz_0.detectGateRight("orange"):
					self.motion.linear.x = 1.0
					self.motion.linear.y = 0.0
					self.motion.linear.z = 0.0
					self.motion.angular.x = 0.0
					self.motion.angular.y = 0.0
					self.motion.angular.z = 0.0

					status = 2
					continue		        


				#turns the AUV left 45 deg in case right leg is not found
				else:
					self.motion.linear.x = 0.0
					self.motion.linear.y = 0.0
					self.motion.linear.z = 0.0
					self.motion.angular.x = 0.0
					self.motion.angular.y = 0.0
					self.motion.angular.z = 0.785
					self.movement.publish(self.motion)

				#motion.angular.z = 0.0
				rospy.loginfo(self.motion)
				#movement.publish(motion)
				rate.sleep()
				continue

			#turns the AUV right 45 deg in case left leg not found
			else:
				self.motion.linear.x = 0.0
				self.motion.linear.y = 0.0
				self.motion.linear.z = 0.0
				self.motion.angular.x = 0.0
				self.motion.angular.y = 0.0
				self.motion.angular.z = 0.785
				counter +=1

				if counter > 6:
					self.motion.linear.x = 1.0
					self.motion.linear.y = 0.0
					self.motion.linear.z = 0.0
					self.motion.angular.x = 0.0
					self.motion.angular.y = 0.0
					self.motion.angular.z = 0.0
					counter = 0
			
			self._feedback.end_goal_status = status
			#motion.angular.z = 0.0
			rospy.loginfo(self.motion)
			#movement.publish(motion)
			r.sleep()
			rospy.spin()
		if success:
			self._result.current_goal_status = self.feedback.end_goal_status
			rospy.loginfo("%s succeeded" %self._action_name)			
			rospy.loginfo(self.motion)
			self.movement.publish(self.motion)
			viz_0.__del__()
			self._as.set_succeeded(self.result)

if __name__ == '__main__':
	rospy.init_node('find_gate')
	server = GateAction(rospy.get_name())
	rospy.spin()



		
