import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640); cam.set(4, 360)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ignore, frame = cam.read()  
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = list(faceCascade.detectMultiScale(frameGray, 1.3, 5))
    
    for face in faces:
        x, y, w, h = face
        print ('x:', x, 'y:', y, 'width:', w, 'height:', h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    
    cv2.imshow('My WEBcam', frame)
    cv2.moveWindow('My WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cam.release()

