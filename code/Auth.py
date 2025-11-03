

import cv2

import mysql.connector
import firstpage as fp


def auth():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
    id = 0
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")

    mycursor = mydb.cursor()
# names related to ids: example ==> Marcelo: id=1,  etc
#names = ['None','Ashmita'] 
    names=[]

    mycursor.execute("Select username from login")
    myresult = mycursor.fetchall()

    for x in myresult:
        #print(x)
        names.append(x[0])
        #print(names)


# Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()
    #img = cv2.flip(img, 1) # Flip vertically

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 50):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            #sql = "Update Attend SET status='Present' where name='"+id+"'"
                #print(id)
            #mycursor.execute(sql)
            #mydb.commit()
            #os.system("python firstpage.py")
            else:
                id = "Cannot detect face"
                confidence = "  {0}%".format(round(100 - confidence))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            if id=="Amulya":
                cam.release()
                
                cv2.destroyAllWindows()
                fp.firstpage()
                
                break
            elif id=="Cannot detect face":
                print("You are not authorised")
                cam.release()
                cv2.destroyAllWindows()

# Do a bit of cleanup
    #print("\n [INFO] Exiting Program and cleanup stuff")
    #cam.release()
    #cv2.destroyAllWindows()



