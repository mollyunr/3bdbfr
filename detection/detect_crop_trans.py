import cv2, sys
import numpy as np

if len(sys.argv) == 2:
    fileName = sys.argv[1]
    image = cv2.imread(fileName)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceClassifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    eyeClassifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')
    faces = faceClassifier.detectMultiScale(grayImage)

    print faces

    for x, y, w, h in faces:
        roi_gray = grayImage[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        eyes = eyeClassifier.detectMultiScale(roi_gray)

        points = []

        for ex, ey, ew, eh in eyes:
            point = [ex + ew/2, ey]
            points.append(point)
            point = [ex + ew/2, ey + eh/2]
            points.append(point)

        if points[0][0] > points[2][0]:
            p3 = points[0]
            p4 = points[1]
            p1 = points[2]
            p2 = points[3]
            del points
            points = []
            points.append(p1)
            points.append(p2)
            points.append(p3)
            points.append(p4)

        x = points[1][0] + points[3][0]
        x /= 2
        y = points[1][1] + points[3][1]
        y /= 2

        y += 40

        points[2] = [x,y]

        pts1 = np.float32(points)
        pts2 = np.float32([[20, 28], [20, 38], [46, 80], [65, 38]])

        M = cv2.getPerspectiveTransform(pts1, pts2)

        dst = cv2.warpPerspective(roi_gray, M, (92, 112))

        cv2.imwrite('output.pgm', dst)
