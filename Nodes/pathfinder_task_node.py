#!/usr/bin/env python
from visualizer import visualizer
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8, String, Bool

def pathfinder_task():
    rospy.init_node("pathfinder_task", anonymous=True)
    rate = rospy.Rate(10)
    task_status = rospy.Publisher('pathfinder_task/status', Int8, queue_size = 10)
    movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

    motion  = Twist()

    status = 0
    task_status.publish(status)
    viz_1 = visualizer(1)

    while not rospy.is_shutdown():
        while status != 3:
            line_check = viz_1.detectLine("orange")
          
            if line_check == -1:
                if status == 1:
                    status = 3
                    break
                else:   
                    continue
            #if the line is centered to the AUV, continue forward
            elif line_check == 0:
                status = 1
                motion.linear.x = 1.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = 0.0

            #if the line curves left, AUV turns left
            elif line_check == 1:
                status = 1
                motion.linear.x = 1.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = 0.050

            #if the line curves right, AUV turns right
            elif line_check == 2:
                status = 1
                motion.linear.x = 1.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = -0.050
            
            else:
                continue
            
            #publish AUV motion changes
            rospy.loginfo(motion)
            movement.publish(motion)
            rospy.loginfo(status)
            task_status.publish(status)
            rate.sleep()

        #after follwing line, AUV stops inorder to process next task
        motion.linear.x = 0.0
        motion.linear.y = 0.0
        motion.linear.z = 0.0
        motion.angular.x = 0.0
        motion.angular.y = 0.0
        motion.angular.z = 0.0
        
        rospy.loginfo(motion)
        movement.publish(motion)
        rospy.loginfo(status)
        task_status.publish(status)
        rate.sleep()

        viz_1.__del__()

if __name__ == '__main__':
    try:
        pathfinder_task()
    except rospy.ROSInterruptException:
           pass

            