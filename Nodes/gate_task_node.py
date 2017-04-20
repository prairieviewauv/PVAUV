#!/usr/bin/env python
from visualizer import visualizer
import rospy
from geometry_msgs.msg import Point, Pose, Quaternion, Twist
from std_msgs.msg import Int8, String, Bool

def gate_task():
    rospy.init_node("gate_task", anonymous=True)
    rate = rospy.Rate(10)
    task_status = rospy.Publisher('gate_task/status', Int8, queue_size = 10)
    movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

    motion  = Twist()

    status = 1
    task_status.publish(status)
    counter = 0
    viz_0 = visualizer(0)

    while not rospy.is_shutdown():
        
        while status == 1:
            if viz_0.detectGateLeft("orange"):
            	if viz_0.detectGateRight("orange"):
                        motion.linear.x = 1.0
                        motion.linear.y = 0.0
                        motion.linear.z = 0.0
                        motion.angular.x = 0.0
                        motion.angular.y = 0.0
                        motion.angular.z = 0.0
                
                    	status = 2
                    	break		        
                    
                        
                #turns the AUV left 45 deg in case right leg is not found
            	else:
			motion.linear.x = 0.0
			motion.linear.y = 0.0
			motion.linear.z = 0.0
			motion.angular.x = 0.0
			motion.angular.y = 0.0
			motion.angular.z = 0.785
			movement.publish(motion)
            
			motion.angular.z = 0.0
			rospy.loginfo(motion)
			movement.publish(motion)
			rate.sleep()
			continue
            
            #turns the AUV right 45 deg in case left leg not found
            else:
                motion.linear.x = 0.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = 0.785
                counter +=1

                if counter > 6:
                        motion.linear.x = 1.0
                        motion.linear.y = 0.0
                        motion.linear.z = 0.0
                        motion.angular.x = 0.0
                        motion.angular.y = 0.0
                        motion.angular.z = 0.0
                        counter = 0
                
                motion.angular.z = 0.0
                rospy.loginfo(motion)
                movement.publish(motion)
                rate.sleep()
                continue

        rospy.loginfo(motion)
        movement.publish(motion)
        rospy.loginfo(status)
        task_status.publish(status)
        viz_0.__del__()
        rate.sleep()

if __name__ == '__main__':
    try:
        gate_task()
    except rospy.ROSInterruptException:
           pass
