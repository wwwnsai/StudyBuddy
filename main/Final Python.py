from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import time
from time import strftime

class StudyBud:
    def __init__(self):

        self.w = Tk()
        self.w.title("Study Bud")
        self.w.geometry("1280x720")
        self.w.resizable(0,0)

        self.bg = ImageTk.PhotoImage(file = "D:\Year1\Python\Final Proposal\photos\IMG_0508.JPG")


        self.canvas = Canvas(self.w , width = 1280, height = 720)
        self.canvas.pack(fill = "both", expand = True)
        self.canvas.create_image(0, 0, image = self.bg, anchor = "nw")     


        self.th = StringVar()
        self.tm = StringVar()

        self.timeh = Entry(self.w, width = 2, textvariable = self.th, justify = RIGHT, font = ("Times New Roman", 12))
        self.timem = Entry(self.w, width = 2, textvariable = self.tm, justify = RIGHT, font = ("Times New Roman", 12))
        self.start = Button(self.w, width = 10, text = 'Start', background = '#203939', fg = "white", font = ("Times New Roman", 12), command = lambda:[self.get_bt(),self.get_time()])
        # self.start = Button(self.w, width = 10, text = 'Start', background = '#203939', fg = "white", font = ("Times New Roman", 12), command = self.get_time)

        
        # self.options_list = [ 5, 10, 15, 20]
        self.b = StringVar(self.w)
        self.question_menu = OptionMenu(self.w, self.b, '05', '10', '15', '20')

        # self.breakt = Entry(self.w, width = 2, textvariable = self.b, justify = RIGHT, font = ("Times New Roman", 12))
        self.m = Checkbutton(self.w,justify = RIGHT, background = '#4B7674' ,font = ("Times New Roman", 12))

        self.p = Checkbutton(self.w,justify = RIGHT, background = '#4B7674' ,font = ("Times New Roman", 12))

 
        # Display Buttons
        self.title_canvas = self.canvas.create_text( 225, 100, anchor = "nw", text = 'Menu', fill = 'white', font = ("Times New Roman", 16))

        self.Lt_canvas = self.canvas.create_text( 130, 200, anchor = "nw", text = 'Enter your study time  :', fill = 'white', font = ("Times New Roman", 12))
        self.timeh_canvas = self.canvas.create_window( 300, 200, anchor = "nw", window = self.timeh)
        self.Ltdot_canvas = self.canvas.create_text( 330, 200, anchor = "nw", text = ' : ', fill = 'white', font = ("Times New Roman", 12))
        self.timem_canvas = self.canvas.create_window( 350, 200, anchor = "nw", window = self.timem)
        
        self.Lb_canvas = self.canvas.create_text( 150, 300, anchor = "nw", text = 'Enter your break time  :', fill = 'white', font = ("Times New Roman", 12))
        self.breakt_canvas = self.canvas.create_window( 325, 300, anchor = "nw", window =  self.question_menu)

        self.mchk_canvas = self.canvas.create_window (220, 400, anchor = "nw", window = self.m)
        self.mtext_canvas = self.canvas.create_text( 250, 405, anchor = "nw", text = "music", fill = 'white', font = ("Times New Roman", 12))

        self.pchk_canvas = self.canvas.create_window (190, 475, anchor = "nw", window = self.p)
        self.ptext_canvas = self.canvas.create_text( 220, 480, anchor = "nw", text = "posture reminder", fill = 'white', font = ("Times New Roman", 12))

        self.start_canvas = self.canvas.create_window( 210, 570, anchor = "nw", window = self.start)



        self.w.mainloop()
    
    def get_bt(self):
        s = format(self.b.get())
        ss = int(s)
        self.gbtt_canvas = self.canvas.create_text( 850, 400, anchor = "nw", text = f"Break time: {ss:0>2}", fill = '#203939', font = ("Times New Roman", 24))
        for i in range(-1,ss):
            
            time.sleep(1)
            self.canvas.itemconfig(self.gbtt_canvas, text = f"Break time: {ss:0>2}")
            ss -= 1
            
            
            
                # self.gbtt_canvas2 = self.canvas.create_text( 850, 400, anchor = "nw", text = f"Break time: {ss}", fill = '#203939', font = ("Times New Roman", 24))
                
                
                
            # s2 = format(self.b.get())
            # self.gbtt_canvas.replace(s,s2)

           
        return None

    def get_time(self):
        # self.gt = Label(self.w, font = ("Times New Roman", 24), text = f"00 h : 00 m : 00 s")
        # self.gt_canvas = self.canvas.create_window( 825, 150, anchor = "nw", window = self.gt)

        self.gtt_canvas = self.canvas.create_text( 750, 200, anchor = "nw", text = '00 h : 00 m : 00 s', fill = '#203939', font = ("Times New Roman", 38))

        return None

    
StudyBud()