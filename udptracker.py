import cv2
from cvzone.PoseModule import PoseDetector
import socket
cap = cv2.VideoCapture(0)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5056)   

detector = PoseDetector()
posList = []  
count = 0
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
            count +=1
        print(count)
        count = 0
        print(lmString)
        date = lmString
        sock.sendto(str.encode(str(date)), serverAddressPort)

    cv2.imshow("Image", img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
