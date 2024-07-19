import cv2
import mediapipe as mp
import pyautogui

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True :
    success, image = webcam.read()
    if not success:
        break
    frame_height ,frame_width ,  _ = image.shape
    x1 = y1 = x2 = y2 = 0

    rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands : 
        for hand in hands :
            drawing_utils.draw_landmarks(image , hand)
            landmarks = hand.landmark
            for id , landmark in enumerate(landmarks) :
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8 :
                    cv2.circle(img=image , center=(x , y ) ,radius= 8 , color=(0,255,255) , thickness=2)
                    x1 = x
                    y1 = y
                if id == 4 :
                    cv2.circle(img=image , center=(x , y ) , radius= 8 , color=(0,0,255) , thickness=2)
                    x2 = x
                    y2 = y
            distance = ((x2-x1)**2) + ((y2 - y1)**2)** 0.5 // 4
            cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2) 
            if distance > 50 :
                pyautogui.press("volumeup")
            else :
                pyautogui.press("vloumendown")
    cv2.imshow("volume control via hand " , image)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
