# webcam-motion-detector

This repo contains a pyton script called *motion_detector.py* that utilizes the [opencv](https://pypi.org/project/opencv-python/) python library to engage the computer webcam. 

The script will then capture a static image initially and compare the frames as the webcam is running to ultimately detect moving objects. This ends up looking something like the following:

**Static Frame:**
<br>
<br>
![Static Frame Example](/images/Static%20Frame%20Example.png)

**Object Detected:**
<br>
<br>
![Object Detected Example](/images/Object%20Detected%20Example.png)

When objects are detected, the script also creates a file that captures the point in time that the object enters and exits the frame. The file looks like the following:
<br>
<br>
![Output File Example](/images/Output%20File%20Example.png)
<br>
Where column A represents an identifier for the object that was detected, column B is the point in time at which the object entered the frame, and column C is the point in time at which the object exited the frame.

While running, the script can be exited by pressing the *q* key.

**NOTE:** Code in this repository was adapted from an online Python training course called [The Python Megacourse 2022: Build 10 Real World Programs](https://www.udemy.com/course/the-python-mega-course/) featured on [udemy](https://www.udemy.com/), taught by [Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/#instructor-1).
