from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import cv2
import threading
import smtplib     # Library for email sending
import ssl
from email.message import EmailMessage
import imghdr
import pytesseract
import csv
import numpy as np
import vehicles
import time
a=[]
def send_mail_function3():
   
    email_sender = 'hallothonpes@gmail.com'
    email_password = 'evamzmmsguxqwprf'
    email_receiver = 'shishirhebbar74799@gmail.com'
    subject = 'Traffic Violation'
    body = """"
    ID 43 has been violating speed limits.
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    with open('opencv0.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    em.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
def send_mail_function2(a):
    email_sender = 'hallothonpes@gmail.com'
    email_password = 'evamzmmsguxqwprf'
    email_receiver = a[5]
    subject = 'Traffic Violations'
    body = """"
    Insurance of your vehicle has been expired.
    Pay fine of Rs1000 before 30 days
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("MAIL SENT SUCCESSFULY")

def send_mail_function():
   
    email_sender = 'hallothonpes@gmail.com'
    email_password = 'evamzmmsguxqwprf'
    email_receiver = 'shishirhebbar74799@gmail.com'
    subject = 'Traffic violation fine'
    body = """"
    Person not wearing helmet at location(x,y,z)
    Pay fine of Rs 500 on/before 30 days. 
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    with open('opencv0.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    em.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
def funct2():
    runOnce=False
    frameWidth = 640
    frameHeight =400
    minArea=500
    color=(255,0,255)
    faceCascade =cv2.CascadeClassifier("face.xml")
    cap=cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeight)
    cap.set(10,150)
    while True:
        success, img=cap.read()
        imgGray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(imgGray,1.1,4)
        for (x,y,w,h) in faces:
            area=w*h
            if area >minArea:

                cv2.rectangle(img, (x,y) , (x+w,y+h),(255,0,0),2)
                cv2.putText(img,"WITHOUT HELMET",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
                return_value, image = cap.read()
                cv2.imwrite('opencv'+str(0)+'.png', image)
                if runOnce == False:
                    print("Mail send initiated")
                    # To call alarm thread
                    send_mail_function()
                    runOnce = True
                if runOnce == True:
                    print("Mail is already sent once")
                    runOnce = True
                imgRoi =img[y:y+h,x:x+w]
                cv2.imshow("ROI",imgRoi)
        cv2.imshow("Result",img)
        if(cv2.waitKey(1)& 0xFF==ord('q')):
            break
def funct3():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Hp\AppData\Local\Tesseract-OCR\tesseract.exe'
    frameWidth = 640
    frameHeight =400
    minArea=500
    color=(255,0,255)
    faceCascade =cv2.CascadeClassifier("numberplate.xml")
    cap=cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeight)
    cap.set(10,150)
    while True:
        success, img=cap.read()
        imgGray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces=faceCascade.detectMultiScale(imgGray,1.1,4)
        for (x,y,w,h) in faces:
            area=w*h
            if area >minArea:

                cv2.rectangle(img, (x,y) , (x+w,y+h),(255,0,0),2)
                cv2.putText(img,"Numebr plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
                imgRoi =img[y:y+h,x:x+w]
                text_1 = pytesseract.image_to_string(imgRoi)
                #print(text_1)
                #print(len(text_1))
                if(len(text_1)>13):
                    #print("hel")
                    with open("data.csv", 'r') as file:
                        csvreader = csv.reader(file)
                        for i in csvreader:
                            #print(i)
                            #print("in csv")
                            #print(text_1,"---------",i[0])
                            if((text_1.strip())==(i[0].strip())):
                                print("Mail initiated")
                                a=i
                                
                                if(a[3]=="no" or a[4]=="no"):
                                    send_mail_function2(a)
                                    break

                cv2.imshow("ROI",imgRoi)
        cv2.imshow("Result",img)
        if(cv2.waitKey(1)& 0xFF==ord('q')):
            break
def funct4():
    cnt_up=0
    cnt_down=0


    cap=cv2.VideoCapture("surveillance.m4v")

    #Get width and height of video

    w=cap.get(3)
    h=cap.get(4)
    frameArea=h*w
    areaTH=frameArea/100

    #Lines
    line_up=int(2*(h/5))
    line_down=int(3*(h/5))

    up_limit=int(1*(h/5))
    down_limit=int(4*(h/5))
    print("Red line y:",str(line_down))
    print("Blue line y:",str(line_up))
    line_down_color=(255,0,0)
    line_up_color=(255,0,255)
    pt1 =  [0, line_down]
    pt2 =  [w, line_down]
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))
    pt3 =  [0, line_up]
    pt4 =  [w, line_up]
    pts_L2 = np.array([pt3,pt4], np.int32)
    pts_L2 = pts_L2.reshape((-1,1,2))

    pt5 =  [0, up_limit]
    pt6 =  [w, up_limit]
    pts_L3 = np.array([pt5,pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1,1,2))
    pt7 =  [0, down_limit]
    pt8 =  [w, down_limit]
    pts_L4 = np.array([pt7,pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1,1,2))

    #Background Subtractor
    fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)

    #Kernals
    kernalOp = np.ones((3,3),np.uint8)
    kernalOp2 = np.ones((5,5),np.uint8)
    kernalCl = np.ones((11,11),np.uint8)


    font = cv2.FONT_HERSHEY_SIMPLEX
    cars = []
    max_p_age = 5
    pid = 1

    k=0
    while(cap.isOpened()):
        ret,frame=cap.read()
        for i in cars:
            i.age_one()
        fgmask=fgbg.apply(frame)
        fgmask2=fgbg.apply(frame)

        if ret==True:

            #Binarization
            ret,imBin=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
            ret,imBin2=cv2.threshold(fgmask2,200,255,cv2.THRESH_BINARY)
            #OPening i.e First Erode the dilate
            mask=cv2.morphologyEx(imBin,cv2.MORPH_OPEN,kernalOp)
            mask2=cv2.morphologyEx(imBin2,cv2.MORPH_CLOSE,kernalOp)

            #Closing i.e First Dilate then Erode
            mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernalCl)
            mask2=cv2.morphologyEx(mask2,cv2.MORPH_CLOSE,kernalCl)


            #Find Contours
            countours0,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            for cnt in countours0:
                area=cv2.contourArea(cnt)
            # print(area)
                if area>areaTH:
                    ####Tracking######
                    m=cv2.moments(cnt)
                    cx=int(m['m10']/m['m00'])
                    cy=int(m['m01']/m['m00'])
                    x,y,w,h=cv2.boundingRect(cnt)

                    new=True
                    if cy in range(up_limit,down_limit):
                        for i in cars:
                            if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                                new = False
                                i.updateCoords(cx, cy)

                                if i.going_UP(line_down,line_up)==True:
                                    cnt_up+=1
                                    print("ID:",i.getId(),'crossed going up at', time.strftime("%c"))
                                    return_value,image=cap.read()
                                    cv2.imwrite('opencv'+str(k)+'.png',image)
                                    k+=1
                                elif i.going_DOWN(line_down,line_up)==True:
                                    cnt_down+=1
                                    return_value, image = cap.read()
                                    cv2.imwrite('opencv'+str(0)+'.png', image)
                                    send_mail_function3()
                                    print("ID:", i.getId(), 'crossed going down at', time.strftime("%c"))
                                    return_value,image=cap.read()
                                    cv2.imwrite('opencv'+str(k)+'.png',image)
                                    k+=1
                                break
                            if i.getState()=='1':
                                if i.getDir()=='down'and i.getY()>down_limit:
                                    i.setDone()
                                elif i.getDir()=='up'and i.getY()<up_limit:
                                    i.setDone()
                            if i.timedOut():
                                index=cars.index(i)
                                cars.pop(index)
                                del i

                        if new==True: #If nothing is detected,create new
                            p=vehicles.Car(pid,cx,cy,max_p_age)
                            cars.append(p)
                            pid+=1

                    cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
                    img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            for i in cars:
                cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)




            str_up='UP: '+str(cnt_up)
            str_down='DOWN: '+str(cnt_down)
            frame=cv2.polylines(frame,[pts_L1],False,line_down_color,thickness=2)
            frame=cv2.polylines(frame,[pts_L2],False,line_up_color,thickness=2)
            frame=cv2.polylines(frame,[pts_L3],False,(255,255,255),thickness=1)
            frame=cv2.polylines(frame,[pts_L4],False,(255,255,255),thickness=1)
            cv2.putText(frame, str_up, (10, 40), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, str_up, (10, 40), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.imshow('Frame',frame)

            if cv2.waitKey(1)&0xff==ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()
wi1 = Tk()

# Define the geometry of the window
wi1.geometry("6000x5000")

frame1 = Frame(wi1, width=600, height=400)
frame1.pack()
frame1.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img1 = ImageTk.PhotoImage(Image.open("image2.png"))

# Create a Label Widget to display the text or Image
label1 = Label(frame1,image=img1)
label1.pack()

#l2 = Label(wi1, text='').pack()
bt2 = Button(wi1, text="HELMET DETECTOR",font=('Arial',20), command=funct2)
bt2.place(x=100,y=110)

#l3 = Label(wi1, text='').pack()
bt3 = Button(wi1, text="INSURANCE CHECKER",font=('Arial',20), command=funct3)
bt3.place(x=100,y=260)


bt4 = Button(wi1, text="SPEED DETECTOR",font=('Arial',20), command=funct4)
bt4.place(x=100,y=410)
wi1.mainloop()
