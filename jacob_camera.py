import cv2
import keyboard
def camera():
    try:
        vid = cv2.VideoCapture(0)
        while(True):
            ret,frame = vid.read()
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & keyboard.is_pressed('q'):
                break
        vid.release()
        cv2.destroyAllWindows() 
    except:
        print("Unexpected error occured")           