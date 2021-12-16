import os
import numpy as np
import cv2
from glob import glob

def createdir(save_add):
    try:
        if not os.path.exists(save_add):
            os.makedirs(save_add)
    except OSError:
        print(f"Error: Crating directory with name {save_add}")

def save_frame(path,save_path,gap=30):
    name=path.split("\\")[-1].split(".")[0]
    save_add=os.path.join(save_path,name)
    createdir(save_add)
    cap=cv2.VideoCapture(path)
    idex=0
    while True:
        res,frame=cap.read()
        if res == False:
            cap.release()
            break
        elif idex ==0:
            cv2.imwrite(f"{save_path}/{idex}.png",frame)
        else:
            if idex % gap==0:
                cv2.imwrite(f"{save_path}/{idex}.png",frame)
        idex+=1



if __name__=="__main__":
    video_path=glob("video\\*")
    save_path="save"

    for path in video_path:
        save_frame(path,save_path,gap=30)
        break