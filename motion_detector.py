import cv2, time

# Create video object
video = cv2.VideoCapture(0)

# Create a variable for the first frame - used to compare against subsequent frames captured 
# If differences in pixellation are detected from first frame, assume that this object is an object in motion going across the camera
first_frame = None

# Capture continuous video with while loop
while True:

    # Create frame object that will read what is captured by the VideoCapture object
    #   check is a boolean datatype - for example, check if videocapture is still running
    #   frame is the numpy array of image being captured - 3 dimensions, 
    check, frame = video.read()

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

    # Show image being captured
    cv2.imshow("Gray", gray)

    # Show delta frame
    cv2.imshow("Delta", delta_frame)

    # Show threshold frame
    cv2.imshow("Threshold", threshold_frame)

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
