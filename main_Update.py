from tkinter import *
import tkinter as tk
import time
from PIL import Image,ImageTk
import RPi.GPIO as GPIO
from threading import*



PIN1 = 11
PIN2 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Global variables
int_value = []
array_2 = []
label = []
i = 0

def work():
    while True:
        VAL_A = GPIO.input(PIN1)
        VAL_B = GPIO.input(PIN2)

        if (VAL_A == True):
            while True:
                GPIO.wait_for_edge(PIN1 ,GPIO.FALLING)
                start = time.time()
                time.sleep(0.02)
                while VAL_A == False:
                    time.sleep(0.01)
                    length = time.time() - start
                    if length > 3:
                        Adding()
                    else:
                        global i
                        string_value = var_1.get()
                        array_2.append(string_value)        # Append the value to array_2
                        image= Image.open('label_button.png')
                        img_2= image.resize((160, 100))
                        labelimage.append(ImageTk.PhotoImage(img_2))
                        label.append(Button(frame_12,image=labelimage[i],text=array_2[i], font="lucida 10 bold",compound='center', fg="white"))
                        label[i].pack(anchor="nw", padx=5, pady=5)
                        i += 1
                        var_1.set("")
                        screen.update()

        # if GPIO.input(PIN2):
    
        elif (VAL_B == True):
            Clearing()


def threading():
    t1=Thread(target=work)
    t1.start()

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    var_1.set(var_1.get() + text)
    screen.update()

def Adding():    
    total = sum(int(value) for value in array_2)
    aman = StringVar()
    aman.set(str(total))
    screen_4.config(text=aman)
    screen_4.update()
        
def Clearing():
    global i, label
    array_2.clear()
    for x in range(len(label)):
        label[x].destroy()
    label = []
    aman = StringVar()
    aman.set("")
    screen_4.configure(text=aman)
    screen_4.update()
    i = 0


####### GUI OF 1st Screen ##############
# Set up window for display on HDMI 0
# Tkinter setup
root = Tk()

# Set resolutions of windows
w0, h0 = 800, 800
w1, h1 = 600, 515

# Set up window for display on HDMI 0
win0 = Toplevel()
win0.geometry(f"{w0}x{h0}+0+0")
win0.title("Raspberry Pi GUI")

var_1 = StringVar()
var_1.set("")
screen = Entry(win0, textvar=var_1, font="lucida 40 bold")
screen.pack(fill="x", ipadx=20, padx=10, pady=10)

# Create number buttons in frames
frames = []
button_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

loadimage = []
labelimage = []
for j in range(4):
    frame = Frame(win0, bg="black")
    frames.append(frame)
    frame.pack()
    
    image=Image.open('button.png')

# Resize the image in the given (width, height)
    img=image.resize((150, 150))
    for k in range(3):
        index = 3 * j + k
        if index < 10:
            loadimage.append(ImageTk.PhotoImage(img))
            roundedbutton = tk.Button(frame,image=loadimage[index],text=button_labels[index], font="lucida 28 bold",compound='center', fg="white")
            roundedbutton.pack(side=LEFT,fill="y")
            roundedbutton.bind("<Button-1>", click)

for i in range(4):
    win0.grid_rowconfigure(i, weight=0)
    win0.grid_columnconfigure(i, weight=0)
    
####### GUI OF 2nd Screen ##############

# Set up window for display on HDMI 1
win1 = Toplevel()
win1.geometry(f"{w1}x{h1}+{w0}+0")

result = StringVar()
result.set("")

# In the Labels section of win1
frame_12 = Frame(win1, bg="white", borderwidth=3, relief="sunken")
frame_12.pack(fill="y", side=LEFT, anchor="nw", padx=10, pady=10)

frame_13 = Frame(win1, bg="lightgray", borderwidth=3, relief="sunken", height=500)
frame_13.pack(fill="y", side=TOP, anchor="ne", padx=10, pady=10)
screen_4 =Entry(frame_13,font="lucida 40 bold", textvariable="")
screen_4.pack(fill="y", padx=10, side=TOP, pady=210)

threading()

root.withdraw()

root.mainloop()