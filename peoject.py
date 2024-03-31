import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("capture")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("capture", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 13:
        # ENTER pressed
        img_name = "full1{}.png".format(img_counter)
        cv2.imwrite("D:\\code\\full\\"+img_name+".png", frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
