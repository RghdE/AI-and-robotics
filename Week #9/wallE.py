#!/usr/bin/env python
import rospy
from std_msgs.msg import String 

def wallE_talker():
    hello_pub = rospy.Publisher('hello', String, queue_size = 10)
    rospy.init_node('wallE', anonymous=False)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        greeting = "Hello, Eva" 
        rospy.loginfo(greeting)
        hello_pub.publish(greeting)
        rate.sleep()

if __name__ == '__main__':
    try:
        wallE_talker()
    except rospy.ROSInterruptException:
        pass
