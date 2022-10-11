import numpy as np
from PIL import ImageGrab
import cv2
import time
from ctype import PressKey, ReleaseKey, W, A, S, D

x1 = 110
y1 = 350

x2 = 520
y2 = 350

x3 = 315
y3 = 340

m = 0
m1 = 0
def maskk(screen, vertex):
    mask = np.zeros_like(screen)
    cv2.fillPoly(mask, vertex, 255)
    mask1 = cv2.bitwise_and(screen, mask)
    return mask1

def dlines(screen, lines):
    global x1, y1
    try:
        for line in lines:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [0, 255, 50], 5)
            x1 = lines[0][0][0]
            y1 = lines[0][0][1]
    except:
        pass

def dlines1(screen, lines1):
    global x2, y2
    try:
        for line in lines1:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [0, 255, 50], 5)
            x2 = lines1[0][0][0]
            y2 = lines1[0][0][1]
    except:
        pass

def dlines2(screen, lines2):
    global x3, y3
    try:
        for line in lines2:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [0, 255, 50], 5)
            x3 = lines2[0][0][0]
            y3 = lines2[0][0][1]
    except:
        pass

t = time.process_time()
print(t)
while True:
    window = np.array(ImageGrab.grab(bbox=(10, 10, 640, 480)))
    #print("Время кадра " + str(time.process_time() -t))
    t = time.process_time()
    im = cv2.cvtColor(window, cv2.COLOR_BGR2GRAY)
    window1 = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
    # sobelx = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize= 5) #играться с ksize
    # sobely = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize= 5)
    # sob = (sobelx + sobely)
    Can = cv2.Canny(im, 10, 200, 7) #играемся с 2-4
    Can = cv2.GaussianBlur(Can, (5, 5), 0)

    #vertex = np.array([[0, 480], [0, 360], [140, 240], [500, 240], [640, 360], [640, 480]])
    vertex1 = np.array([[0, 350], [0, 210], [230, 210], [230, 350]])
    vertex2 = np.array([[420, 350], [420, 210], [630, 210], [630, 350]])
    vertex3 = np.array([[230, 350], [230, 210], [420, 210], [420, 350]])

    Can1 = maskk(Can, [vertex1])
    Can2 = maskk(Can, [vertex2])
    Can3 = maskk(Can, [vertex3])

    lines = cv2.HoughLinesP(Can1, 5, np.pi/180, 100, 10, 100)
    lines1 = cv2.HoughLinesP(Can2, 5, np.pi / 180, 100, 10, 100)
    lines2 = cv2.HoughLinesP(Can3, 5, np.pi / 180, 100, 10, 100)

    dlines(window1, lines)
    dlines1(window1, lines1)
    dlines2(window1, lines2)

    cv2.line(window1, (x1, y1), (110, 350), [100, 0, 100], 5)
    cv2.line(window1, (x2, y2), (520, 350), [100, 0, 100], 5)
    cv2.line(window1, (x3, y3), (315, 350), [100, 0, 100], 5)

    d1 = int(np.sqrt((x1-110)**2+(y1-350)**2))
    d2 = int(np.sqrt((x2-520)**2+(y2-350)**2))
    d3 = int(np.sqrt((x2 - 315) ** 2 + (y2 - 350) ** 2))
    # if d1<=100:
    #     PressKey(D)
    #     PressKey(W)
    #     time.sleep(0.5)
    #     ReleaseKey(D)
    #     ReleaseKey(W)
    #     ReleaseKey(A)
    #     ReleaseKey(S)
    #     time.sleep(0.2)
    # elif d2<=100:
    #     PressKey(A)
    #     PressKey(W)
    #     time.sleep(0.5)
    #     ReleaseKey(D)
    #     ReleaseKey(W)
    #     ReleaseKey(A)
    #     ReleaseKey(S)
    #     time.sleep(0.2)
    if d1!=m and d2==m1:
        PressKey(D)
        PressKey(W)
        time.sleep(0.5)
        ReleaseKey(D)
        ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(S)
        time.sleep(0.2)
    elif d2!=m1 and d1==m:
        PressKey(A)
        PressKey(W)
        time.sleep(0.5)
        ReleaseKey(D)
        ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(S)
        time.sleep(0.2)
    elif d1==m and d2==m1:
        PressKey(S)
        time.sleep(0.5)
        ReleaseKey(D)
        ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(S)
        time.sleep(0.2)
    else:
        PressKey(W)
        time.sleep(0.5)
        ReleaseKey(W)
        time.sleep(0.2)

    cv2.putText(window1, " " + str(d1) + " ", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
    cv2.putText(window1, " " + str(d2) + " ", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
    cv2.putText(window1, " " + str(d2) + " ", (320, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)

    m = d1
    m1 = d2

    cv2.imshow("window_new", window1)


    if cv2.waitKey(30) == ord("q"):
        cv2.destroyAllWindows()
        break