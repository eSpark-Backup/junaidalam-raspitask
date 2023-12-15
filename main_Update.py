from tkinter import *
import tkinter as tk
import time
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
from threading import*
import pygame
import os

PIN1 = 11 #button A
PIN2 = 13 #button_B

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# Global variables
button_text = []
image_array = []
text_array = []
increment_counter = 0
a=260
flag = 0

def work():
    while True:

        Button_A = GPIO.input(PIN1)
        Button_B = GPIO.input(PIN2)
        # Button_A = input()
        if (Button_A == 1):
        # if (Button_A == "a"):
            global flag,i,a,increment_counter
            global wallet,wallet_text
            Buzz_play()
            while True:
                if (Button_A == 1 and flag == 0 ):
                    wallet = Keypad_Input.get()
                    if not wallet:
                        wallet = "0"
                    wallet_image=  ImageTk.PhotoImage(Image.open(image_path +"/wallet_button.png").resize((250,100)))
                    bttn_1 = canvas.create_image(750, 150, image = wallet_image)
                    canvas.tag_bind(bttn_1) 
                    wallet_text = canvas.create_text(760,150, text="",font="lucida 30 bold",fill="white")
                    canvas.itemconfigure(wallet_text, text = "R " + str(wallet))
                    canvas.itemconfigure(Sum_button_text, text = "R " + str(wallet))
                    flag = 1
                    Keypad_Input.set("")
                    canvas_1.itemconfigure(screen, text = Keypad_Input.get())
                    time.sleep(1)
                    break

                elif (Button_A == 1 and flag!= 0):
                # elif (Button_A == "a" and flag!= 0):
                    string_value = Keypad_Input.get()
                    if not string_value:
                        string_value = '0'
                    button_text.append(string_value)
                    text_array.append(canvas.create_text(300,a, text="R " + button_text[increment_counter],font="lucida 45 bold",fill="white"))
                    a = a + 185
                    wallet = int(wallet) - int(button_text[increment_counter])
                    canvas.itemconfigure(Sum_button_text, text = "R " + str(wallet))
                    increment_counter += 1
                    Keypad_Input.set("")
                    canvas_1.itemconfigure(screen, text = Keypad_Input.get())
                    time.sleep(1)
                    break
           

        # if GPIO.input(PIN2):
    
        elif(Button_B == 1):
        # elif(Button_A == "b"):
            Clearing()
def play():
    pygame.init()
    pygame.mixer.music.load('buzz.mp3')
    pygame.mixer.music.play()
# Add a delay to allow the sound to play before the program exits
    pygame.time.delay(5000)
def Buzz_play():
    t2=Thread(target=play)
    t2.start()


def threading():
    t1=Thread(target=work)
    t1.start()

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    
    print(text)
    if text == "Clear":
        Keypad_Input.set("")
        canvas_1.itemconfigure(screen, text ="")

    elif text == " Backspace":
        Back_space = Keypad_Input.get()
        Keypad_Input.set(Back_space[:-1])
        canvas_1.itemconfigure(screen, text = (Back_space[:-1]))

    else:
        keypad_Numbers = (Keypad_Input.get() + text)
        Keypad_Input.set(keypad_Numbers)
        canvas_1.itemconfigure(screen, text = keypad_Numbers)

        
def Clearing():
    global increment_counter, image_array,text_array, a, i,wallet,flag,button_text
    for x in range(len(button_text)):
        canvas.delete(button_text[x])
        canvas.delete(text_array[x])
    
    text_array=[]
    button_text =[]
    canvas.itemconfigure(Sum_button_text, text ="")
    canvas.itemconfigure(wallet_text, text = "")
    canvas.itemconfigure(button_text, text = "")
    increment_counter = 0
    i = 0
    flag = 0
    wallet= 0
    a = 80


####### GUI OF 1st Screen ##############
# Set up window for display on HDMI 0
# Tkinter setup

root = Tk()

# Set resolutions of windows
w0, h0 = 1280, 720
w1, h1 = 1920,1080

# Set up window for display on HDMI 0
Window_1 = Toplevel()
Window_1.geometry(f"{w0}x{h0}+0+0")
Window_1.title("Raspberry Pi GUI")

Keypad_Input = StringVar()
Keypad_Input.set("")
image_path = os.path.dirname(os.path.realpath(__file__))
canvas_1 = Canvas(Window_1,width=w0 , height= h0)
canvas_1.pack(anchor="nw")
calculator_Background_image = ImageTk.PhotoImage(Image.open(image_path + "/calculator_fram.jpg").resize((w0,h0)))
canvas_1.create_image(0,0,image=calculator_Background_image, anchor="nw")

screen = canvas_1.create_text(645, 160, text="",font="lucida 40 bold",fill="white")
# canvas_1.itemconfigure(screen, text = Keypad_Input)

click_btn= ImageTk.PhotoImage(Image.open(image_path + "/blue_button.png").resize((140,90)))
# bg="#121FA2"

# button_1
btn = Button(canvas_1,image = click_btn, text='1', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=425, y=215)
btn.bind("<Button-1>", click)
#button_2
btn = Button(canvas_1,image = click_btn, text='2', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=570, y=215)
btn.bind("<Button-1>", click)
#button_3
btn = Button(canvas_1,image = click_btn, text='3', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=710, y=215)
btn.bind("<Button-1>", click)

#button_4
btn = Button(canvas_1,image = click_btn, text='4', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=425, y=315)
btn.bind("<Button-1>", click)

#button_5
btn = Button(canvas_1,image = click_btn, text='5', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=570, y=315)
btn.bind("<Button-1>", click)

#button_6
btn = Button(canvas_1,image = click_btn, text='6', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=710, y=315)
btn.bind("<Button-1>", click)

#button_7
btn = Button(canvas_1,image = click_btn, text='7', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=425, y=415)
btn.bind("<Button-1>", click)

#button_8
btn = Button(canvas_1,image = click_btn, text='8', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=570, y=415)
btn.bind("<Button-1>", click)

#button_9
btn = Button(canvas_1,image = click_btn, text='9', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=710, y=415)
btn.bind("<Button-1>", click)

#button_clear
btn = Button(canvas_1,image = click_btn, text='Clear', relief="flat", borderwidth= 0, font="lucida 22 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=425, y=510)
btn.bind("<Button-1>", click)

#button_0
btn = Button(canvas_1,image = click_btn, text='0', relief="flat", borderwidth= 0, font="lucida 27 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=570, y=510)
btn.bind("<Button-1>", click)

#button_backspace
btn = Button(canvas_1,image = click_btn, text=' Backspace', relief="flat", borderwidth= 0, font="lucida 12 bold", fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=710, y=510)
btn.bind("<Button-1>", click)

####### GUI OF 2nd Screen ##############

# Set up window for display on HDMI 1
Window_2 = Toplevel()
Window_2.geometry(f"{w1}x{h1}+{w0}+0")
# In the canva section of Window_2
Background_image = ImageTk.PhotoImage(Image.open(image_path + "/new_display2.jpg").resize((w1,h1)))
canvas = Canvas(Window_2,width=w1 , height= h1)
canvas.pack(anchor="nw")
#Add the image in the canvas
canvas.create_image(0,0,image=Background_image, anchor="nw")
Sum_button_text = canvas.create_text(1200,530, text="",font="SuperSport 90 bold",fill="white")

threading()

root.withdraw()
root.mainloop()
