# This task is for launching multiple TB3 on one map and controlling them using Teleop

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
```
Place [Launch](https://github.com/raghdutionn/AI-and-robotics/tree/main/Week%20%237-8/launch) files here:
```
$ vi one_robot.launch

$ vi robots.launch

$ vi main.launch

$ roslaunch n_robots main.launch (Gazebo will open)

```
![VirtualBox_Ubuntu 18 4 Bionic_15_08_2021_07_26_22](https://user-images.githubusercontent.com/53378171/129467444-e83ed552-d451-4d13-a04d-a7e837204858.png)


```
$ rostopic list (to see running topics and robots)
```
![VirtualBox_Ubuntu 18 4 Bionic_15_08_2021_07_27_46](https://user-images.githubusercontent.com/53378171/129467470-e7ac1ec4-55ea-431b-8726-db8d7ec01dd1.png)

Control the robots with teleop: (keyboard)
```
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel (1st window)
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot2/cmd_vel (2nd window)
```
https://user-images.githubusercontent.com/53378171/129467546-9c1ca755-80a6-40cf-bf28-52114ed83a6b.mov

## Problems Faced:

- when I ran `$ catkin_make` the virtual machine halted. I tried 4 times but it didn't work. So I tried to delete unesseary packages and It worked.

![VirtualBox_Ubuntu 18 4 Bionic_15_08_2021_06_27_26](https://user-images.githubusercontent.com/53378171/129467577-1a41b7f7-08de-4e33-9dea-957846777fd6.png)

- At first, I added 3 Turtlebots, I think I made a mistake with the Robots positions, they were very far away from each other. 

![VirtualBox_Ubuntu 18 4 Bionic_15_08_2021_07_22_06](https://user-images.githubusercontent.com/53378171/129467666-1ebbc008-887a-4c81-803c-63299b9a701f.png)

- Then I fixed it; I only made changes to the x-axis and left the y-axis as it is ( 1 ). But when I ran `$ rolaunch`, I faced this error, so I deleted the 3rd robot and it worked.

![VirtualBox_Ubuntu 18 4 Bionic_15_08_2021_07_29_59](https://user-images.githubusercontent.com/53378171/129467741-b507f57c-464d-4184-896d-78868f6811a6.png)
