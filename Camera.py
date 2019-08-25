import cv2

video_capture = cv2.VideoCapture(0)
i=0
while True:
    # Capture frame-by-frame
    try:
        ret, frame = video_capture.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        #start = time.time()

        cv2.imshow('InTarget', frame)  # mostra na tela
        #while time.time() < start + 5:
        if i%300==0:
    	    cv2.imwrite('in.jpg',frame)

        #cv2.waitKey(0)

        key = cv2.waitKey(100) & 0xFF
        if key == ord("q"):
            break
    except:
        print("erro")
    i+=1

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()