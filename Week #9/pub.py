#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped

def pub():
    rospy.init_node("pub") 
    goal_publisher = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10) 

    goal = PoseStamped()

    goal.header.seq = 5
    goal.header.frame_id = "map"
    
    goal.pose.position.x = 1.65549182892
    goal.pose.position.y = 0.19844982028
    goal.pose.position.z = 0.0
    
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0

    rospy.sleep(1)
    goal_publisher.publish(goal) 
    rospy.spin() 

if __name__ == '__main__':
     try:
         pub()
     except rospy.ROSInterruptException:
         pass
