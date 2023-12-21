# Projecy Name: Super Sport

## GUI Using Tkinter on Raspberry Pi-4
## 1- Import Libraries:
### If using raspberry pi then install the library.
1- `sudo apt-get install python3-pil`  `sudo apt-get install python3-pil.imagetk`  
2- `sudo apt-get install threading` <br/>
3- `sudo apt-get install python3-pygame`   
4- `sudo apt-get install python3-screeninfo` <br/>
5- `sudo apt-get install python3-tk`
## How to Install Library? <br/>
![Image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/library%20install.PNG)
# Code-1
### After installing all libraries import all commands in the code as shown in the picture.
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/library_1.png)

## 2- Adding Fonts file in the Folder
### Add `SuperSport-BlackItalic.ttf` and `SuperSport-BoldItalic.ttf` fonts file in the folder of .font
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_addFolder.PNG)
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_paste.PNG)

## 3- Set GPIO's.
### `PIN 11` set input pin for Button_A and `PIN 13` set input pin for Button_B.

## 4- 19" and 7" Connection with raspberry pi 4 through HDMI.
### Make sure the 19" screen should be connected `with HDMI_0` port and 7" screen connect with `HDMI_1` port of `Raspberry pi 4`. 
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/fritzing.png)

## 5- Code Discribtion.
### Automatically detect GPIO Setup and Screen Resolution.
Automatically detect if Raspberry Pi-4 is connected then setup the GPIO, Input taking from the GPIO Button_A(PIN 11) and Button_B(PIN 13) otherwise take input from the computer keyboard "a" for adding values and "b" for the clearing all values. Same for the screen resolution if Raspi 4 connected with both screen so it automatically detect the resolution and detected first resolution for 7" touch screen while second resolution for 19" screen display. 

![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/3979d360-82f1-454f-99c9-71bd0b20d404)
### Add value in Wallet.
First inserting input value save in wallet and Reference Wallet.
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/c7690e43-6f75-463d-a18d-f8881f63cf86)

Second inserting input values save in **list**, and substracte from value of **reference wallet** and the result save in **reference wallet**. 

![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/2fabef47-283d-4fbe-824e-e4acf36303d0)
