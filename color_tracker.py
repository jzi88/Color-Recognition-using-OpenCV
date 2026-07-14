import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # change the color space from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blue color range in HSV
    lower_blue = (100, 150, 50)
    upper_blue = (140, 255, 255)

    # mask the blue color in the image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # search for contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        # drop small contours to reduce noise
        if cv2.contourArea(contour) > 500:

            # draw a rectangle around the object
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # calculate the center of the object
            center_x = x + w // 2
            center_y = y + h // 2

            # draw a small circle at the center of the object
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            # write the label "Blue Object" above the rectangle
            cv2.putText(frame, "Blue Object",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 0, 0),
                        2)

    # show the original frame, mask, and result
    cv2.imshow("Original", frame)
    cv2.imshow("Blue Mask", mask)
    cv2.imshow("Blue Object", result)

    # quit when pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()