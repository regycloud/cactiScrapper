import cv2
import re
import pytesseract
from pytesseract import Output



def convert_grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def blur(img, param):
    img = cv2.medianBlur(img, param)
    return img

def threshold(img):
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

def findValue(image):
    value = []
    averageValues = []
    maximumValues = []
    percentileValues = []
    # img = cv2.imread('{} - SSPL.VAL.13.02.png'.format(image))
    img = cv2.imread('./graph/{}'.format(image))

    resize = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    # convert_grayscale(img)
    # threshold(img)
    bw = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    # Resize the image
    custom_config = r'--psm 4'


    d = pytesseract.image_to_data(bw, output_type=Output.DICT, config=custom_config)
    keys = list(d.keys())

    found = 0
    # xStart = 999
    # xEnd = 999
    # yStart = 999
    

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        # print(d['text'][i], i)
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        # Average In/outbound 
            # PGAS.VAL.33.01#1 --> #56 & #67
            # PGAS.VAL.33.01#2 --> #61 & #67
        # Max In/oubound
            # PGAS.VAL.33.01#1 --> #59 & #70
            # PGAS.VAL.33.01#2 --> #59 & #70
        # 95th percentile
            # PGAS.VAL.33.01#1 --> #80
            # PGAS.VAL.33.01#2 --> #80

        # Search "Average word then +1 its index to get Average Inbound & Outbound"
        if re.search(r"\bAve\w+", d['text'][i]):
                if d['text'][i+2] == 'G':
                    averageValues.append(str(int(float((d['text'][i+1]).replace(',','.'))*1000)))
                else:
                    averageValues.append(d['text'][i+1])
                
        # Search "Maximum word then +1 its index to get Maximum Inbound & Outbound"
        if re.search(r"\bMax\w+", d['text'][i]):
                if d['text'][i+2] == 'G':
                    maximumValues.append(str(int(float((d['text'][i+1]).replace(',', '.'))*1000)))
                else:
                    maximumValues.append(d['text'][i+1])
                # print(d['text'][i+2])

        # Search "Percentile word then +2 its index to get Percentile"
        if re.search(r"\bPer\w+", d['text'][i]):
                if d['text'][i+2] == 'M':
                    percentileValues.append(d['text'][i+1])
                else:
                    percentileValues.append(d['text'][i+2])
                

        
    value.append(averageValues)
    value.append(maximumValues)
    value.append(percentileValues)
    return value

# print(findValue('./imgs/table/1 - SSPL.VAL.13.02 .png'))