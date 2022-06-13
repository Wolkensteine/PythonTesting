import cv2                              # Opencv must be installed

cam = cv2.VideoCapture(0)

while True:
    _, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 100)

    # cv2.imshow("LiveVideo", image)    uncomment to have a live preview of your cam
    # cv2.imshow("Edges", edges)        uncomment to have a live preview of your cam as only edges
    if cv2.waitKey(1) == ord("q"):      # press q to close all windows 
        break

cam.release()
cv2.destroyAllWindows()
