#! /usr/bin/env python

import rospy
import actionlib
import auv.msg
from geometry_msgs.msg import Twist
from visualizer import visualizer

class ChannelAction(object):
	_feedback = auv.msg.channelFeedback()
	_result = auv.msg.channelResult()
	
	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, auv.msg.channelAction, execute_cb=self.execute_cb, auto_start = False)
		
		self._as.start()
		
		self.movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
		self.motion  = Twist()

	def execute_cb(self, goal):
		
		r = rospy.Rate(10)
		success = True
		status = 1
		above_gate=False
		viz_0 = visualizer(0)
		
		while status != goal:

			if self._as.is_preempt_requested():
				rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
				break
            
			if viz_0.detectGateLeft("yellow"):
				if viz_0.detectGateRight("yellow"):
                    #check to see if AUV is above bottom of the channel
                    while not above_gate:
                    	if viz_0.detectGateBottom("yellow")==0:
	                        above_gate=True
	                        self.motion.linear.x = 1.0
	                        self.motion.linear.y = 0.0
	                        self.motion.linear.z = 0.0
	                        self.motion.angular.x = 0.0
	                        self.motion.angular.y = 0.0
	                        self.motion.angular.z = 0.0 
	                        break
                    
				        #If auv is below bottom of channel, AUV ascends
						elif viz_0.detectGateBottom("yellow")==1:
		                	self.motion.linear.x = 0.0
		                    self.motion.linear.y = 0.0
		                    self.motion.linear.z = 1.0
		                    self.motion.angular.x = 0.0
		                    self.motion.angular.y = 0.0
		                    self.motion.angular.z = 0.0
		                    
							rospy.loginfo(self.motion)
		                    self.movement.publish(self.motion)
		                    rate.sleep()
		                        
				        status = 2  
				        rospy.loginfo(self.motion)
				        self.movement.publish(self.motion)
				        rate.sleep()
				        break
		        
                #turns the AUV left 45 deg in case right leg is not found
				else:
		            self.motion.linear.x = 0.0
		            self.motion.linear.y = 0.0
		            self.motion.linear.z = 0.0
		            self.motion.angular.x = 0.0
		            self.motion.angular.y = 0.0
		            self.motion.angular.z = 0.785
		            
		            rospy.loginfo(self.motion)
		            self.movement.publish(self.motion)
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
                
	        rospy.loginfo(self.motion)
	        self.movement.publish(self.motion)
	        rate.sleep()
	        continue

		if success:
			self._result.current_goal_status = self.feedback.end_goal_status
			rospy.loginfo("%s succeeded" %self._action_name)			
			rospy.loginfo(motion)
			self.movement.publish(motion)
			viz_0.__del__()
			self._as.set_succeeded(self.result)

if __name__ == '__main__':
	rospy.init_node('channel')
	server = ChannelAction(rospy.get_name())
	rospy.spin()



		
