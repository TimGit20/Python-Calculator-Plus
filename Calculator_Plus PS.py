from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tm
import os
import time
import tempfile
from tkinter import filedialog
from math import *
import turtle
from PIL import Image, ImageGrab
import datetime as dt
import subprocess
import platform
import random

#test
window = Tk()

window.title("Welcome to My Python Calculator Plus Program")

window.geometry('870x600+100+100')

# Variables
Bin_output =""
Hex_output =""
date = dt.datetime.now()
var = IntVar()
var.set(1)
var1= IntVar()
var2= IntVar()
var3= IntVar()

Temp_Type ="Not Selected"
Tvar=IntVar()
Tvar.set(1)
Temp_Type="K"   
Temp="60"
Plot_Axis_Line_Colour="black"
      


def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def Help_WINDOW():
   helpwin = Toplevel(window)
   helpwin.geometry("250x100")
   hbutton = Button(helpwin, text="Real Men! don't need a manual")
   hbutton.pack()
   Add_to_Log("Help Accessed"+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

def Display_About():
   filewin = Toplevel(window)
   filewin.geometry("250x100")
   button = Button(filewin, text="Calculator Plus \n Written in Python using tKinter \n by Tim Watkins Jan 2021")
   button.pack()
   Add_to_Log("Display About ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

def Do_End():
    Answer = tm.askquestion("Are You Sure", "Do you wish to close Calculator")
    
    if Answer == "yes" :
        window.quit()
        window.destroy()

def btnClearPlot():
   w.delete("all")

def btnRt_TxtClear_pressed():
   rightText.delete(1.0,END)
        
def sel():
   selection = str(var.get())
   
   if selection =="1":
      w.config(bg="blue")

   if selection =="2":
      w.config(bg="red")
      Plot_Axis_Line_Colour="black"
      Draw_Plot()

   if selection=="3":
      w.config(bg="white")
      
   if selection=="4":
      w.config(bg="yellow")

   if selection=="5":
      w.config(bg="green")

   if selection=="6":
      w.config(bg="grey98")

   if selection=="7":
      w.config(bg="grey90")

   window.update()

### Main Frames ###

frame = Frame(window)


rightframe = Frame(window)



rightText = Text(rightframe, height=22, width=40,padx=2,pady=2, foreground ="white",background="Grey")
rightText.grid(column=0,row=1,columnspan=2)

rightframe.config(background="lightgrey",height =20)

leftFrame = Frame(window,relief= RAISED, borderwidth=2,height=17)
bottomframe = Frame(window)

lbframe = Frame(leftFrame)
lbframe.pack()
lbframe.config(height=20, width=200)



scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )
scrollbar.config( command = rightText.yview )
var.set(3)

lb1= Radiobutton(lbframe,text=" Blue ",variable=var,value=1,command=sel).pack(side="left")
lb2= Radiobutton(lbframe,text=" Red ",variable=var,value=2,command=sel).pack(side="left")
lb3= Radiobutton(lbframe,text=" White ",variable=var,value=3,command=sel).pack(side="left")
lb4= Radiobutton(lbframe,text=" Yellow ",variable=var,value=4,command=sel).pack(side="left")
lb5= Radiobutton(lbframe,text=" Green ",variable=var,value=5,command=sel).pack(side="left")
lb6= Radiobutton(lbframe,text=" LGrey ",variable=var,value=6,command=sel).pack(side="left")
lb7= Radiobutton(lbframe,text=" Gray ",variable=var,value=7,command=sel).pack(side="left")

txt = Entry(frame, width=55,font=("Calibri",12),borderwidth=2)
txt.grid(padx=3,pady=3,column=2,row=0,columnspan=8)


def Open_Log_File():
   lwin = Toplevel(window)
   lFrame = Frame(lwin)
   lFrame.config(relief= RAISED, borderwidth=2)
   Add_to_Log("Log File Opened ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")
   textfile= Text(lFrame,width=100,font=("Calibri",12))
   textfile.pack(side= "top",padx=10,pady=10)

   txtscroll = Scrollbar(lwin)
   txtscroll.pack( side = RIGHT, fill = Y )
   txtscroll.config( command = textfile.yview )

   
    # Read File to the end of file              

   lfile = open('Calculator.log', 'r')
   Logtext = lfile.read()
   # copy into textbox
   
   textfile.insert(END,Logtext)
   
   # Close the file
   lfile.close()  

   button = Button(lFrame, text="Calculator Plus Browser\n Written in Python using tKinter \n by Tim Watkins Jan 2021")
   button.pack()
   lFrame.pack()

def btnPlot_Ok_pressed():
   PL = window.Plot_Entry.get()
   btnTxtClear_pressed()
   txt.insert(INSERT,PL)
   Draw_Plot()
   #child_window_plot.destroy()
   

   

def paint(event):
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)


canvas_width = 500
canvas_height = 340

w = Canvas(leftFrame,
           width=canvas_width,
           height=canvas_height,
           bg="white", relief=GROOVE)
w.pack(expand=YES, fill=BOTH, padx=4,pady=4)
w.bind("<B1-Motion>", paint)

message = Label(leftFrame, text="Press and Drag the mouse to draw\n Calculator Plus program and design by Tim Watkins (c) Jan 2021")
message.pack(side=BOTTOM)

def generate_pdf():
        w.postscript(file="tmp.ps", colormode='color')
        process = subprocess.Popen(["ps2pdf", "tmp.ps", "result.pdf"], shell=True)
        window.update()
        process.wait()
        #os.remove("tmp.ps")
        


def Temp_converter_window():

   def Do_SetFocus():
      window.focus_force()
      Temp_win.destroy()

   def temp_converter():
      Temp = Tentry.get()
      window.update()
      CorF = str(Tvar.get())
      print(CorF+" TEMP = "+Temp)
      fahrenheit=float()
      celsius= float()
      
      if CorF == "1":
         fahrenheit = eval(Temp)
         celsius = round(((fahrenheit - 32) / 1.8),3)
         Temp_Type = ("Temp "+str(fahrenheit )+" Fahrenheit = " +str(celsius)+ " Celsius.")
      
      if CorF == "2":
         celsius = eval(Temp)
         fahrenheit = round(((celsius * 1.8) +32),3)
         Temp_Type = ("Temp "+str(celsius) +" Celsius = " +str(fahrenheit)+ " Fahrenheit.")

      
      rightText.insert(INSERT,Temp_Type + "\n")
      Add_to_Log("Temp Converted " + Temp_Type + str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

   Temp_win = Toplevel(window)
   Temp_win.geometry("220x150+300+300")
   Temp_win.title("Temperature Convertion")
  
   Temp_Label = Label(Temp_win,text=" Select Convertion and enter value").grid(column=0, row=0)
   
   radio_btn1 = Radiobutton(Temp_win,text="Celsius to Fahrenheit",variable=Tvar,value="1",command=temp_converter).grid(column=0, row=1)
   
   radio_btn2 = Radiobutton(Temp_win,text="Fahrenheit to Celsius",variable=Tvar,value="2",command=temp_converter).grid(column=0, row=2)
   
   Tentry = Entry(Temp_win)
   Tentry.grid(column=0, row=3)
   Tentry.insert(INSERT,Temp)
   
   def Post_OK_Pressed():
      Temp_Type=str(Tvar.get())
      temp_converter()
   
   temp_button = Button(Temp_win,text="OK",command=Post_OK_Pressed)
   temp_button.grid(column=0,row=4 , pady=3,padx=3)

   Temp_win.protocol("WM_DELETE_WINDOW", Do_SetFocus)

   Temp_win.mainloop()

  
      

def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(rightText.get("1.0", "end-1c")) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.




def Save_Canvas():
   window.geometry("850x600+50+50")
   window.update()
   time.sleep(1)

   box = (60,270,560,690)
   
   grabcanvas = ImageGrab.grab(bbox=box)
   Calc_Area = "Calculator Plot"+time.strftime("_%d_%B_%Y_%H_%M_%S")+".jpg"
   grabcanvas.save(Calc_Area,quality=95)
   My_message = "Screen shot was saved as " + Calc_Area
   messagebox.showinfo("Plot Screen Shot", My_message)
   Add_to_Log("Plot area saved ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

def Screen_Save():
   window.geometry("850x600+50+50")
   window.update()
   time.sleep(2)

   box = (49,49,920,710)
   
   grabcanvas = ImageGrab.grab(bbox=box)
   Screen_Area = "Calculator"+time.strftime("_%d_%B_%Y_%H_%M_%S")+".jpg"
   grabcanvas.save(Screen_Area, optimize=True,quality=99)
   My_message = "Screen shot was saved as "+Screen_Area
   messagebox.showinfo("Screen Shot", My_message)
   Add_to_Log("Screen saved ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

   #print('Screenshoot of tkinter.Canvas saved in "out.jpg"')

def Get_Plot_Input():

   child_window_plot = Toplevel() # Child window 
   child_window_plot.geometry("480x200")  # Size of the window 
   child_window_plot.title("Plot Input Data")

   def btnPlot_Ok_pressed():
      
      btnTxtClear_pressed()
      if var3.get()==1:
         w.delete("all")

      txt.insert(0,PEntry.get())
      w.create_text(250,320,text=X_Entry.get())
      w.create_text(6,150,width=2,text=Y_Entry.get())
      if var2.get()==1 :
       w.create_text(40,320,text=str(Des_Entry.get()))

      
      window.update()
      Draw_Plot()
      
      

   Plot_Label = Label(child_window_plot, text="Plot example = { sin(radians(x)) }").grid(column=0, row=0)
   Plot_Label = Label(child_window_plot, text="Plot example = { cos(radians(x)) }").grid(column=0, row=1)
   Plot_Label = Label(child_window_plot, text="Plot example = { tan(radians(x)) }").grid(column=0, row=2)

   Plot_Label = Label(child_window_plot, text="Equation ").grid(column=0, row=3)
 
   PEntry = Entry(child_window_plot)
   PEntry.grid(column=1, row=3)
   PEntry.insert(INSERT," sin(radians(x))")
   
   
   
   #Plot_Entry.insert(END,"sin(radians(x))")

   X_Label = Label(child_window_plot, text="Enter Label -X  ").grid(column=0, row=4)
   X_Entry = Entry(child_window_plot)
   X_Entry.grid(column=1,row=4)
   X_Entry.insert(INSERT,"X-Label")

   Date_Checkbutton = Checkbutton(child_window_plot,text="Add Date",variable=var1)
   Date_Checkbutton.grid(column=2,row=4)
   

   Y_Label = Label(child_window_plot, text="Enter Label -Y  ").grid(column=0, row=5)
   Y_Entry = Entry(child_window_plot)
   Y_Entry.grid(column=1,row=5)
   Y_Entry.insert(INSERT,"Y-Label")

   E_Checkbutton = Checkbutton(child_window_plot,text="Erase Old Plot",variable=var3)
   E_Checkbutton.grid(column=2,row=5)
   
   Des_Label = Label(child_window_plot, text="Title ").grid(column=0, row=6)
   Des_Entry = Entry(child_window_plot)
   Des_Entry.grid(column=1,row=6)
   Des_Entry.insert(INSERT,"Title Here")

   Des_Checkbutton = Checkbutton(child_window_plot,text="Add Title",variable=var2)
   Des_Checkbutton.grid(column=2,row=6)
   
   window.Plot_Ok_Button = Button(child_window_plot,text = " OK ",width=10,padx=4,command=btnPlot_Ok_pressed).grid(column=3,row=7,columnspan=2)
   
   child_window_plot.mainloop()
   Add_to_Log("Get Plot ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

  
   



### Plot Canvas ###

def Draw_Plot():
   
   Px=14
   Py=12
   
   w.create_line(Px, Py, Px+470, Py, fill=Plot_Axis_Line_Colour)
   w.create_line(Px, Py+300, Px+470, Py+300, fill=Plot_Axis_Line_Colour)
   w.create_line(Px, Py, Px, Py+300, fill=Plot_Axis_Line_Colour)
   w.create_line(Px+470, Py+300, Px+470, Py, fill=Plot_Axis_Line_Colour)
   w.create_line(Px,150, Px+470, 150, fill=Plot_Axis_Line_Colour)
   w.create_text(50,150,text="0")
   w.create_text(Px+55,17,text="Calculator Plus Plot")
   if var1.get()==1 :
       w.create_text(400,320,text=str(date.strftime("%A %d %B %Y %H:%M")))

   

   w.create_text(420,150,text="360")
   stringa= txt.get()
   rightText.insert(INSERT,stringa +" (Plotted)\n")
   stringb=stringa.replace("x","angle")
   y1=0
   try:
      
      for angle in range(360):
         y=eval(stringb)
     
         w.create_line((angle)+50,150+(y1*100),(angle)+51,151+(y*100), fill="blue")
         y1=y
   except:
      return
   
      
def mandel_pixel(c):
  """ calculates the color index of the mandelbrot plane point passed in the arguments """
  maxIt = 256
  z =  c   
  for i in range(maxIt):
      a = z * z
      z=a + c
      if a.real  >= 4.:
         return i
  return 256

def mandelbrot(xa,xb,ya,yb,x,y):
    """ returns a mandelbrot in a string for Tk PhotoImage"""
    #color string table in Photoimage format #RRGGBB 
    clr=[ ' #%02x%02x%02x' % (int(255*((i/255)**.25)),0,0) for i in range(256)]
    clr.append(' #000000')  #append the color of the centre as index 256
    #calculate mandelbrot x,y coordinates for each screen pixel
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
    #build the Photoimage string by calling mandel_pixel to index in the color table
    return" ".join((("{"+" ".join(clr[mandel_pixel(complex(i,j))] for i in xm))+"}" for j in ym))


### Mandelbrot ###


   
   
def Plot_Mandelbrot():

   def Save_Mandelbrot():
      child_window.geometry("850x600+50+50")
      child_window.update()
      Screen_Save()

   child_window = Toplevel() # Child window 
   child_window.geometry("850x600+50+50")  # Size of the window 
   child_window.title("Mandelbrot")

   menubar = Menu(child_window)
   filemenu = Menu(menubar, tearoff=0)
   filemenu.add_command(label="New", command=donothing)
   filemenu.add_command(label="Open Log File", command=Open_Log_File)
   filemenu.add_command(label="Save Screen", command=Save_Mandelbrot)
   filemenu.add_command(label="Save Plot Area", command=Save_Canvas)
   filemenu.add_command(label="Save Equation Results", command=file_save)
   filemenu.add_command(label="Close", command=donothing)

   filemenu.add_separator()
   
   filemenu.add_command(label="Exit", command=Do_End)
   menubar.add_cascade(label="File", menu=filemenu)
   editmenu = Menu(menubar, tearoff=0)
   editmenu.add_command(label="Undo", command=donothing)

   editmenu.add_separator()

   editmenu.add_command(label="Delete Results", command=btnRt_TxtClear_pressed)
   editmenu.add_command(label="Copy", command=donothing)
   editmenu.add_command(label="Paste", command=donothing)
   editmenu.add_command(label="Delete Plot", command=btnClearPlot)
   editmenu.add_command(label="Select All", command=donothing)

   menubar.add_cascade(label="Edit", menu=editmenu)
   helpmenu = Menu(menubar, tearoff=0)
   helpmenu.add_command(label="Help Index", command=Help_WINDOW)
   helpmenu.add_command(label="About...", command=Display_About)
   menubar.add_cascade(label="Help", menu=helpmenu)
   editmenu = Menu(menubar, tearoff=0)
   
   child_window.config(menu=menubar)

   Log_String = "          "
   

   WIDTH = 800; HEIGHT = 600
  
   xa = -2.0; xb = 1.0
   ya = -1.27; yb = 1.27
   #maxIt = 256
   
   
   child_window.canvas = Canvas(child_window, width = WIDTH, height = HEIGHT, bg = "white")
   child_window.canvas.pack(padx=10,pady=10)

   Canvas_text = child_window.canvas.create_text(150,100, text="Please wait while Mandelbrot is being prepared")
   
   child_window.update()
   
   
   Img = PhotoImage(width = WIDTH, height = HEIGHT)
   child_window.canvas.create_image((0, 0), image = Img, state = "normal" ,anchor = NW)
   Img.put(mandelbrot(xa,xb,ya,yb,WIDTH,HEIGHT))
   child_window.update()
   Add_to_Log("Mandlebrot Opened ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")
   child_window.mainloop ()
  
def Add_to_Log(Log_String) :  
   # Open a file with access mode 'a'
   file_object = open('Calculator.log', 'a')
   # Append 'hello' at the end of file
   file_object.write(Log_String)
   # Close the file
   file_object.close()  


def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

def btnCopy_pressed():
   Equation_Copy = txt.get()
   rightText.insert(INSERT,Equation_Copy +" (Copied)")
   
   Add_to_Log(Equation_Copy +" (Copied); "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")

def View_Plot():

   f = filedialog.askopenfilename( defaultextension=".jpg")

   if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return

   Viewimage = Image.open(f)
   Viewimage.show()
   


   
### Buttons Pressed ###


def btnA_pressed():
    txt.insert(INSERT, "A")

def btnB_pressed():
    txt.insert(INSERT, "B")

def btnC_pressed():
    txt.insert(INSERT, "C")

def btnD_pressed():
    txt.insert(INSERT, "D")

def btnE_pressed():
    txt.insert(INSERT, "E")

def btnF_pressed():
    txt.insert(INSERT, "F")

def btn1_pressed():
    txt.insert(INSERT, "1")

def btn2_pressed():
    txt.insert(INSERT, "2")

def btn3_pressed():
    txt.insert(INSERT, "3")

def btn4_pressed():
    txt.insert(INSERT, "4")

def btn5_pressed():
    txt.insert(INSERT, "5")

def btn6_pressed():
    txt.insert(INSERT, "6")

def btn7_pressed():
    txt.insert(INSERT, "7")

def btn8_pressed():
    txt.insert(INSERT, "8")

def btn9_pressed():
    txt.insert(INSERT, "9")

def btn0_pressed():
    txt.insert(INSERT, "0")

def btnMinus_pressed():
    txt.insert(INSERT, "-")

def btnPlus_pressed():
    txt.insert(INSERT, "+")

def btnMulti_pressed():
    txt.insert(INSERT, "*")

def btnDiv_pressed():
    txt.insert(INSERT, "/")

def btnPerCent_pressed():
    txt.insert(INSERT, "%")

def btnOpenBracket_pressed():
    txt.insert(INSERT, "(")

def btnCloseBracket_pressed():
    txt.insert(INSERT, ")")


def btnSquRoute_pressed():
    txt.insert(INSERT, "sqrt()")

def btnCos_pressed():
    txt.insert(INSERT, "cos()")


def btnAcos_pressed():
    txt.insert(INSERT, "acos()")


def btnAtan_pressed():
    txt.insert(INSERT, "atan()")

def btnTan_pressed():
    txt.insert(INSERT, "tan()")

def btnSin_pressed():
    txt.insert(INSERT, "sin()")

def btnAsin_pressed():
    txt.insert(INSERT, "asin()")

def btnLog_pressed():
    txt.insert(INSERT, "log(x, base)")
    
def btnMod_pressed():
    txt.insert(INSERT, "modf()")
    
def btnExp_pressed():
    txt.insert(INSERT, "exp()")

def btnPower_pressed():
    txt.insert(INSERT, "pow(x,^)")
   


def btnTxtClear_pressed():
    txt.delete(0,"end")
    Add_to_Log("Entry Cleared ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")


def btnPrint_pressed():
    PrintOut = rightText.get("10.", "end-1c")
    #print (PrintOut)
    #return
    filename = tempfile.mktemp(".txt")
    open (filename , "w").write ("Calculator Output\n" + PrintOut)
    os.startfile(filename, "print")
    Add_to_Log("Results Printed ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")
    

def btnPoint_pressed():
    txt.insert(INSERT, ".")


   
def HexToBin_pressed():

   HexIn = txt.get()

   try:
      
       BinOut = bin(int(HexIn, 16))[2:]
   except:
      BinOut = format(error)

   rightText.insert(INSERT,HexIn + " Hex = " + BinOut + " Bin.\n")
    
  
  
def bin_to_dec():
    """ Convert from binary to decimal. """
    # get input string
    bits = txt.get()

    for i in bits:
        if i > "1":
                tm.showerror("Error Bin to Dec", "Illegal Char")
                return
                
    

    # set exponent
    exp = len(txt.get()) - 1

    tot = 0

    # do conversion
    while exp >= 1:
        for i in bits[:-1]:  

            if i == '1':
                tot += 2**exp
            elif i == '0':
                tot = tot

            

            exp -= 1
            
        if bits[-1] == '1':
            tot += 1

    total = tot
    # print output
    rightText.insert(INSERT,bits + " Bin = " + str(total) + " Dec.\n")




def BinToHex_pressed():
   try:
      binary_string = txt.get()
      decimal_representation = int(binary_string, 2)
      hexadecimal_string = hex(decimal_representation)
      rightText.insert(INSERT,binary_string +" Bin = " + hexadecimal_string+"\n")
      
   except Exception as error:
       
         message = "An error has occurred: '{}'.".format(error)
         detail = format(error)
         tm.showerror(message, detail)
         Add_to_Log("Error ; "+str(detail)+" ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")


def btnEquals_pressed():
    MyValue = txt.get()
    
    try:
        
        rightText.insert(INSERT,MyValue + " = " + str((eval(MyValue))) + "\n")
        Add_to_Log(MyValue + " = " + str((eval(MyValue))) + "\n")
    
    except Exception as error:
            
            message = "An error has occurred: '{}'.".format(error)
            detail = format(error)
            tm.showerror(message, detail)
            Add_to_Log("Error ; "+str(detail)+" ; "+ str(date.strftime("%A %d %B %Y %H:%M"))+"\n")


def MySystem():
   rightText.insert(INSERT,"Please Wait!\nwhile I collect your System Information\n")
   window.update()
   child_window_sys = Toplevel(window) # Child window 
   child_window_sys.geometry("800x400")  # Size of the window 
   child_window_sys.title("System Data")

   si = subprocess.STARTUPINFO()
   si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
   
   Sys_text = subprocess.check_output(['systeminfo'], startupinfo=si).decode('utf-8')

   sys_scrollbar = Scrollbar(child_window_sys)
   sys_scrollbar.pack( side = RIGHT, fill = Y )

   Sys_txt = Text(child_window_sys,height=60, width=100,padx=4,pady=4, background ="white")
   Sys_txt.pack()
   
   
   sys_scrollbar.config( command = Sys_txt.yview )
   
   Sys_txt.insert(INSERT,Sys_text)
   

   child_window_sys.update()

   child_window_sys.mainloop()

   
def Random_Line_Art():

   NW = Toplevel(window)
   NW.title("Welcome to My Random Line Art Program")
   NW.geometry('{}x{}'.format(600,600))

   btntext = StringVar()
   delflag = IntVar()
   delflag.set(1)
   Btn_run_flag = BooleanVar()
   Btn_run_flag.set(True)
   
   Canvas_Width =580
   Canvas_Height =500



   def paint(event):
       python_green = "green"
       x1, y1 = (event.x - 1), (event.y - 1)
       x2, y2 = (event.x + 1), (event.y + 1)
       w.create_line(x1, y1, x2, y2, fill=python_green)

   def rotate( point, angle,length):
       x,y =point
       endy = y+(length * sin(radians(angle)))
       endx = x+(length * cos(radians(angle)))
       
       return endx,endy


   COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
       'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
       'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
       'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
       'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
       'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
       'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
       'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
       'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
       'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
       'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
       'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
       'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
       'indian red', 'saddle brown', 'sandy brown',
       'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
       'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
       'pale violet red', 'maroon', 'medium violet red', 'violet red',
       'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
       'thistle', 'snow2', 'snow3',
       'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
       'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
       'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
       'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
       'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
       'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
       'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
       'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
       'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
       'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
       'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
       'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
       'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
       'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
       'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
       'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
       'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
       'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
       'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
       'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
       'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
       'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
       'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
       'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
       'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
       'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
       'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
       'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
       'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
       'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
       'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
       'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
       'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
       'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
       'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
       'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
       'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
       'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
       'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
       'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
       'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
       'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
       'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
       'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
       'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
       'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
       'gray1']

   DrawFrame=Frame(NW)
   DrawFrame.grid(row=0,columnspan=3)    

   w = Canvas(DrawFrame,
              width=Canvas_Width,
              height=Canvas_Height,
              bg="white", relief=GROOVE)

   w.grid()
   
   w.bind("<B1-Motion>", paint)


   

   def btn_run_pressed():
       
       if Btn_run_flag.get() == True:
           Btn_run_flag.set(False)
           
           btntext.set('STOP')
           Draw_Art()
           
       else :
           Btn_run_flag.set(True)
           
           btntext.set('RUN')
           
           
   btntext.set("RUN")

   def Clear_Canvas(event):
       delflag.set(1)
       w.delete("all")
       
       
   ControlsFrame = Frame(NW)
   ControlsFrame.grid(column=0,row=1)   


   Btnrunstop = Button(ControlsFrame,textvariable=btntext,command=btn_run_pressed)
   Btnrunstop.grid(column=0,row=1)

   BtnDelete = Button(ControlsFrame,text='Delete')
   BtnDelete.grid(column=1,row=1)
   BtnDelete.bind('<Button-1>',Clear_Canvas)

   Vscale = Scale(ControlsFrame, from_=1, to=60,label="Max Random Angle +/-",width=20,length=150,orient=HORIZONTAL)
   Vscale.set(10)
   Vscale.grid(column=0,row=2)

   Hscale = Scale(ControlsFrame, from_=1, to=15,label="Line Length", width=20,length=150,orient=HORIZONTAL)
   Hscale.set(5)
   Hscale.grid(column=1,row=2)

   LineWidth = Scale(ControlsFrame, from_=1, to=5,label="Line Width", width=20,length=150,orient=HORIZONTAL)
   LineWidth.set(2)
   LineWidth.grid(column=2,row=2)


   def Draw_Art():
       
       delflag.set(0)
       rect = w.create_rectangle(Canvas_Width,Canvas_Height, 2, 2, fill="")
       rect = w.create_rectangle(Canvas_Width+1,Canvas_Height+1, 1, 1, fill="")

       px=200
       py=200
       
       w.create_line(px,py,px+5,py+5,fill="RED")

       Ipoint=(px,py)

       Ilength=int(random.randint(1,10))

       Iangle =20
       IsDelete_pressed=0


       output = rotate(Ipoint,Iangle,Ilength)

       w.create_line(px,py,output,fill="black")
       NW.update

       for i in range(10000):
           IsDelete_pressed = delflag.get()
           if IsDelete_pressed == 1:
               
               return
               
           while (Btn_run_flag.get() == False) :

               [px,py] = output

               if px >=Canvas_Width or px<=1:
                   px=Canvas_Width/2
                   py=Canvas_Height/2
                   output=(Canvas_Width/2,Canvas_Height/2)
                   break
               if py >=Canvas_Height or py <=1:
                   px=Canvas_Width/2
                   py=Canvas_Height/2
                   output=(Canvas_Width/2,Canvas_Height/2)
                   break
                   
               Ilength=int(random.randint(5,Hscale.get()))   
               r = int(random.randint(1,100))
               Crgb = COLORS[r]
               
               
               
                   
               Ipoint=output
               Iangle += random.randint(-(Vscale.get()),(Vscale.get()))
               output = rotate(Ipoint,Iangle,Ilength)
               w.create_line(px,py,output,width=LineWidth.get(),fill=str(Crgb))

               DrawFrame.update()

               time.sleep(.001)

       btn_run_pressed
       
       
   NW.update()
   NW.mainloop()

### End Random Line Art ###   


### Main Menu Bar ###   

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="View Plot", command=View_Plot)
filemenu.add_command(label="Open Log File", command=Open_Log_File)
filemenu.add_command(label="Save Screen", command=Screen_Save)
filemenu.add_command(label="Save Plot Area", command=Save_Canvas)
filemenu.add_command(label="Save Equation Results", command=file_save)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=Do_End)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Delete Results", command=btnRt_TxtClear_pressed)
editmenu.add_command(label="Safe Plot as pdf", command=generate_pdf)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete Plot", command=btnClearPlot)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=Help_WINDOW)
helpmenu.add_command(label="About...", command=Display_About)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)



### ROW 1 ###

btnA = Button(frame, padx=2, text="A",width=8, command=btnA_pressed)

btnA.grid(column=1, row=1)

btnB = Button(frame, padx=2, text="B",width=6, command=btnB_pressed)

btnB.grid(column=2, row=1)


btn7 = Button(frame, padx=2, text="7",width=6, command=btn7_pressed)

btn7.grid(column=3, row=1)

btn8 = Button(frame, padx=2, text="8",width=6, command=btn8_pressed)

btn8.grid(column=4, row=1)

btn9 = Button(frame, padx=2, text="9",width=6, command=btn9_pressed)

btn9.grid(column=5, row=1)

btnPlus = Button(frame, padx=2, text="+",width=6, command=btnPlus_pressed)

btnPlus.grid(column=6 , row=1)

btnSquRoute = Button(frame, padx=2, text="SQRT()",width=6, command=btnSquRoute_pressed)

btnSquRoute.grid(column=7 , row=1)

btnCos = Button(frame, padx=2, text="COS()",width=6, command=btnCos_pressed)

btnCos.grid(column=8, row=1)

btnAcos = Button(frame, padx=2, text="ACOS()",width=6, command=btnAcos_pressed)

btnAcos.grid(column=9, row=1)

btnSpare = Button(frame, padx=2, text="Temp",width=6, command=Temp_converter_window)

btnSpare.grid(column=10, row=1)




#ROW 2
btnC= Button(frame, padx=2, text="C",width=8, command=btnC_pressed)

btnC.grid(column=1, row=2)

btnD= Button(frame, padx=2, text="D",width=6, command=btnD_pressed)

btnD.grid(column=2, row=2)

btn4 = Button(frame, padx=2, text="4",width=6, command=btn4_pressed)

btn4.grid(column=3, row=2)

btn5 = Button(frame, padx=2, text="5",width=6, command=btn5_pressed)

btn5.grid(column=4, row=2)

btn6 = Button(frame, padx=2, text="6",width=6, command=btn6_pressed)

btn6.grid(column=5, row=2)

btnMinus = Button(frame, padx=2, text=" - ",width=6, command=btnMinus_pressed)

btnMinus.grid(column=6, row=2)

btnOpenBracket = Button(frame, padx=2, text= "(",width=6, command=btnOpenBracket_pressed)

btnOpenBracket.grid(column=7, row=2)

btnTan = Button(frame, padx=2, text="TAN()",width=6, command=btnTan_pressed)

btnTan.grid(column=8, row=2)


btnAtan = Button(frame, padx=2, text="ATAN()",width=6, command=btnAtan_pressed)

btnAtan.grid(column=9, row=2)

btnSpare = Button(frame, padx=2, text="System",width=6, command=MySystem)

btnSpare.grid(column=10, row=2)

#ROW 3

btnE= Button(frame, padx=2, text="E",width=8, command=btnE_pressed)

btnE.grid(column=1, row=3)

btnF= Button(frame, padx=2, text="F",width=6, command=btnF_pressed)

btnF.grid(column=2, row=3)

btn1 = Button(frame, padx=2, text="1",width=6, command=btn1_pressed)

btn1.grid(column=3, row=3)

btn2 = Button(frame, padx=2, text="2",width=6, command=btn2_pressed)

btn2.grid(column=4, row=3)

btn3 = Button(frame, padx=2, text="3",width=6,command=btn3_pressed)

btn3.grid(column=5, row=3)

btnMult = Button(frame, padx=2, text=" x ",width=6, command=btnMulti_pressed)

btnMult.grid(column=6, row=3)

btnCloseBracket = Button(frame, padx=2, text=")",width=6, command=btnCloseBracket_pressed)

btnCloseBracket.grid(column=7, row=3)

btnAsin = Button(frame, padx=2, text="ASIN()",width=6, command=btnAsin_pressed)

btnAsin.grid(column=8, row=3)

btnSin = Button(frame, padx=2, text="SIN()",width=6, command=btnSin_pressed)

btnSin.grid(column=9, row=3)

btnSpare = Button(frame, padx=2, text="RLA",width=6, command=Random_Line_Art)

btnSpare.grid(column=10, row=3)


#ROW 4
btnHex= Button(frame, padx=2, text="Hex-Bin",width=8, command=HexToBin_pressed)

btnHex.grid(column=1, row=4)

btnBin= Button(frame, padx=2, text="Bin-Hex",width=6, command=BinToHex_pressed)

btnBin.grid(column=2, row=4)

btnClear = Button(frame, padx=2, text="CLR",width=6, command=btnTxtClear_pressed)

btnClear.grid(column=3, row=4)

btn0 = Button(frame, padx=2, text="0",width=6, command=btn0_pressed)

btn0.grid(column=4, row=4)

btnPoint = Button(frame,padx=2, text=".",width=6, command=btnPoint_pressed)

btnPoint.grid(column=5, row=4)

btnDiv = Button(frame,padx=2, text=" / ",width=6, command=btnDiv_pressed)

btnDiv.grid(column=6, row =4)

btnLog = Button(frame,padx=2, text="Log",width=6, command=btnLog_pressed)

btnLog.grid(column=7, row =4)

btnMod = Button(frame,padx=2, text="Mod",width=6, command=btnMod_pressed)

btnMod.grid(column=8, row =4)

btnExp = Button(frame,padx=2, text="Exp",width=6, command=btnExp_pressed)

btnExp.grid(column=9, row =4)
btnSpare = Button(frame, padx=2, text="Spare",width=6, command=donothing)

btnSpare.grid(column=10, row=4)

# Rightframe Buttons

btnTxtClear= Button(rightframe, text="Clear Results",width=10, command=btnRt_TxtClear_pressed).grid(column=0,row=2)
btnPrint= Button(rightframe, text="Print Results",width=10, command=btnPrint_pressed).grid(column=1,row=2)



#ROW 5

btnMandelbrot = Button(frame,padx=2, text="Mandelbrot",width=8, command=Plot_Mandelbrot)

btnMandelbrot.grid(column=1, row=5)

btnPlot = Button(frame,padx=2, text="PLOT",width=6, command=Get_Plot_Input)

btnPlot.grid(column=2, row=5)

btnEquals = Button(frame,padx=2, text=" = ",width=14, command=btnEquals_pressed)

btnEquals.grid(column=3, row=5, columnspan=2)


btnEquals1 = Button(frame,padx=2, text=" = ",width=14, command=btnEquals_pressed)

btnEquals1.grid(column=5, row=5, columnspan=2)

btnStarDate = Button(frame,padx=2, text="Copy",width=6, command=btnCopy_pressed)

btnStarDate.grid(column=7, row=5)


btnbin_to_dec = Button(frame,padx=2, text="Bin-Dec",width=6, command=bin_to_dec)

btnbin_to_dec.grid(column=8, row=5)

btnPower = Button(frame,padx=2, text="Pow",width=6)

btnPower.grid(column=9, row=5)

btnSpare = Button(frame, padx=2, text="Spare",width=6, command=donothing)

btnSpare.grid(column=10, row=5)

#End Rows
### CLOCK   ###

label = Label(rightframe, font=("Courier",8, 'bold'), bd =10)
label.config(height=1,relief= RAISED,width=44)
label.grid(row =0, column=0,columnspan=2)

def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(200, digitalclock)


### Pack Frames ###

frame.pack(side ="top")
leftFrame.pack(side="left", padx=2,pady=2)
leftFrame.config(height=24)
rightframe.pack(side = "right")
bottomframe.pack( side = 'bottom')

rightText.insert(INSERT,str(date.strftime("%A %d %B %Y %H:%M"))+"\n")


digitalclock()
Add_to_Log("Calculator Started "+ str(date)+"\n")

window.protocol("WM_DELETE_WINDOW", Do_End)

window.mainloop()

