# webcam-motion-detector

This repo contains a pyton script called *motion_detector.py* that utilizes the [opencv](https://pypi.org/project/opencv-python/) python library to engage the computer webcam. 

The script will then capture a static image initially and compare the frames as the webcam is running to ultimately detect moving objects. This ends up looking something like the following:

**Static Frame:**
<br>
![Static Frame Example](/images/Static Frame Example.png)

**Object Detected:**

When objects are detected, the script also creates a file that captures the point in time that the object enters and exits the frame. The file looks like the following:

While running, the script can be exited by pressing the *q* key.

**NOTE:** Code in this repository was adapted from an online Python training course called [The Python Megacourse 2022: Build 10 Real World Programs](https://www.udemy.com/course/the-python-mega-course/) featured on [udemy](https://www.udemy.com/), taught by [Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/#instructor-1)
