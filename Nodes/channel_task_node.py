from visualizer import visualizer
import rospy
from geometry_msgs.msg import Point, Pose, Quarternion, Twist
from std_msgs.msg import Int8, String, Bool


def channel_task():
    rospy.init_node("channel_task", anonymous=True)
    rate = rospy.Rate(10)
    task_status = rospy.Publisher('channel_task/status', Int8, queuesize=1)
    movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

    motion  = Twist()

    status = 1
    counter = 0
    above_gate = False
    task_status.publish(status)
    viz_0 = visualizer(0)

    while not rospy.is_shutdown():
        
        while status == 1:
            if viz_0.detectGateLeft():
                    if viz_0.detectGateRight():

                        #check to see if AUV is above bottom of the channel
                        while not above_gate:
                            if viz_0.detectGatebottom()=0:
                                above_gate=True
                                motion.linear.x = 1.0
                                motion.linear.y = 0.0
                                motion.linear.z = 0.0
                                motion.angular.x = 0.0
                                motion.angular.y = 0.0
                                motion.angular.z = 0.0 
                                break
                        
                            #If auv is below bottom of channel, AUV ascends
                            elif viz.detectGateBottom()=1:
                                motion.linear.x = 0.0
                                motion.linear.y = 0.0
                                motion.linear.z = 1.0
                                motion.angular.x = 0.0
                                motion.angular.y = 0.0
                                motion.angular.z = 0.0
                                
                                rospy.loginfo(motion)
                                movement.publish(motion)
                                rate.sleep()
                                
                        status = 2  
                        rospy.loginfo(motion)
                        movement.publish(motion)
                        rate.sleep()
                        break
                
                #turns the AUV left 45 deg in case right leg is not found
                else:
                        motion.linear.x = 0.0
                        motion.linear.y = 0.0
                        motion.linear.z = 0.0
                        motion.angular.x = 0.0
                        motion.angular.y = 0.0
                        motion.angular.z = 0.785
                        
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
                
                rospy.loginfo(motion)
                movement.publish(motion)
                rate.sleep()
                continue
        
        rospy.loginfo(motion)
        movement.publish(motion)
        task_status.publish(status)
        viz_0.__del__()
        rate.sleep()

if __name__ == '__main__':
    try:
        channel_task()
    except rospy.ROSInterruptException:
           pass