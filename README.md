# Super Sport

## GUI Using Tkinter on Raspberry Pi-4
## 1- Import Libraries:
### If using raspberry pi than intall the library by given commands with the libaries.
1- from tkinter import *     
2- import time            <br />
3- from PIL import Image, ImageTk  ------`sudo apt-get install python3-pil`  `sudo apt-get install python3-pil.imagetk`  
4- from threading import*    ---------------`sudo apt-get install threading` <br/>
5- import pygame    -------------- ---------`sudo apt-get install python3-pygame` <br/>
6- import os       
7- from screeninfo import get_monitors --`sudo apt-get install python3-screeninfo` <br/>
8- import tkinter.font as tkfont -----------`sudo apt-get install python3-tk`

## How to Install Library? <br/>
![Image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/library%20install.PNG)


## 2- Adding Fonts file in the Folder
### Add `SuperSport-BlackItalic.ttf` and `SuperSport-BoldItalic.ttf` fonts file in the folder of .font
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_addFolder.PNG)
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_paste.PNG)

##3- Set GPIO's.
`PIN 11` set input pin for Button_A and `PIN 13` set input pin for Button_B.
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/connection%20Fritzing.png)
