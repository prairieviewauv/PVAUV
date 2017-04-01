import rospy
import roslaunch
from geometry_msgs.msg import Point, Pose, Quarternion, Twist
from std_msgs.msg import Int8, String, Bool

def task_manager():
    rospy.init_node("task_manager", anonymous=True)
    rate = rospy.Rate(10)
    task_status = rospy.Publisher('channel_task/status', Int8, queuesize=1)
    movement = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

    motion  = Twist()

    motion.linear.x = 1.0
    motion.linear.y = 0.0
    motion.linear.z = 0.0
    motion.angular.x = 0.0
    motion.angular.y = 0.0
    motion.angular.z = 0.0  