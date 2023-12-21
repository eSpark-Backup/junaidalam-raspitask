# Projecy Name: Super Sport

## GUI Using Tkinter on Raspberry Pi-4
## 1- Import Libraries:
1.0- If using raspberry pi then install the library.  

1- `sudo apt-get install python3-pil`  `sudo apt-get install python3-pil.imagetk`  
2- `sudo apt-get install threading` <br/>
3- `sudo apt-get install python3-pygame`   
4- `sudo apt-get install python3-screeninfo` <br/>
5- `sudo apt-get install python3-tk`

## 1.1- How to Install Library? <br/>
![Image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/library%20install.PNG)

# 1.2- Code-1
After installing all libraries import all commands in the code as shown in the picture.
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/library_1.png)

## 2- Adding Fonts file in the Folder
Add `SuperSport-BlackItalic.ttf` and `SuperSport-BoldItalic.ttf` fonts file in the folder of .font
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_addFolder.PNG)
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/font_paste.PNG)

## 3- Set GPIO's.
`PIN 11` and `PIN 13` are set input pin for Button_A and Button_B.

## 4- 19" and 7" Connection with raspberry pi 4 through HDMI.
Make sure the 19" screen should be connected `with HDMI_0` port and 7" screen connect with `HDMI_1` port of `Raspberry pi 4`. 
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/blob/main/extra/fritzing.png)

## 5 : Code Discribtion.
Automatically detect GPIO Setup and Screen Resolution.
Automatically detect if Raspberry Pi-4 is connected then setup the GPIO, Input taking from the GPIO Button_A(PIN 11) for inserting value and Button_B(PIN 13) for clearing the display value on secong screen otherwise take input from the computer keyboard "a" and "b" instead of Button_A(PIN 11) and Button_b(PIN 13) respectivlly. Same for the screen resolution if Raspi 4 connected with both screen so it automatically detect the resolution and detected first resolution for 7" touch screen while second resolution for 19" screen display. 

## 6: For Button A:

### 6.0: Inserting Inputs  
 Through 7" Touch screen insert the value and press Button_A(PIN 11). If no value insert and input button_A(PIN 11) pressed so by default **"0"** insert. 
### First Input.
6.1 : First inserting input value save in wallet and Reference Wallet.
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/5779017e-31ff-4456-9f1b-cce7acd7b2ae)
### Continously Given Input not more than 4 times.  
6.2 : Second inserting input values save in **list**, and substracte from value of **reference wallet** and the result save in **reference wallet**. 
![image](https://github.com/eSpark-Consultants/junaidalam-raspitask/assets/146022877/2bce2762-3f27-4e14-9bc1-5958b2d06066)

## 7.0 : For Button B:
 After inserting the values, When Button_B(PIN13) is pressed all the values clear and empty. And program again ready for re-inserting the values.

## 8.0 File Required:
Place the same code and these file on the same folder.
**`buzz.mp3`** **`backspace.png`** **`blue_button.png`**  **`calculator_fram.jpg`** **`new_display2.jpg`** **`wallet_button.png`** **`SuperSport-BlackItalic.ttf`** **`SuperSport-BoldItalic.ttf`** .



