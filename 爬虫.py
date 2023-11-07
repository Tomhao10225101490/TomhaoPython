 
#导入相关库
import requests
import json
import base64
import cv2
import numpy as np
from alive_progress import alive_bar
import time
 
 
while True:
    u="https://flagopen.baai.ac.cn/flagStudio/auth/getToken"
    param={"apikey":"aee3672220ec348b3b3dfaa7956a8282"}
    token_response=requests.get(url=u,params=param)
    token_json=json.loads(token_response.text)
    token=token_json['data']['token']
 
#调用api
    u = "https://flagopen.baai.ac.cn/flagStudio/v1/text2img"
    prompt=input("请输入你的创意:")
    param={"prompt":prompt,"steps":80,"style":"写实主义","width":500,"height":300}
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "token":token}
    response=requests.post(url=u,json=param,headers=header)
    print('AI正在绘画中...')
 
    img_json=json.loads(response.text)
    img=img_json['data']
    img=base64.b64decode(img)
 
 
    imgstring = np.array(img).tobytes()
    imgstring = np.asarray(bytearray(imgstring), dtype="uint8")
    image = cv2.imdecode(imgstring, cv2.IMREAD_COLOR)
    mylist = range(0,30)
    with alive_bar(len(mylist)) as bar: 
        for i in mylist: 
            bar() 
            time.sleep(0.5)
    print('绘制完成')
    cv2.imshow('result',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
