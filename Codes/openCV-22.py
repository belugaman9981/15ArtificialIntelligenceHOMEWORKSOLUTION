import cv2, time

cam = cv2.VideoCapture(0)
cam.set(3, 640); cam.set(4, 360)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

fps = 10
timeStamp = time.time()

while True:
    ignore, frame = cam.read()  
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = list(faceCascade.detectMultiScale(frameGray, 1.3, 5))
    eyes  = list(eyeCascade.detectMultiScale(frameGray, 1.3, 5))
    
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)       
        frameROI = frame[y:y + h, x:x + w]
        frameROIFGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(frameROIFGray)
        
        for eye in eyes:
            xeye, yeye, weye, heye = eye
            cv2.rectangle(frame[y:y + h, x:x + w], (xeye, yeye), (xeye + weye, yeye + heye), (255, 0, 0), 3)

    loopTime = time.time() - timeStamp
    timeStamp = time.time()
    fpsNew = 1 / loopTime
    fps = .9 * fps + .1 * fpsNew

    cv2.putText(frame, str(int(fps)),'fps:', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
    cv2.imshow('My WEBcam', frame)
    cv2.moveWindow('My WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cam.release()

