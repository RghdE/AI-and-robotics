# A beginner tutorial to learn to publish a position or a message between two nodes  

## Turtlesim Tutorial:
```
$ roscore

$ rosrun turtlesim turtlesim_node

$ rosrun turtlesim turtle_teleop_key (make sure the tab is active while moving around with the turtle in your keyboard) 

$ rostopic echo /turtle1/cmd_vel (rostopic echo: to print the messages published under any topic)

$ rosrun rqt_graph rqt_graph (to see nodes and their associated topic visually)

$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, 4.0]' (rostopic pub -1: publish once and exit) 

$ rostopic pub  /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, 4.0]' (rostopic pub -r 1: publish the message repeatedly at the rate of one second) 
```

- if you want to make the robot move with your control AND with a predefined controller:
```
$ rostopic pub  /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, 4.0]' 

$ rosrun turtlesim turtle_teleop_key 
```

## Publisher and Subscriber scripts (Python)
If you have already created a package with rospy dependency in it, place these steps in **/scripts** directory. If you don't have this package follow the first two [steps here](https://github.com/raghdutionn/AI-and-robotics/blob/main/Week%20%239/Publish%20to%20a%20topic%20using%20a%20Python%20script.md)
```
$ cd scripts
    
$ vi wallE.py (here you can write your Python script using any editor vi/vim ...etc) 

$ python wallE.py | or $ rosrun <package name> <pyhton file name.py> 

```
