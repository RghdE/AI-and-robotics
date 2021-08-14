### Requirements:

Ubunto 18.4 Bionic

Gazebo 9.0

ROS melodic

##
## Steps:
1. Follow the instructions on [diff_drive_bot](https://github.com/devanshdhrafani/diff_drive_bot)

```
$ cd catkin_ws/src

$ git clone https://github.com/devanshdhrafani/diff_drive_bot.git (cloning the package to your source folder)

$ cd ..

$ catkin_make

$ sudo apt-get install ros-melodic-dwa-local-planner

$ sudo apt-get install ros-melodic-joy

$ roslaunch diff_drive_bot gazebo.launch (here I used turtlebot3_house because I need the genertaed map later, but you can change it)
```
![VirtualBox_Ubuntu 18 4 Bionic_14_08_2021_07_31_55](https://user-images.githubusercontent.com/53378171/129462344-7e0a91b7-e21c-40ef-a8df-81a8ba9e1810.png)

```
$ roslaunch diff_drive_bot gmapping.launch (open RViz)
```
![VirtualBox_Ubuntu 18 4 Bionic_14_08_2021_07_47_43](https://user-images.githubusercontent.com/53378171/129462353-ae44cc69-0fcc-4c5e-b5ed-34993cd4f76a.png)

```
$ rosrun diff_drive_bot keyboard_teleop.py (you can repalce it with joy_teleop_launch.launch if you have a joystick)
```

![VirtualBox_Ubuntu 18 4 Bionic_14_08_2021_07_54_26](https://user-images.githubusercontent.com/53378171/129462366-363e86aa-e1d9-48e1-b8cd-1364fb7d4cda.png)


- move around with the robot untill the map is created and the robot has recognized the environment and the obstacles to avoid-
![VirtualBox_Ubuntu 18 4 Bionic_14_08_2021_08_00_24](https://user-images.githubusercontent.com/53378171/129462367-8e2d10c8-8b92-4554-9d7f-5ca363a3e562.png)
```
$ rosrun map_server map_saver -f ~/my_map
```


you can continue with the Autonomous Navigation step but for my task this was enough.

