##USING OpenCV
import cv2

#We want to read the path from the user we could do this
imgPath = input("Enter Image Path : ")
# Loads an image
img = cv2.imread(imgPath)
# Check if image is loaded fine
if img is None:
    print('Error opening image!')
else:
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.imshow("Input Image", img)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        area = cv2.contourArea(contour)
        #CIRCLE
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30)):
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(img, center, radius, (0, 0, 255), -1)
        #TRIANGLE
        elif len(approx) == 3:
            cv2.drawContours(img, [contour] , 0, (0, 255 , 0), -1)
        #REGTANGLE
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            if x!=0 and y!=0:
                img = cv2.rectangle(img , (x, y) , (x + w, y + h) , (255,0,0) , -1)
        #UNKNOWN_SHAPE
        else:
            cv2.drawContours(img, [contour], 0, (0, 0, 0), -1)
    cv2.imshow("Output Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
