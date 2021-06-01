from types import FrameType
from pipeline import fetchline
import cv2



video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

while True:

    ret, frame = video.read()

    image = fetchline(frame)


    cv2.imshow("Lane", image)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()