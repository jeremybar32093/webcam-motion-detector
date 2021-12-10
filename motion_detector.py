import cv2
from datetime import datetime
import pandas as pd

# Create video object
video = cv2.VideoCapture(0)

# Create a variable for the first frame - used to compare against subsequent frames captured 
# If differences in pixellation are detected from first frame, assume that this object is an object in motion going across the camera
first_frame = None

# Create empty list to store when object detection status below changes
# Add 2 'None' entries because in the loop below check the last 2 entries - will prevent error upon first iteration of loop
status_list = [None,None]

# Create empty list to capture entry times
entry_times = []

# Create empty list to capture exit times
exit_times = []

# Capture continuous video with while loop
while True:

    # Create frame object that will read what is captured by the VideoCapture object
    #   check is a boolean datatype - for example, check if videocapture is still running
    #   frame is the numpy array of image being captured - 3 dimensions, 
    check, frame = video.read()

    # Create "status" variable - used for flagging when object enters/exits frame
    status = 0

    # Convert video capture to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply "Gaussian Blur"
    # Blur the image to remove noise - better accuracy in calculations
    # Parameters are variable to which you are applying the blur, then the width and height of the "Gaussian Kernel" -> for now, use 21 as boilerplate
    # Last parameter is the "standard deviation" -> for now, use 0 as boilerplate
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    # Assign first frame if it has not yet been assigned (i.e. is still None, based on definition above)
    if first_frame is None:
        first_frame = gray
        # Proceed to next iteration of while loop using continue, since we don't have any other frames to compute differences against
        continue

    # Create "delta" frame - compare first frame with current frame
    # Use absdiff method already built into cv2
    delta_frame = cv2.absdiff(first_frame, gray)

    # Create "threshold" frame - if deltas are > certain threshold, assign color of pixel as white, otherwise black
    # inputs include frame to calculate against, actual threshold (difference in pixels, color to use when threshold met (rgb -> white), and finally threshold method (boilerplate for now))
    # Can refer to documentation for different methods to experiment with instead of THRESH_BINARY
    # Also, threshold method returns tuple - when using THRESH_BINARY, return second item of tuple -> boilerplate for now
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # Smooth threshold frame (remove erroneous black splotches from white objects) using dilate method
    # 2nd parameter is "kernel array", too sophisticated for now, so pass in none as boilerplate
    # 3rd parameter - how many times to go through the white images and remove the noise - theoretically the larger the number, the smoother - but likely comes at the expense of performance
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    # Find contours in threshold frame - to ultimately be able to outline object
    # Find contours method returns a tuple, so set variable as tuple
    # Perform operation on copy as opposed to actual frame, and use cv2.RETR_EXTERNAL/cv2.CHAIN_APPROX_SIMPLE -> boilerplate for now
    (cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours --> only execute subsequent code for contours with area > 1000 pixels
    # If it's less than 1000, continue to next iteration in loop
    # If not, execute code underneath in for loop -> calculate outer rectangle of object
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue

        # If python finds a contour area of > 10000, flag as object detected in frame using status variable defined above
        status = 1
        # Calculate rectangle corresponding to contours
        (x, y, w, h) = cv2.boundingRect(contour)
        # Add rectangle to color frame
        # Frame to add, top left point of rectangle, bottom right point of rectangle, color of rectangle, width
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    # Append status to status list defined above - will be one when contours with area >= 10,000 are found, otherwise 0
    status_list.append(status)

    # Determine when an object comes into the frame when the last 2 items of the list are 0 then 1
    if status_list[-1] == 1 and status_list[-2] == 0:
        # Record datetime of this event -> represents point in time that object comes into frame
        entry_times.append(datetime.now())
    
    # Determine when an object leaves the frame when the last two items of the list are 1 then 0
    if status_list[-1] == 0 and status_list[-2] == 1:
        # Record datetime of this event -> represents point in time that object comes into frame
        exit_times.append(datetime.now())

    # Determine when an object leaves the frame when the last 2 items of the list are 1 then 0

    # Show image being captured
    cv2.imshow("Gray", gray)

    # Show delta frame
    cv2.imshow("Delta", delta_frame)

    # Show threshold frame
    cv2.imshow("Threshold", threshold_frame)

    # Show color frame with rectangle
    cv2.imshow("Color Frame", frame)

    # Iterate (capture next frame) every 1 millisecond
    key = cv2.waitKey(1)
    
    # Print numpy arrays of video frames being captured
    # print(gray)

    # Quit webcam recording if user presses Q key
    if key == ord('q'):
        # If the program is exited when an object is in the frame, capture the current time as the ending time - otherwise will be an uneven number of entry/exit times
        if status == 1:
            exit_times.append(datetime.now())
        break

    # print(status)

# print(status_list)
print(entry_times)
print(exit_times)

# Add entry/exit lists to pandas dataframe
entry_exit_df = pd.DataFrame(data={'Start':entry_times, 'Stop':exit_times}, index=None)
print(entry_exit_df)
# Export resulting dataframe to csv file
entry_exit_df.to_csv("Times.csv")

# Release the camera (i.e. stop recording)
video.release()

# close camera capture windows
cv2.destroyAllWindows()
