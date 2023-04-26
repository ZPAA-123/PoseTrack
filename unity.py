import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('1.flv')

_ISOPENED = cap.isOpened()
detertor = PoseDetector()

posList = [] 
while True:
    success, img = cap.read()
    img = detertor.findPose(img)
    lmList, bboxInfo = detertor.findPosition(img)  

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            #opencv和unity的定位点不同所以要做y轴反转
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        posList.append(lmString)

    img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4, interpolation=cv2.INTER_NEAREST)
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)

    if key == ord('s'):
        with open("AnimationFile.txt",'w') as f:
            f.writelines(["%s\n" % item for item in posList])