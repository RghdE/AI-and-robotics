# If you're a macOS Catalina user, these steps are for you!

First, you need to understand how **OpenCV** work:
1.	Calling the classifiers; you can get them form their open source in GitHub. 
2.	Convert the frame or image, -depending on the program- to gray.
3.	Highlighting the object coordinates with a rectangle, which you can change its colors and width.
4.	After that, make sure to end the program with a command or a keyboard letter you can enter to quit the camera.



# Steps:
1.	Source the work directly with: 

    `$ python[your version] -m venv work`  
  
    `$ source work/bin/activate` 
     
    `$ pip install opencv-python`
  
  
2.	And while you are in that directory (work -to the left-), change your directory to the folder in which you have your program.
    Then launch the program using the known command: 
    
     `$ python [the name of your program.py]` 
     
    then the seminal would ask you to access your camera, and then after you run it again, it will hopefully work. 

![HOOR](https://user-images.githubusercontent.com/53378171/125168987-d8a33380-e1b0-11eb-9552-e114eaf1fb1c.png)


P.S: I don’t know if there is another easier way to do this, but since this way worked, I’ll make it the default way of launching any Python program with OpenCV in it.
