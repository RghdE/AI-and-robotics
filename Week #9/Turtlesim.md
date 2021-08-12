# A beginner tutorial to learn to publish a position or a message between two ROS nodes  

## Turtlesim Tutorial:
```
$ roscore (1st tab)

$ rosrun turtlesim turtlesim_node (2nd tab)

$ rosrun turtlesim turtle_teleop_key (make sure the tab is active while moving around with the turtle 
in your keyboard) 

$ rostopic echo /turtle1/cmd_vel (rostopic echo: to print the messages published under any topic)

$ rosrun rqt_graph rqt_graph (to see nodes and their associated topic visually)
```
![VirtualBox_Ubuntu 18 4 Bionic_09_08_2021_02_44_26](https://user-images.githubusercontent.com/53378171/129241602-839a1d60-13b0-4486-ac66-7ac82740e7d1.png)

```
$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, 4.0]' 
(rostopic pub -1: publish once and exit) 
```

![turtlesim](https://user-images.githubusercontent.com/53378171/129241056-ff2ec747-91fb-498c-a569-24e89ea38e16.png)


```
$ rostopic pub  /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, 4.0]' 
(rostopic pub -r 1: publish the message repeatedly at the rate of one second) 
```

- if you want to make the robot move with your control AND with a predefined controller:
```
$ rostopic pub  /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, 4.0]' 

$ rosrun turtlesim turtle_teleop_key 
```

![VirtualBox_Ubuntu 18 4 Bionic_09_08_2021_02_53_21](https://user-images.githubusercontent.com/53378171/129241711-6a466112-09a1-4cea-8df4-b3f24a8c8052.png)



## Publisher and Subscriber scripts (Python)
If you have already created a package with rospy dependency in it, place these steps in **/scripts** directory. If you don't have this package follow the first two [steps here](https://github.com/raghdutionn/AI-and-robotics/blob/main/Week%20%239/Publish%20to%20a%20topic%20using%20a%20Python%20script.md)

- In a new tab:
```
$ cd scripts
    
$ vi wallE.py (here you can write your Python script using any editor vi/vim ...etc) 

- In a new tab run:

$ roscore -if you haven't already-

$ chmod +x wallE.pyn (change the permission to make the *publsiher* file executable)

$ python wallE.py (here you can see that your message gets published by the help of # rospy.loginfo(greeting) )

you can run: 

$ rosrun rqt_graph rqt_graph (you'll see wallE node alone because initially there are no subscriptions to (hello) topic)

$ rostopic echo /hello (if you refreshed the rqt_graph window you'll see the wallE publisher with /hello topic and a subscriber)

now create the subscriber code:

$ vi Eva.py

$ chmod +x Eva.py (change the permission to make the subscriber file executable)

$ python Eva.py 

$ python wallE.py 

here you'll see clearly how the publisher and the subscriber nodes are communicating 
```
---

You're done! 

---
Notes: 

- If you add `#!/usr/bin/env python` line at the begginneng of your python script, and sourced your workesapce, you can run the file from anywhere using: 

`$ rosrun [package name] [pyhton file name.py]` 

- Do this tutorial first before jumping into [this](https://github.com/raghdutionn/AI-and-robotics/blob/main/Week%20%239/Publish%20to%20a%20topic%20using%20a%20Python%20script.md) task, it'll be way easier for you.

Python files:

[wallE.py](https://github.com/raghdutionn/AI-and-robotics/blob/main/Week%20%239/wallE.py)

[Eva.py](https://github.com/raghdutionn/AI-and-robotics/blob/main/Week%20%239/Eva.py)



