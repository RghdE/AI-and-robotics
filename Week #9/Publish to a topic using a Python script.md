# Writing a python script that publishes to /move_base_simple/goal topic in ROS

## Steps:
1. Create a package


    Go to [ROS](http://wiki.ros.org/ROS/Tutorials/CreatingPackage) and follow the steps of creating a package
   

  `$ cd ~/catkin_ws/src`

    $ catkin_create_pkg pub std_msgs rospy roscpp (create the package with its dependencies)
  
    $ cd .. (go back to parent directory)

    $ catkin_make

    $ . ~/catkin_ws/devel/setup.bash

2. Writing the Publisher Node
   
  ` $ roscd pub`
   
    $ mkdir scripts
   
    $ cd scripts
    
    $ vi pub.py (here you can write your Python script using any editor) 
   
   
3. Now open the RViz simulator 

  `$ roscore` (1st tab)
    
    $ export TURTLEBOT3_MODEL=burger (2nd tab)
    
    $ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml (here I opened the map i saved before using these steps [1] )

    $ export TURTLEBOT3_MODEL=burger (3rd tab)
    
    $ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch (here follow the steps of [2] and move around with the robot so it can collect info about its environment) 

3. Publishing the robot position to the topic 

 ` $ rostopic echo /move_base_simple/goal` (1st tab)
 
 ` $ rosrun pub pub.py` (2nd tab)
 
 ---
 
## Finally! The Result

https://user-images.githubusercontent.com/53378171/128947962-ccfbd773-6a12-4ebc-9854-486b2bad9510.mov


  

## Recources:
[1] [steps](https://github.com/raghdutionn/AI-and-robotics/blob/main/2nd%20Task/2.1%20Turtlebot3%20with%20SLAM%20approach.md)

[2] [estimate-initial-pose](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/#estimate-initial-pose)

