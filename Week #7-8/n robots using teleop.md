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

$ vi multi_robot.launch

$ vi main.launch

$ roslaunch n_robots main.launch


```
