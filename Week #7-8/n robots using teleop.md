## Steps:
```
$ cd catkin_ws/src 

$ catkin_create_pkg n_robots rospy gazebo_ros 

$ cd .. (go back to parent directory)

$ catkin_make

$ . ~/catkin_ws/devel/setup.bash

$ cd src/n_robots

$ mkdir launch 

$ cd launch 

$ vi one_robot.launch

$ vi robots.launch

$ vi main.launch

$ roslaunch n_robots main.launch (gazebo will open)

```

Control the robots with teleop: (keyboard)
```
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel (1st window)
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot2/cmd_vel (2nd window)
```
