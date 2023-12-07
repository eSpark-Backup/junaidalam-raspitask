from tkinter import *
import tkinter as tk
import time
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
from threading import*

PIN1 = 11
PIN2 = 13


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Global variables
button_text = []
image_array = []
text_array = []
increment_counter = 0
a=40

def work():
    while True:
        Button_A = GPIO.input(PIN1)
        Button_B = GPIO.input(PIN2)

        if (Button_A == 1):
            start = time.time()
            while True:
                time.sleep(0.02)
                if Button_A == 0:
                    time.sleep(0.01)
                    length = time.time() - start
                    if length > 2:
                        Adding()
                        break
                    else:
                        global increment_counter, a
                        string_value = Keypad_Input.get()
                        if not string_value:
                            string_value = '0'
                        button_text.append(string_value)
                        img_2=  ImageTk.PhotoImage(Image.open("label_button.png").resize((160,100)))
                        Button_Image.append(img_2)
                        image_array.append(canvas.create_image(100,a,image = Button_Image[increment_counter]))
                        canvas.tag_bind(image_array[increment_counter]) 
                        text_array.append(canvas.create_text(100,a, text="R " + button_text[increment_counter],font="lucida 20 bold",fill="white"))
                        a = a + 80
                        increment_counter += 1
                        Keypad_Input.set("")
                        screen.update()
                        break
                Button_A = GPIO.input(PIN1)

        # if GPIO.input(PIN2):
    
        elif (Button_B == 1):
            Clearing()


def threading():
    t1=Thread(target=work)
    t1.start()

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    Keypad_Input.set(Keypad_Input.get() + text)
    screen.update()

def Adding():    
    total_Sum = sum(int(value) for value in button_text)
    canvas.itemconfigure(Sum_button_text, text = "R " + str(total_Sum))
        
def Clearing():
    global increment_counter, image_array,text_array, a
    button_text.clear()
    for x in range(len(image_array)):
        canvas.delete(image_array[x])
        canvas.delete(text_array[x])
    image_array = []
    text_array=[]
    canvas.itemconfigure(Sum_button_text, text ="")
    increment_counter = 0
    a = 40


####### GUI OF 1st Screen ##############
# Set up window for display on HDMI 0
# Tkinter setup

root = Tk()

# Set resolutions of windows
w0, h0 = 800, 800
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
button_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

Keypad_Button = []
Button_Image = []
for j in range(4):
    frame = Frame(Window_1, bg="black")
    Keypad_Columns.append(frame)
    frame.pack()
    
    image=Image.open("button.png")

# Resize the image in the given (width, height)
    img=image.resize((150, 150))
    for k in range(3):
        index = 3 * j + k
        if index < 10:
            Keypad_Button.append(ImageTk.PhotoImage(img))
            roundedbutton = tk.Button(frame,image=Keypad_Button[index],text=button_labels[index], font="lucida 28 bold",compound='center', fg="white")
            roundedbutton.pack(side=LEFT,fill="y")
            roundedbutton.bind("<Button-1>", click)

for i in range(4):
    Window_1.grid_rowconfigure(i, weight=0)
    Window_1.grid_columnconfigure(i, weight=0)
    
####### GUI OF 2nd Screen ##############

# Set up window for display on HDMI 1
Window_2 = Toplevel()
Window_2.geometry(f"{w1}x{h1}+{w0}+0")
# In the canva section of Window_2
Background_image = ImageTk.PhotoImage(Image.open("party.png").resize((1366,768)))
canvas = Canvas(Window_2,width=w1 , height= h1)
canvas.pack(anchor="nw")
#Add the image in the canvas
canvas.create_image(0,0,image=Background_image, anchor="nw")
img_1=  ImageTk.PhotoImage(Image.open("sum.png").resize((500,150)))
Sum_Button_Image = canvas.create_image(800, 384, image = img_1)
canvas.tag_bind(Sum_Button_Image) 
Sum_button_text = canvas.create_text(800,384, text="",font="lucida 40 bold",fill="black")

threading()

root.withdraw()
root.mainloop()