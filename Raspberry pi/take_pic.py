import picamera
import time
import cv2
import Line_notifier as line
import sys

def take():
    camera = picamera.PiCamera()
    time.sleep(2)
    camera.capture('/home/pi/final_iot/detect.jpg')
    #line.send_pic("Someone is coming", "/home/pi/detect.jpg")
    camera.close() 

def found():
    imagePath = '/home/pi/final_iot/detect.jpg'
    # Create the haar cascade
    cascPath = '/home/pi/final_iot/model/haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)

    if cv2.__version__.startswith('2'):
        PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
        PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
    elif cv2.__version__.startswith('3'):
        PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
        PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite("found.jpg", image)

    #cv2.imshow("preview", image)
    #cv2.waitKey(0)
    if(len(faces) > 0):
        line.send_pic("Someone is coming", "/home/pi/final_iot/found.jpg")
        return 1

    #cv2.destroyAllWindows()
 
    

if __name__ == '__main__':
    take()
    found()