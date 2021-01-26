from tkinter import *
from tkinter import messagebox
import random
import math
import time




NW = Tk()
NW.title("Welcome to My Random Line Art Program")

NW.geometry("600x600")

btntext = StringVar()
delflag = IntVar()
delflag.set(1)

Canvas_Width =580
Canvas_Height =500



def paint(event):
    python_green = "green"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_line(x1, y1, x2, y2, fill=python_green)

def rotate( point, angle,length):
    x,y =point
    endy = y+(length * math.sin(math.radians(angle)))
    endx = x+(length * math.cos(math.radians(angle)))
    
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

w = Canvas(DrawFrame,
           width=Canvas_Width,
           height=Canvas_Height,
           bg="white", relief=GROOVE)
w.pack(expand=YES, fill=BOTH,side="top", padx=4,pady=4)

w.bind("<B1-Motion>", paint)


Btn_run_flag = True

def btn_run_pressed():
    global Btn_run_flag
    if Btn_run_flag == True:
        Btn_run_flag=False
        
        btntext.set('STOP')
        Draw_Art()
        
    else :
        Btn_run_flag=True
        
        btntext.set('RUN')
        
        
btntext.set("RUN")

def Clear_Canvas(event):
    delflag.set(1)
    w.delete("all")
    
    
    


Btnrunstop = Button(DrawFrame,textvariable=btntext,command=btn_run_pressed).pack()

BtnDelete = Button(DrawFrame,text='Delete')
BtnDelete.pack()
BtnDelete.bind('<Button-1>',Clear_Canvas)



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
            
        while (Btn_run_flag == False) :

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
    
    
        


Vscale = Scale(DrawFrame, from_=1, to=60,label="Max Random Angle +/-",width=20,length=150,orient=HORIZONTAL)
Vscale.set(10)
Vscale.pack(side="left")
Hscale = Scale(DrawFrame, from_=1, to=15,label="Line Length", width=20,length=150,orient=HORIZONTAL)
Hscale.set(5)
Hscale.pack(side="left")
LineWidth = Scale(DrawFrame, from_=1, to=5,label="Line Width", width=20,length=150,orient=HORIZONTAL)
LineWidth.set(2)
LineWidth.pack(side="left")


DrawFrame.pack(side ="top")        


NW.update()



NW.mainloop()





