
1. Follow the instructions on [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup), and make sure you chose the correct ROS version you're using from the tabs above

2. Afer you are done with this [step](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#install-turtlebot3-packages)

3. Go to the [Simualtion page](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/) and follow the instruction for Gazebo and [SLAM simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam_simulation/)

4. If you want to do the simulation on SLAM also, make sure you followed the isntructions on the [*Launch Simulation World*](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#launch-simulation-world) for **TurtleBot3 World** or **TurtleBot3 House**

5. If you want to move around with your robot, run [this node](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam_simulation/#run-teleoperation-node) 

6. Moving around inside the map 


https://user-images.githubusercontent.com/53378171/124689613-7bbe2980-dee1-11eb-85ba-ce110d693ae3.mov




7. Lastly, after you've moved aroud with your robot on the map, run this command to save the map to your VM:

   **$ rosrun map_server map_saver -f ~/map**
   
   ![map](https://user-images.githubusercontent.com/53378171/124688166-fdf91e80-dede-11eb-8e49-cd7e2d8a7590.png)

   and voila! you're done!
