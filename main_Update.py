from tkinter import *
import time
from PIL import Image, ImageTk    # sudo apt-get install python3-pil.imagetk
from threading import*
import pygame
import os
from screeninfo import get_monitors
import tkinter.font as tkfont

PIN1 = 11 #button A
PIN2 = 13 #button_B

# Global variables
button_text = []
image_array = []
text_array = []
increment_counter = 0
# a=260
flag = 0
try:
    import RPi.GPIO as GPIO
    gpio_available = True
except ImportError:
    gpio_available = False
# if gpio_available:
#    monitors = get_monitors()
#    w1 = monitors[0].width
#    h1 = monitors[0].height
#    w0 = monitors[1].width
#    h0 = monitors[1].height
# else:
w0, h0 = 800, 480
w1, h1 = 1280, 720

# height difference between input values
inputsHeight_align = int((h1*24.7/100))
a = inputsHeight_align

def work():
    while True:
        if gpio_available:
            GPIO.setwarnings(False) 
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(PIN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(PIN2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
            Button_A = GPIO.input(PIN1)
            Button_B = GPIO.input(PIN2)
        else:
            Button_A = input()
            Button_B = 0
        if (Button_A == 1 or Button_A == "a") and (Button_B == 1 or Button_B == "b"):
            root.destroy()
        elif (Button_A == 1 or Button_A == "a" ):
                global flag,i,a,increment_counter
                global wallet,wallet_text
                Buzz_play()
                while True:
                    if ((Button_A == 1 or Button_A == "a") and flag == 0 ):
                        wallet = Keypad_Input.get()
                        if not wallet:
                            wallet = "0"
                        walWidht_size = int((w1*13/100))
                        walHeight_size = int((h1*9/100))
                    
                        wallet_image =  ImageTk.PhotoImage(Image.open(image_path +"/Images/wallet_button.png").resize((walWidht_size,walHeight_size)))
                        walWidth_align = int((w1*37/100))
                        walheight_align= int((h1*14/100))
                        walTextExtra_align= int ((w1*0.5/100))
                        bttn_1 = canvas.create_image(walWidth_align, walheight_align, image = wallet_image)
                        canvas.tag_bind(bttn_1) 
                        textFontWallet =int((w1*1.5/100))
                        font_2 = tkfont.Font(family="SuperSport Extra Black", size = textFontWallet)
                        wallet_text = canvas.create_text(walWidth_align + walTextExtra_align, walheight_align, text=" " ,font=font_2,fill="white")
                        canvas.itemconfigure(wallet_text, text = "R" + str(wallet))
                        canvas.itemconfigure(Sum_button_text, text = "R" + str(wallet))
                        flag = 1
                        Keypad_Input.set("")
                        canvas_1.itemconfigure(screen, text = Keypad_Input.get())
                        time.sleep(1)
                        break
                    elif ((Button_A == 1 or Button_A == "a") and flag!= 0):
                    # elif (Button_A == "a" and flag!= 0):
                        string_value = Keypad_Input.get()
                        if not string_value:
                            string_value = '0'
                        button_text.append(string_value)
                        InputWeidthText_align = int(w1*16/100)
                        inputs_textFont = int((w1*2.34/100))
                        font_3 = tkfont.Font( family="SuperSport HD", size = inputs_textFont)
                        text_array.append(canvas.create_text(InputWeidthText_align, a, text="R" + button_text[increment_counter], font=font_3 ,fill="white"))
                        Diffence_of_inputs_height = int((h1*17.129/100))
                        # a = a + 185
                        a = a + Diffence_of_inputs_height
                        wallet = int(wallet) - int(button_text[increment_counter])
                        canvas.itemconfigure(Sum_button_text, text = "R" + str(wallet))
                        increment_counter += 1
                        Keypad_Input.set("")
                        canvas_1.itemconfigure(screen, text = Keypad_Input.get())
                        time.sleep(1)
                        break

        # if GPIO.input(PIN2):
        elif(Button_B == 1 or Button_A == "b"):
            Clearing()


def play():
    pygame.init()
    buzz_path = os.path.dirname(os.path.realpath(__file__))
    pygame.mixer.music.load(buzz_path + '/Buzz Sound/buzz.mp3')
    # pygame.mixer.music.load('buzz.mp3')
    pygame.mixer.music.play()
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
    if text == "Clear":
        Keypad_Input.set("")
        canvas_1.itemconfigure(screen, text ="R")
    #  for backspace button
    elif text == ".":
        Back_space = Keypad_Input.get()
        Keypad_Input.set(Back_space[:-1])
        canvas_1.itemconfigure(screen, text ="R"+(Back_space[:-1]))
    else:
        keypad_Numbers = (Keypad_Input.get() + text)
        Keypad_Input.set(keypad_Numbers)
        canvas_1.itemconfigure(screen, text ="R"+ keypad_Numbers)

        
def Clearing():
    try:
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
        a = inputsHeight_align
    except Exception as e:
        print(e)


####### GUI OF 1st Screen ##############
# Set up window for display on HDMI 0
# Tkinter setup
root = Tk()
# Set up window for display on HDMI 1
Window_1 = Toplevel()
Window_1.geometry(f"{w0}x{h0}+{w1}+196")
Window_1.title("Raspberry Pi GUI")
Window_1.attributes('-fullscreen',1)
Window_1.overrideredirect(1)

####### GUI OF 2nd Screen ##############
# Set up window for display on HDMI 0
Window_2 = Toplevel()
Window_2.geometry(f"{w1}x{h1}+0+0")
Window_2.title("Display Screen")
Window_2.attributes('-fullscreen',True)

Window_2.overrideredirect(1)

Keypad_Input = StringVar()
Keypad_Input.set("")
image_path = os.path.dirname(os.path.realpath(__file__))
canvas_1 = Canvas(Window_1,width=w0 , height= h0)
canvas_1.pack(anchor="nw")
calculator_Background_image = ImageTk.PhotoImage(Image.open(image_path + "/Images/calculator_fram.jpg").resize((w0,h0)))
canvas_1.create_image(0,0,image=calculator_Background_image, anchor="nw")
calScreen_width = int((w0*50/100))
calScreen_height= int((h0*22.5/100))
Screen_text_size = int((w0*3/100))
font_4 = tkfont.Font( family="SuperSport Extra Black", size = Screen_text_size)
screen = canvas_1.create_text(calScreen_width, calScreen_height, text="R", font = font_4 ,fill="white",state="normal")
# resize image automatically
calWidth_align = int((w0*11/100))
calheight_align = int((h0*13/100))

click_btn= ImageTk.PhotoImage(Image.open(image_path + "/Images/blue_button.png").resize((calWidth_align, calheight_align)))
# bg="#121FA2"
#button align automatically according to screen resolution
calX_1_align = int((w0*33/100))
calX_2_align = int((w0*44/100))
calX_3_align = int((w0*55/100))
calY_1_align = int((h0*30/100))
calY_2_align = int((h0*44/100))
calY_3_align = int((h0*58/100))
calY_4_align = int((h0*71/100))

#Automatically change screen size 
cal_font_size = int((w0*3/100))
font_5 = tkfont.Font(family="SuperSport Extra Black", size = cal_font_size)
# button_1
btn = Button(canvas_1,image = click_btn, text='1', relief="flat", highlightthickness=0, borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E", compound="center", activebackground="#0C1B6E")
btn.place(x=calX_1_align, y=calY_1_align)
btn.place(x=calX_1_align, y=calY_1_align)
btn.bind("<Button-1>", click)
#button_2
btn = Button(canvas_1,image = click_btn, text='2', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_2_align, y=calY_1_align)
btn.bind("<Button-1>", click)
#button_3
btn = Button(canvas_1,image = click_btn, text='3', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_3_align, y=calY_1_align)
btn.bind("<Button-1>", click)

#button_4
btn = Button(canvas_1,image = click_btn, text='4', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_1_align, y=calY_2_align)
btn.bind("<Button-1>", click)

#button_5
btn = Button(canvas_1,image = click_btn, text='5', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_2_align, y=calY_2_align)
btn.bind("<Button-1>", click)

#button_6
btn = Button(canvas_1,image = click_btn, text='6', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_3_align, y=calY_2_align)
btn.bind("<Button-1>", click)

#button_7
btn = Button(canvas_1,image = click_btn, text='7', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_1_align, y=calY_3_align)
btn.bind("<Button-1>", click)

#button_8
btn = Button(canvas_1,image = click_btn, text='8', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_2_align, y=calY_3_align)
btn.bind("<Button-1>", click)

#button_9
btn = Button(canvas_1,image = click_btn, text='9', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_3_align, y=calY_3_align)
btn.bind("<Button-1>", click)

#button_clear
clear_textFont = int((w0*1.7/100))
font_6 = tkfont.Font( family="SuperSport Extra Black", size = clear_textFont)
btn = Button(canvas_1,image = click_btn, text='Clear', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_6, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_1_align, y=calY_4_align)
btn.bind("<Button-1>", click)

#button_0
btn = Button(canvas_1,image = click_btn, text='0', relief="flat", highlightthickness=0,  borderwidth= 0, font=font_5, fg="white", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
btn.place(x=calX_2_align, y=calY_4_align)
btn.bind("<Button-1>", click)

#button_backspace
calWidthImage_align = int((w0*9/100))
calheightImage_align = int((h0*12.5/100))
click_btn_1= ImageTk.PhotoImage(Image.open(image_path + "/Images/backspace.png").resize((calWidthImage_align ,calheightImage_align)))
btn = Button(canvas_1,image = click_btn_1, text='.', relief="flat", highlightthickness=0,  borderwidth= 0, font="lucida 7 bold", fg="#0C1B6E", bg="#0C1B6E",compound="center",activebackground="#0C1B6E")
calX_4_align = int(w0*56.5/100)
calY_4_align_bacspace = int(h0*71.5/100)
btn.place(x=calX_4_align, y=calY_4_align_bacspace)
btn.bind("<Button-1>", click)

####### GUI OF 2nd Screen ##############

# In the canva section of Window_2
Background_image = ImageTk.PhotoImage(Image.open(image_path + "/Images/new_display2.jpg").resize((w1,h1)))
canvas = Canvas(Window_2,width=w1 , height= h1)
canvas.pack(anchor="nw")

# substracting text alignment
sumTextwidht_align = int((w1*62/100))
sumTextheight_align= int((h1*49/100))

# text of substracting values
canvas.create_image(0,0,image=Background_image, anchor="nw")
textFont = int((w1*7/100))
font_1 = tkfont.Font(family="SuperSport HD", size = textFont)
Sum_button_text = canvas.create_text(sumTextwidht_align, sumTextheight_align, text="", font=font_1, fill="white")

threading()

root.withdraw()
root.mainloop()