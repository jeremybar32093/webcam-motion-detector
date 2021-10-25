import cv2, time

# 1.) Create video object
video = cv2.VideoCapture(0)

# 2.) Capture continuous video with while loop
while True:

    # Create frame object that will read what is captured by the VideoCapture object
    #   check is a boolean datatype - for example, check if videocapture is still running
    #   frame is the numpy array of image being captured - 3 dimensions, 
    check, frame = video.read()

    # Convert video capture to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show image being captured
    cv2.imshow("Capturing", gray)

    # Iterate (capture next frame) every 1 millisecond
    key = cv2.waitKey(1)
    
    # Print numpy arrays of video frames being captured
    print(gray)

    # Quit webcam recording if user presses Q key
    if key == ord('q'):
        break

# Release the camera (i.e. stop recording)
video.release()

# close camera capture windows
cv2.destroyAllWindows()
