# Projecy Name: Super Sport

## GUI Using Tkinter on Raspberry Pi-4
## 1- Import Libraries: 

1- `sudo apt-get install python3-pil`  `sudo apt-get install python3-pil.imagetk`  
2- `sudo apt-get install threading` <br/>
3- `sudo apt-get install python3-pygame`   
4- `sudo apt-get install python3-screeninfo` <br/>
5- `sudo apt-get install python3-tk`

## 1.1- How to Install Library? <br/>
![Image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/library%20install.PNG)

## 2- Adding Fonts file in the Folder
Add `SuperSport-BlackItalic.ttf` and `SuperSport-BoldItalic.ttf` fonts file in the folder of .font
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_addFolder.PNG)
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_paste.PNG)

## 3- Connections of GPIO's.
`PIN 11` and `PIN 13` are Raspberry pi-4 GPIO's, set input pin for Button_A and Button_B.

## 4- 19" and 7" Connection with raspberry pi 4 through HDMI.
Make sure the 19" screen should be connected `with HDMI_0` port and 7" screen connect with `HDMI_1` port of `Raspberry pi 4`. 
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/fritzing.png)

## 5 : How Program Works?
### Automatically detect GPIO Setup and Screen Resolution.
When the program run two window will appears, Inputs taken from the keypad Screen and then press Button A for save inserted values in wallet and reference Wallet, again insert value and press button A, then it start storing in list and minus from reference wallet. While Button B for clearing the display values on second screen. For the screen resolution, Raspi 4 connected with both screen so it automatically detect the resolutions and detected first resolution for 7" touch screen while second resolution for 19" screen display. 
## Screen_1:
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/f5c63240-4652-4b65-aaf8-68bf10a7a90c)
## Screen_2:
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/0180062a-f0d3-4c61-8aa1-9fa9a2c8bddc)

## 6: For Button A:
### 6.0: Inserting Inputs  
 Through 7" Touch screen insert the value and press Button A. If no value insert and input button A pressed so by default **"0"** insert.
 ![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/1fea000a-5032-495e-8879-88187845b194)
 
### First Input.
6.1 : First inserting input value save in wallet and Reference Wallet.

### Continously Given Input not more than 4 times.  
6.2 : Second inserting input values save in **list**, and substracte from value of **reference wallet** and the result save in **reference wallet**. 
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/2bce2762-3f27-4e14-9bc1-5958b2d06066)

## 7.0 : For Button B:
 After inserting the values, When Button B is pressed all the values clear and empty. And program again ready for re-inserting the values.

## 8.0 Folders Required:
Place these folders and main code on the same folder. 
 **`Images`** **`Fonts`** **`Buzz Sound`**



