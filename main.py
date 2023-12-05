from tkinter import *
import time
import RPi.GPIO as GPIO
from threading import*

PIN = 3

PIN1 = 11
PIN2 = 13

# GPIO.setmode(GPIO.BCM)

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
        if (VAL_A == True):
            print("a")
            while True:
                GPIO.wait_for_edge(PIN1 ,GPIO.FALLING)
            # print ("Pressed")
                start = time.time()
                time.sleep(0.02)

                while GPIO.input(PIN1) == GPIO.LOW:
                    time.sleep(0.01)
                    length = time.time() - start

                    if length > 3:
                        Adding
                    else:
                        global i
                        string_value = var_1.get()
                        # int_val = int(string_value)
                        # int_value.append(int_val)
                        frame_12 = Frame(win1, bg="lightgray", borderwidth=3, relief="sunken")
                # for i in array_2:
                        frame_12.pack(fill="y", side=LEFT, anchor="nw", padx=10, pady=10)
                        # Append the value to array_2
                        array_2.append(string_value)
                        label.append(Label(frame_12, text=array_2[i], width=20, font="lucida 10 bold"))
                        label[i].pack(anchor="nw", padx=10, pady=10)
                        i += 1
                        var_1.set("")
                        screen.update()

        if GPIO.input(PIN2):
            print("b")
            Clearing

def threading():
    t1=Thread(target=work)
    t1.start()



# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    var_1.set(var_1.get() + text)
    screen.update()

def Adding(event):
    text = event.widget.cget("text")
    if text == "Clear":
        
        total = sum(int(value) for value in array_2)
        print(total)
        aman = StringVar()
        aman.set(str(total))
        screen_4.config(text=aman)
        screen_4.update()
        
def Clearing():
    # text = event.widget.cget("text")
    array_2.clear()
    label.clear()
    screen_4.config(text=" ")

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

for j in range(4):
    frame = Frame(win0, bg="gray")
    frames.append(frame)
    frame.pack()

    for k in range(3):
        index = 3 * j + k
        if index < 10:
            button = Button(frame, text=button_labels[index], padx=20, pady=5, font="lucida 28 bold")
            button.pack(side=LEFT, padx=5, pady=5)
            button.bind("<Button-1>", click)


# Set up window for display on HDMI 1
win1 = Toplevel()
win1.geometry(f"{w1}x{h1}+{w0}+0")

result = StringVar()
result.set("")

# In the Labels section of win1

frame_13 = Frame(win1, bg="lightgray", borderwidth=3, relief="sunken", height=500)
frame_13.pack(fill="y", side=TOP, anchor="ne", padx=10, pady=10)
screen_4 =Entry(frame_13,font="lucida 40 bold", textvariable="")
screen_4.pack(fill="y", padx=10, side=TOP, pady=210)

GPIO.add_event_detect(PIN1,GPIO.FALLING,callback=threading)
GPIO.add_event_detect(PIN2,GPIO.FALLING,callback=Clearing)


root.withdraw()

root.mainloop()

# TypeError: threading() takes 0 positional arguments but 1 was given