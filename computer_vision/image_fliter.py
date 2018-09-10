import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    mark1=-1
    mark2=-1
    for loop1 in frame:
        mark2=-1
        mark1=mark1+1
        for loop2 in loop1:
            mark2=mark2+1
            #print(loop2[0])
            if loop2[0] > 30 and loop2[1]>30 and loop2[2]>100:
                pass
            else:
                #print("mark1",mark1)
                #print("mark2",mark2)
                frame[mark1][mark2][0]=0
                frame[mark1][mark2][1]=0
                frame[mark1][mark2][2]=0
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
