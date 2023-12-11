from tkinter import *
import tkinter as tk
import time
from PIL import Image, ImageTk
import RPi.GPIO as GPIO  # when using without Raspberry pi comment this line
from threading import *
import pygame
import os

PIN1 = 11
PIN2 = 13

GPIO.setwarnings(False)  # when using without Raspberry pi comment this line
GPIO.setmode(GPIO.BOARD)  # when using without Raspberry pi comment this line
GPIO.setup(PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # when using without Raspberry pi comment this line
GPIO.setup(PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # when using without Raspberry pi comment this line

# Global variables
button_text = []
image_array = []
text_array = []
increment_counter = 0
a = 80
flag = 0


def work():
    while True:

        Button_A = GPIO.input(PIN1)  # when using without Raspberry pi comment this line
        Button_B = GPIO.input(PIN2)  # when using without Raspberry pi comment this line
        # Button_A = input()                           # when using without Raspberry pi  remove the comment of this line    
        if (Button_A == 1):  # when using without Raspberry pi comment this line
            # if (Button_A == "a"):                        # when using without Raspberry pi  remove the comment of this line
            global flag, i, a, increment_counter
            global wallet, wallet_text
            while True:
                if (Button_A == 1 and flag == 0):  # when using without Raspberry pi comment this line
                    # if (Button_A == "a" and flag == 0 ): # when using without Raspberry pi  remove the comment of this line
                    wallet = Keypad_Input.get()
                    if not wallet:
                        wallet = "0"
                    wallet_image = ImageTk.PhotoImage(Image.open(image_path + "/wallet.png")).resize((350, 250))
                    bttn_1 = canvas.create_image(550, 100, image=wallet_image)
                    canvas.tag_bind(bttn_1)
                    wallet_text = canvas.create_text(580, 90, text="", font="lucida 20 bold", fill="white")
                    canvas.itemconfigure(wallet_text, text="R " + str(wallet))
                    canvas.itemconfigure(Sum_button_text, text="R " + str(wallet))
                    flag = 1
                    Keypad_Input.set("")
                    screen.update()
                    time.sleep(1)
                    break

                elif (Button_A == 1 and flag != 0):  # when using without Raspberry pi comment this line
                    # elif (Button_A == "a" and flag!= 0):          # when using without Raspberry pi  remove the comment of this line

                    string_value = Keypad_Input.get()
                    if not string_value:
                        string_value = '0'
                    button_text.append(string_value)
                    img_2 = ImageTk.PhotoImage(Image.open(image_path + "/label_button.png")).resize((160, 100))
                    Button_Image.append(img_2)
                    image_array.append(canvas.create_image(190, a, image=Button_Image[increment_counter]))
                    canvas.tag_bind(image_array[increment_counter])
                    text_array.append(
                        canvas.create_text(190, a, text="R " + button_text[increment_counter], font="lucida 20 bold",
                                           fill="white"))
                    a = a + 80
                    wallet = int(wallet) - int(button_text[increment_counter])
                    canvas.itemconfigure(Sum_button_text, text="R " + str(wallet))
                    increment_counter += 1
                    Keypad_Input.set("")
                    screen.update()
                    time.sleep(1)
                    break


        # if GPIO.input(PIN2):

        elif (Button_B == 1):  # when using without Raspberry pi comment this line
            # elif(Button_A == "b"):                          # when using without Raspberry pi  remove the comment of this line
            Clearing()


def play():
    pygame.init()
    pygame.mixer.music.load('buzz.mp3')
    pygame.mixer.music.play()
    # Add a delay to allow the sound to play before the program exits
    pygame.time.delay(5000)
    # playsound("buuz_sound.mp3")


def Buzz_play():
    t2 = Thread(target=play)
    t2.start()


def threading():
    t1 = Thread(target=work)
    t1.start()


# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "Clear":
        Keypad_Input.set("")
    elif text == "Back":
        Back_space = Keypad_Input.get()
        Keypad_Input.set(Back_space[:-1])
        screen.update()
    else:
        Keypad_Input.set(Keypad_Input.get() + text)
        screen.update()


def Clearing():
    global increment_counter, image_array, text_array, a, i, wallet, flag
    button_text.clear()
    for x in range(len(image_array)):
        canvas.delete(image_array[x])
        canvas.delete(text_array[x])
    image_array = []
    text_array = []
    canvas.itemconfigure(Sum_button_text, text="")
    canvas.itemconfigure(wallet_text, text="")
    increment_counter = 0
    i = 0
    flag = 0
    wallet = 0
    a = 80


####### GUI OF 1st Screen ##############
# Set up window for display on HDMI 0
# Tkinter setup

root = Tk()

# Set resolutions of windows
w0, h0 = 500, 700
w1, h1 = 1366, 768

# Set up window for display on HDMI 0
Window_1 = Toplevel()
Window_1.geometry(f"{w0}x{h0}+0+0")
Window_1.title("Raspberry Pi GUI")

Keypad_Input = StringVar()
Keypad_Input.set("")
screen = Entry(Window_1, textvar=Keypad_Input, font="lucida 40 bold")
screen.pack(fill="x", ipadx=20, padx=10, pady=10)

# Create number buttons in Keypad_Column
Keypad_Columns = []
button_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Clear", "0", "Back"]
image_path = os.path.dirname(os.path.realpath(__file__))
Keypad_Button = []
Button_Image = []
for j in range(4):
    frame = Frame(Window_1, bg="black")
    Keypad_Columns.append(frame)
    frame.pack()
    image = Image.open(image_path + "/button.png")

    # Resize the image in the given (width, height)
    img = image.resize((150, 150))
    for k in range(3):
        index = 3 * j + k
        if index < 12:
            Keypad_Button.append(ImageTk.PhotoImage(img))
            roundedbutton = tk.Button(frame, image=Keypad_Button[index], text=button_labels[index],
                                      font="lucida 28 bold", compound='center', fg="white")
            roundedbutton.pack(side=LEFT, fill="y")
            roundedbutton.bind("<Button-1>", click)

# for i in range(4):
#     Window_1.grid_rowconfigure(i, weight=0)
#     Window_1.grid_columnconfigure(i, weight=0)

####### GUI OF 2nd Screen ##############

# Set up window for display on HDMI 1
Window_2 = Toplevel()
Window_2.geometry(f"{w1}x{h1}+{w0}+0")
# In the canva section of Window_2
Background_image = ImageTk.PhotoImage(Image.open(image_path + "/party.png")).resize((1366, 768))
border_image = ImageTk.PhotoImage(Image.open(image_path + "/peakpx.png")).resize((410, 768))
border_image_2 = ImageTk.PhotoImage(Image.open(image_path + "/2.png")).resize((1150, 768))
canvas = Canvas(Window_2, width=w1, height=h1)
canvas.pack(anchor="nw")
# Add the image in the canvas
canvas.create_image(0, 0, image=Background_image, anchor="nw")
canvas.create_image(350, 0, image=border_image_2, anchor="nw")
canvas.create_image(-40, 0, image=border_image, anchor="nw")
img_1 = ImageTk.PhotoImage(Image.open(image_path + "/sum.png")).resize((400, 120))
Sum_Button_Image = canvas.create_image(880, 384, image=img_1)
canvas.tag_bind(Sum_Button_Image)
Sum_button_text = canvas.create_text(880, 384, text="", font="lucida 40 bold", fill="black")

threading()

root.withdraw()
root.mainloop()
