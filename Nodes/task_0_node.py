import ../Vision/visualizer.py
import rospy
from actionlib_msgs.msg import GoalID, GoalStatus
from geometry_msgs.msg import Point, Pose, Quarternion, Twist
from std_msgs.msg import Int8, String, Bool


task_ID = rospy.Publisher('task_ID', GoalID, queue_size = 1)
task_status = rospy.Publisher('task_status', GoalStatus, queue_size = 10)
movement = rospy.Publisher('task_0/command', Twist, queue_size = 1)

motion  = Twist()
location = Point()


ID = 'task_0'
status = 1
task_ID.publish(ID)
task_status.publish(status)
viz_0 = visualizer(0)


curr_loc = location.x


counter = 0

if viz_0.detectGateLeft():
       	if viz_0.detectGateRight():
                motion.linear.x = 1.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = 0.0

                movement.publish(motion)
                rate.sleep()
                
        #turns the AUV left 45 deg in case right leg is not found
        else:
                motion.linear.x = 0.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = 0.785
                movement.publish(motion)
                rate.sleep()

#turns the AUV right 45 deg in case left leg not found
else:
        motion.linear.x = 0.0
        motion.linear.y = 0.0
        motion.linear.z = 0.0
        motion.angular.x = 0.0
        motion.angular.y = 0.0
        motion.angular.z = 0.785
        counter +=1

        if counter > 3:
                motion.linear.x = 1.0
                motion.linear.y = 0.0
                motion.linear.z = 0.0
                motion.angular.x = 0.0
                motion.angular.y = 0.0
                motion.angular.z = 0.0
                counter = 0

        movement.publish(motion)
        rate.sleep()
