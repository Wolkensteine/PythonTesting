import cv2
from PIL import Image
import numpy as np

print("Give me a file!!! (It must be in the input folder!)")

filename = input()

image = np.array(Image.open("input/"+filename))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 100)

cv2.imshow("Edges", edges)

while True:
    if cv2.waitKey(1) == ord("q"):
        break

cv2.imwrite('Output/out.png', edges)
