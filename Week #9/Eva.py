import rospy
from std_msgs.msg import String 

def Callback_str(data):
    rospy.loginfo(data.data)
    

def Eva_listener():
    rospy.init_node('Eva', anonymous=False)
    rospy.Subscriber('hello', String, Callback_str)
    rospy.spin()

if __name__ == '__main__':
    Eva_listener()
