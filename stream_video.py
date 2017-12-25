import requests
import json
import cv2
from pivideostream import PiVideoStream
import numpy as np
import base64

addr = 'http://192.168.0.6:5000'
test_url = addr + '/api/test'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

video_capture = PiVideoStream().start()

while True:
    try:
        frame = video_capture.read()
        #print(frame)
        _,img_encoded = cv2.imencode('.jpg',frame)
        response = requests.post(test_url,data=img_encoded.tostring(),headers=headers)
        str_response = json.loads(response.text)
        arr = np.fromstring(base64.b64decode(str_response['message']['py/b64']),dtype=np.uint8)
        img = cv2.imdecode(arr,-1)
        print(img)
        cv2.imshow('frame',img) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        pass
