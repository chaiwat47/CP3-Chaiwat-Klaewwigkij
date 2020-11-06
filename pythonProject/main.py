#import paho.mqtt.client as
#import cv2
#import numpy as np
host = "10.5.50.18"
port = 1883

class machine:
    def Hi():
        print('Hi')

    def Eat():
        print('breakfast')


    '''def robot(self):
        while (True):
            client = mqtt.Client()
            client.connect(host)
            a = int(input("คำสั่ง"))
            if a == 1:
                client.publish("esp/test", "{1}")
                client.publish("esp/test", "{1}")
                print("เดินหน้า", a)
            if a == 2:
                client.publish("esp/test", "{2}")
                client.publish("esp/test", "{2}")
                print("เลี้ยวขวา", a)
            if a == 3:
                client.publish("esp/test", "{3}")
                client.publish("esp/test", "{3}")
                print("เลี้ยวซ้าย", a)
            if a == 4:
                client.publish("esp/test", "{4}")
                client.publish("esp/test", "{4}")
                print("หยุด", a)
            if a == 5:
                client.publish("esp/test", "{5}")
                client.publish("esp/test", "{5}")
                print("ถอยหลัง", a)
            if a == 'q':
                break'''

    '''def camera():
        cap = cv2.VideoCapture(0)

        while (cap.isOpened()):
            ret, img = cap.read()
        if ret:
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.rectangle(img, (184, 124), (515, 368), (0, 0, 255), 2)
            cv2.imshow('image', img)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
        cap.release()
        cv2.destroyAllWindows()'''

machine.Hi()
machine.Eat()








