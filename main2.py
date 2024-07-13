from ultralytics import YOLO
import  cv2
import cvzone
import math



model = YOLO('best.pt')

classNames = ["urine",]
def pixel2(link):
    img=cv2.imread(link)
    results = model(img, stream=True)
    init=0
    final=0
    X1=0
    X2=0
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            # print(x1)
            # print(h)
            init=y1
            final=y2
            X1=x1
            X2=x2
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((box.conf[0]*100))/100

            cls = box.cls[0]
            name = classNames[int(cls)]

            cvzone.putTextRect(img, f'{name} 'f'{conf}', (max(0,x1), max(35,y1)), scale = 0.5)
            break
    im1=img[init:final,X1:X2]        
    cv2.imwrite('im1.jpeg', im1)
    cv2.imwrite('im2.jpeg', img)
    return(init,final)



