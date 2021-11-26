import cv2
import os 
import pyautogui
import BlockFace
import HandTrackingModule as htm
wCam, hCam = 640, 480
cap =cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "Fingerimages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    #print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    #BlockFace.detect_face(img, block=True)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        print(totalFingers)
        try:
            if totalFingers == 0:
                cv2.putText(img, str('Pause'), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
                pyautogui.hotkey('ctrl','space')
            elif totalFingers == 1 :
                pyautogui.hotkey('ctrl', 'up')
                cv2.putText(img, str('Volume Up'), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
            elif totalFingers == 2:
                cv2.putText(img, str('Volume Down'), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
                pyautogui.hotkey('ctrl', 'down')
            elif totalFingers == 3:
                cv2.putText(img, str('Forward'), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
                pyautogui.hotkey('ctrl', 'right')
            elif totalFingers == 4:
                cv2.putText(img, str('Backward'), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
                pyautogui.hotkey('ctrl', 'left')
            elif totalFingers == 5:
                cv2.putText(img, str('Play'), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
                pyautogui.hotkey('ctrl','x')
            
            else:
                pass
        except:
            pass

    cv2.imshow("Image", img)
    cv2.waitKey(1)