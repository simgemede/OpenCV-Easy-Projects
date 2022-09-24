import cv2

while True:
    try:
        giris = input("Fotoğraf çekmek için 's', çıkış yapmak için 'q':")
        if giris == "s":
            giris = cv2.waitKey(1)
            webcam = cv2.VideoCapture(0)
            _,frame = webcam.read()
            cv2.imwrite(filename="image.jpg",img=frame)
            frame.destroy()
        if giris == "q":
            print("ELVEDA")
            webcam.release()
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
             print("ELVEDA")
             webcam.release()
             cv2.destroyAllWindows()
             break
