from abc import ABC, abstractmethod
from tkinter.font import Font
import tkinter as tk
import pygame 
from pygame import mixer
import random
from PIL import ImageTk, Image  
import os
import shutil
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
from mutagen.mp3 import MP3

class MenuWindow(ABC):
    def __init__(self, win = None):
        self.w = win
        self.w = tk.Tk()
        self.w.title("Study Buddy")
        self.w.geometry("500x600")
        self.w.configure(background = '#F4E4C6')
        self.w.resizable(False,False)

        # fonts
        self.futura30 = Font(family = "Futura", size = 30, weight = "bold")
        self.futura16 = Font(family = "Futura", size = 16, weight = "normal")
        self.futura16bold = Font(family = "Futura", size = 16, weight = "bold")
        self.futura14 = Font(family = "Futura", size = 14, weight = "normal")
        self.futura14bold = Font(family = "Futura", size = 14, weight = "bold")
        self.futura20 = Font(family = "Futura", size = 20, weight = "bold")
        self.san18 = Font(family = "Sans Serif", size = 20, weight = "normal")
        self.san16 = Font(family = "Sans Serif", size = 16, weight = "normal")
        self.timesnewR16 = Font(family = "Times New Roman", size =  16, weight = "normal")
        self.timesnewR18 = Font(family = "Times New Roman", size =  18, weight = "normal")
        self.timesnewR20 = Font(family = "Times New Roman", size =  20, weight = "bold")

        # LabelMenu
        self.L_menuText = tk.Label(self.w, text = "Time to Study!", background = '#F4E4C6', foreground = "#425462", font = self.futura30)
        self.L_studyTime = tk.Label(self.w, text = "Select your study time : ", background = '#F4E4C6', foreground = "#425462", font = self.futura16bold)
        self.L_ = tk.Label(self.w, text = " : ", background = '#F4E4C6', foreground = "#425462", font = self.futura16)
        self.L_breakTime = tk.Label(self.w, text = "Select your break time : ", background = '#F4E4C6', foreground = "#425462", font = self.futura16bold)
        self.L_menuText.place(relx = 0.5, rely = 0.07, anchor = 'n')
        self.L_studyTime.place(relx = 0.34, rely = 0.25, anchor = 'n')
        self.L_.place(relx = 0.75, rely = 0.25, anchor = 'n')
        self.L_breakTime.place(relx = 0.44, rely = 0.38, anchor = 'n')

        # CheckButtons
        self.varMusic = tk.IntVar()
        self.varPost = tk.IntVar()
        self.Check_randmusic = tk.Radiobutton(win, text = "Random Music", variable = self.varMusic, value = 1, font = self.futura14bold, background = '#F4E4C6'
        , fg = '#425462', selectcolor = '#F4690C')
        self.Check_music = tk.Radiobutton(win, text = "Custom Music", variable = self.varMusic, value = 2, font = self.futura14bold, background = '#F4E4C6'
        , fg = '#425462', selectcolor = '#F4690C')
        self.Check_posture = tk.Checkbutton(win, text = "Posture Reminder", variable = self.varPost, onvalue = 1, offvalue = 0, background = '#F4E4C6', 
        font = self.futura14bold, fg = '#425462', selectcolor = '#F4690C')
        self.Check_randmusic.place(relx = 0.5, rely = 0.48, anchor = 'n')
        self.Check_music.place(relx = 0.494, rely = 0.53, anchor = 'n')
        self.Check_posture.place(relx = 0.5, rely = 0.705, anchor = 'n')

        # music button
        self.custom_playlist = "main\playlist"
        def addMusic():  
            Importmusic = fd.askopenfilename(title = "Select a mp3 file to add",  filetypes=[("mp3 Files","*.mp3")])  
            try:  
                shutil.copy(Importmusic, self.custom_playlist)  
                print("Saved file")              
            except:  
                print("The file wasn't added")
        self.addmusic_img = tk.PhotoImage(file = "main/add-music.png")
        self.addmusic = tk.Button(self.w,image = self.addmusic_img, background = "#F4E4C6", relief = "flat", activebackground = "#F4690C", 
        highlightbackground = "#203939",command = addMusic)
        self.addmusic.place(relx = 0.5, rely = 0.59 ,anchor = 'n')

        # MenuButtons
            # hour
        self.option_hour = [f"{x:0>2}" for x in range (0,10)]
        self.clicked_hour = tk.StringVar(self.w)
        self.clicked_hour.set(f"H")
        self.M_studyTime = tk.OptionMenu(self.w, self.clicked_hour, *self.option_hour)
        self.M_studyTime.config(background = "#97B7C4", foreground = "white", activebackground = "#F4690C", activeforeground = "#425462", font = self.futura14)
        self.M_studyTime.place(relx = 0.655, rely = 0.247, anchor = 'n')
            # minute
        self.option_minute = [f"{x:0>2}" for x in range (0,60)]
        self.clicked_minute = tk.StringVar(self.w)
        self.clicked_minute.set(f"M")
        self.M_breaktime = tk.OptionMenu(self.w, self.clicked_minute, *self.option_minute)
        self.M_breaktime.config(background = "#97B7C4", foreground = "white", activebackground = "#F4690C", activeforeground = "#425462", font = self.futura14)
        self.M_breaktime.place(relx = 0.85, rely = 0.247, anchor = 'n')
            # breaktime
        self.option_breakTime = [f"{1:0>2}", f"{5:0>2}", f"{10:0>2}", f"{15:0>2}", f"{20:0>2}"]
        self.clicked_breaktime = tk.StringVar(self.w)
        self.clicked_breaktime.set(f"M")
        self.M_breaktime = tk.OptionMenu(self.w, self.clicked_breaktime, *self.option_breakTime)
        self.M_breaktime.config(background = "#97B7C4", foreground = "white", activebackground = "#F4690C", activeforeground = "#425462", font = self.futura14)
        self.M_breaktime.place(relx = 0.76, rely = 0.377, anchor = 'n')

        # Start Button
        self.B_start = tk.Button(self.w, width = 10, text = "start", background = '#425462', foreground = "white", 
        font = self.futura16, activebackground = "#F4690C", activeforeground = "#425462",command = self.start).place(relx = 0.37, rely = 0.85, anchor = 'nw')

        self.w.mainloop()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def timer(self):
        pass

    @abstractmethod
    def breaktimer(self):
        pass

    @abstractmethod
    def PostureReminder(self):
        pass 

    @abstractmethod
    def PlayMusic(self):
        pass

    @abstractmethod
    def DisplayImages(self):
        pass

class Started(MenuWindow):
    def __init__(self, win = None):
        super().__init__(win)
        
    def start(self):
        # timer window
        self.w2 = tk.Toplevel(self.w)
        self.w2.title("Study Buddy")
        self.w2.geometry("1280x720")
        self.w2.config(background = "#425462")
        self.w2.resizable(False,False)
        self.w.withdraw()

        try:
            # get time
            self.h = tk.IntVar(self.w2)
            self.m = tk.IntVar(self.w2)
            self.s = tk.IntVar(self.w2)
            self.hour = int(format(self.clicked_hour.get()))
            self.minute = int(format(self.clicked_minute.get()))
            self.second = 0
            self.h.set("{0:2d}".format(self.hour))
            self.m.set("{0:2d}".format(self.minute))
            self.s.set("{0:2d}".format(self.second))
        except:
            pygame.mixer.init()
            mixer.music.pause()
            self.w.deiconify()
            self.w2.destroy()
            mb.showerror("Error", "Please select time properly")
        try:
            self.varB = tk.IntVar()
            self.getBT = int(format(self.clicked_breaktime.get()))
            self.varB.set(self.getBT)
        except:
            pygame.mixer.init()
            mixer.music.pause()
            self.w.deiconify()
            self.w2.destroy()
            mb.showerror("Error", "Please select break time")

        # config time
        self.w2.columnconfigure(0, weight = 8)
        self.w2.columnconfigure(1, weight = 1)
        self.w2.columnconfigure(2, weight = 1)
        self.w2.columnconfigure(3, weight = 2)
        self.w2.columnconfigure(4, weight = 1)
        self.w2.columnconfigure(5, weight = 1)
        self.w2.columnconfigure(6, weight = 1)
        self.w2.columnconfigure(7, weight = 1)
        self.w2.columnconfigure(8, weight = 5)
        self.w2.columnconfigure(9, weight = 3)
        self.w2.rowconfigure(0, weight = 2)
        self.w2.rowconfigure(1, weight = 1)
        self.w2.rowconfigure(2, weight = 2)
        self.w2.rowconfigure(3, weight = 3)
        self.w2.rowconfigure(4, weight = 1)
        self.w2.rowconfigure(5, weight = 1)
        self.w2.rowconfigure(6, weight = 1)
        self.w2.rowconfigure(7, weight = 1)
        self.w2.rowconfigure(8, weight = 1)
        self.w2.rowconfigure(9, weight = 2)

        # show time
        self.colon1 = tk.Label(self.w2, text = ':', background = '#425462', foreground = "#FBD2B2", 
        font = self.futura30)
        self.colon1.grid(column = 2, row = 3, padx = 20, sticky = tk.EW, rowspan = 2)
        self.colon2 = tk.Label(self.w2, text = ':', background = '#425462', foreground = "#FBD2B2", 
        font = self.futura30)
        self.colon2.grid(column = 4, row = 3, padx = 20, sticky = tk.EW, rowspan = 2)
        
        self.showTime_s = tk.Label(self.w2, text = f"{0:0>2}", background = '#425462', foreground = "White", font = self.futura30)
        self.showTime_s.grid(column = 5, row = 3, padx = 20, sticky = tk.EW, rowspan = 2)
        self.showTime_m = tk.Label(self.w2, text = f"{self.m.get():0>2}", background = '#425462', foreground = "White", font = self.futura30)
        self.showTime_m.grid(column = 3, row = 3, padx = 20, sticky = tk.EW, rowspan = 2)
        self.showTime_h = tk.Label(self.w2, text = f"{self.h.get():0>2}", background = '#425462', foreground = "White", font = self.futura30)
        self.showTime_h.grid(column = 1, row = 3, padx = 20, sticky = tk.EW, rowspan = 2)

        self.showTime_b = tk.Label(self.w2, text = f"Break Time\n{self.varB.get()} minutes",background = '#425462', foreground = "White", font = self.timesnewR16)
        self.showTime_b.grid(column = 2, row = 5, padx = 20, sticky = tk.EW, rowspan = 2, columnspan = 3)

        self.PlayMusic()
        self.DisplayImages()
        self.timer()
        

    def timer(self):
        self.time = int(self.h.get()*3600) + int(self.m.get()*60) + int(self.s.get())
        self.time_const = int(self.h.get()*3600) + int(self.m.get()*60) + int(self.s.get())
        self.play = True
        if self.time > -1:
            while self.play == True:
                mins, secs = divmod(self.time,60)
                hours = 0
                if mins < 0:
                    mins = 0
                if mins > 60:
                    hours, mins = divmod(mins,60)
                if mins == 60:
                    hours = 1
                    mins = 0
                self.s.set("{0:2d}".format(secs))
                self.m.set("{0:2d}".format(mins))
                self.h.set("{0:2d}".format(hours))
                
                # change label
                self.w2.update() 
                self.showTime_s.configure(text = f"{self.s.get() :0>2}")
                self.showTime_m.configure(text = f"{self.m.get() :0>2}")
                self.showTime_h.configure(text = f"{self.h.get() :0>2}")
                self.w2.after(1*(10**3))  
                self.time -= 1
        
                # time's up
                if self.time == 0:
                    self.w2.update() 
                    self.showTime_h.configure(text = f"{0:0>2}")
                    self.showTime_m.configure(text = f"{0:0>2}")
                    self.showTime_s.configure(text = f"{0:0>2}")
                    mixer.music.pause()
                    mb.showinfo("Time's up", "TIME'S UP!")
                    self.w.deiconify()
                    self.w2.destroy()
                    break
                    
                # call break timer
                if (self.time_const-self.time)%(60*60) == 0:
                    print("break time at: ", self.time_const-self.time," - ", self.time_const-self.time/(60*60))
                    self.breaktimer()
                # call posture timer   
                if (self.time_const-self.time)%(15*60) == 0:
                    print("posture time at: ", self.time_const-self. time, " - ", self.time_const-self.time/(15*60))
                    self.PostureReminder()

        if self.h.get() == 0 and self.m.get() == 0:
            mixer.music.pause()
            self.w.deiconify()
            self.w2.destroy()
            mb.showerror("Error", "Please select study time at least 1 minute")           
                    
    def breaktimer(self):
        try:
            # get break time
            self.b_min = tk.IntVar()
            self.b_sec = tk.IntVar()
            self.breakt_min = int(format(self.clicked_breaktime.get()))
            self.breakt_sec = 0
            self.b_min.set("{:0>2}".format(self.breakt_min))
            self.b_sec.set("{:0>2}".format(self.breakt_sec))
            if self.b_min.get() == 0:
                self.play = True
            elif self.b_min.get() > 0:
                self.play = False
        except:
            self.play = True

        # new window for break time
        try:
            if not self.play:
                self.w3_b = tk.Toplevel(self.w2)
                self.w3_b.title("Break Time!")
                self.w3_b.geometry("500x400")
                self.w3_b.configure(background = '#97B7C4')
                self.w3_b.resizable(False,False)

                # break time config
                self.w3_b.columnconfigure(0, weight = 8)
                self.w3_b.columnconfigure(2, weight = 1)
                self.w3_b.columnconfigure(3, weight = 1)
                self.w3_b.columnconfigure(4, weight = 1)
                self.w3_b.columnconfigure(5, weight = 1)
                self.w3_b.columnconfigure(6, weight = 8)
                # self.w3_b.columnconfigure(7, weight = 8)
                self.w3_b.rowconfigure(0, weight = 1)
                self.w3_b.rowconfigure(1, weight = 1)
                self.w3_b.rowconfigure(2, weight = 2)
                self.w3_b.rowconfigure(3, weight = 2)

                # break time label
                self.textBT = tk.Label(self.w3_b, text = 'Give yourself a break', background = '#97B7C4', foreground = "#425462", font = self.timesnewR20)
                self.colon2 = tk.Label(self.w3_b, text = ':', background = '#97B7C4', foreground = "white", font = self.futura30)  
                self.showBT_s = tk.Label(self.w3_b, text = f"{self.b_sec.get():0>2}", background = '#97B7C4', foreground = "white", font = self.futura30)
                self.showBT_m = tk.Label(self.w3_b, text = f"{self.b_min.get():0>2}", background = '#97B7C4', foreground = "white", font = self.futura30)
                self.textBT.grid(column = 3, row = 1, padx = 10, sticky = tk.EW, columnspan = 3)
                self.colon2.grid(column = 4, row = 2, padx = 10, sticky = tk.EW)
                self.showBT_s.grid(column = 5, row = 2, padx = 10, sticky = tk.EW)
                self.showBT_m.grid(column = 3, row = 2, padx = 10, sticky = tk.EW)

                # break timer
                self.bt = int(self.b_min.get()*60) + int(self.b_sec.get())
                if self.bt > 0:
                    while self.play == False:
                        mins, secs = ((self.bt-1)//60, (self.bt-1)%60)
                        if mins < 0:
                            mins = 0 
                        self.b_sec.set("{0:2d}".format(secs))
                        self.b_min.set("{0:2d}".format(mins))
                        
                        # change second
                        self.w3_b.update() 
                        self.showBT_s.configure(text = f"{self.b_sec.get() :0>2}")
                        self.showBT_m.configure(text = f"{self.b_min.get() :0>2}")
                        self.w2.after(1*(10**3))  
                        self.bt -= 1
                        # print(self.b_min.get()*60, "    ,   ", self.b_sec.get(), "    ,   ", self.breakt_min)
                        if self.bt == 0:
                            self.b_min.set("{0:2d}".format(self.breakt_min))
                            self.b_sec.set("{0:2d}".format(self.breakt_sec))
                            self.w3_b.destroy()
                            self.play = True     
                            break 
        except:
            self.play = True

    def PostureReminder(self):    
        # get var checkbox posture
        if self.varPost.get() == 0:
            pass
        if self.varPost.get() == 1:
            # new window4
            self.w4 = tk.Toplevel(self.w2)
            self.w4.title("Posture Reminder")
            self.w4.geometry("500x400")
            self.w4.configure(background = '#F4690C')
            self.w4.resizable(False,False)

            # list of words
            Posture_list = ["Don\'t forget to sit properly!", "Adjust your posture!", "You're sitting like a shrimp!", "Don't loose your good posture!"]
            random.shuffle(Posture_list)

            # row-column config
            self.w4.columnconfigure(0, weight = 8)
            self.w4.columnconfigure(1, weight = 1)
            self.w4.columnconfigure(2, weight = 8)
            self.w4.rowconfigure(0, weight = 1)
            self.w4.rowconfigure(1, weight = 5)
            self.w4.rowconfigure(2, weight = 2)
            self.w4.rowconfigure(3, weight = 1)

            # Text & Button
            def ok():
                if self.Ok_Button["text"] == "OK!":
                    self.w4.destroy() 
            self.Ok_Button = tk.Button(self.w4, text = "OK!", width = 3, height = 1, background = '#425462', foreground = "#97B7C4", font = self.futura16, command = ok)
            self.Ok_Button.grid(column = 1, row = 2, padx = 1, sticky = tk.EW)
            for x in Posture_list:
                self.Posture = tk.Label(self.w4, text = x , background = '#F4690C', foreground = "white", font = self.futura20)
                self.Posture.grid(column = 0, row = 1, padx = 5, sticky = tk.EW, columnspan = 3)

            # auto close window
            def autoclose():
                self.w4.destroy()
            self.w4.after(30000, autoclose)
    
    def PlayMusic(self):
        # input playlist
        self.playlist = "main\playlist"
        list1 = []
        rand_music_list = []
        list2 = []
        cus_music_list = []
    
        # randomplaylist
        a = os.listdir(self.playlist)
        for path in a:
            if os.path.isfile(os.path.join(self.playlist,path)):  
                list1.append(path)
                backlash = "\\"
                for i in list1:
                    p = "main\playlist" + backlash
                    i = p+i
                    rand_music_list.append(i)
        # print(rand_music_list)
        random.shuffle(rand_music_list)

        # customplaylist
        b = os.listdir(self.custom_playlist)
        for path in b:
            if os.path.isfile(os.path.join(self.custom_playlist,path)):  
                list2.append(path)
                for i in list2:
                    p = "main\playlist\\"
                    i = p+i
                    cus_music_list.append(i)
            print(cus_music_list)
        pygame.mixer.init()

        # button commands
        def pause_playMusic():
            if self.B_playM["text"] == "pause":
                self.B_playM["text"] = "play"
                self.B_playM.config(image = self.play_img)
                mixer.music.pause()         
            elif self.B_playM["text"] == "play":
                self.B_playM["text"] = "pause"
                self.B_playM.config(image = self.pause_img)
                mixer.music.unpause()
        def quitwin2():
            if self.quitw2["text"] == "Quit":
                mixer.music.pause()
                self.w.deiconify()
                self.w2.destroy()

        # pause button
        self.pause_img = tk.PhotoImage(file = "main\pause.png")
        self.B_playM = tk.Button(self.w2, text = "pause", image = self.pause_img, relief = 'flat', background = "#425462", command = pause_playMusic)
        self.B_playM.grid(column = 8, row = 7, sticky = tk.EW, columnspan = 2)
        self.play_img = tk.PhotoImage(file = "main\play.png")

        # show music
        self.quit_img = tk.PhotoImage(file = "main\quit_w2.png")
        self.NowP = tk.Label(self.w2, text = "==== Now Playing ====",background = '#425462', foreground = "#97B7C4", font = self.san16)
        self.NowP.grid(column = 8, row = 1, padx = 10, sticky = tk.EW, columnspan = 2)
        # quit w2
        self.quitw2 = tk.Button(self.w2, text = "Quit", image = self.quit_img,  background = '#97B7C4', activebackground = "#F4690C", 
        font = self.san16, command = quitwin2)
        self.quitw2.grid(column = 6, row = 8, sticky = tk.EW, columnspan = 2, rowspan = 1) 
        
        # get var checkbox music
        if self.varMusic.get() == 1:
            def play(x):
                if len(rand_music_list) > 0:
                    print("Now:  ", rand_music_list[0])
                    # get song length
                    song = MP3(rand_music_list[0])
                    self.songLength = song.info.length
               
                    # play
                    mixer.music.load(rand_music_list[0])
                    mixer.music.play()
                    mixer.music.set_volume(0.1)   

                    # show song name
                    self.nnn = rand_music_list[0].replace("main\playlist\\", "")
                    self.nameS = self.nnn.replace(".mp3", "")
                    self.strvar_music = tk.StringVar(self.w2)
                    self.mu = self.nameS
                    self.strvar_music.set(self.mu)
                    self.songN = tk.Label(self.w2, text = f"{self.strvar_music.get()}",background = '#425462', foreground = "#FBD2B2", font = self.timesnewR18)
                    self.songN.grid(column = 8, row = 6, padx = 20, sticky = tk.EW, columnspan = 2)
                    
                    # rand_music_list.pop(0)
                    rand_music_list.append(rand_music_list[0])
                    del rand_music_list[rand_music_list.index(rand_music_list[0])]
                    mixer.music.queue(rand_music_list[0])
                    def change():
                        self.nnn = rand_music_list[0].replace("main\playlist\\", "")
                        self.nameS = self.nnn.replace(".mp3", "")
                        self.mu = self.nameS
                        self.strvar_music.set(self.mu)
                        self.songN.configure(text = f"{self.strvar_music.get()}")
                    # self.w2.update()
                    self.w2.after(round(self.songLength)*1000, change)
                    # print("Next: ",rand_music_list[0],rand_music_list[1])
                
                def returnfunc():
                    return play(rand_music_list[0])
                self.w2.after(round(self.songLength)*1000, returnfunc)
            x = rand_music_list[0]
            play(x)

        if self.varMusic.get() == 2:
            try:
                def play(x):
                    if len(cus_music_list) > 0:
                        # get song length
                        song = MP3(cus_music_list[0])
                        self.songLength = song.info.length

                        # play
                        mixer.music.load(cus_music_list[0])
                        mixer.music.play()
                        mixer.music.set_volume(0.1)
                                    
                        # show song name
                        self.w2.update() 
                        self.nnn = cus_music_list[0].replace("main\playlist\\", "")
                        self.nameS = self.nnn.replace(".mp3", "")
                        self.strvar_music = tk.StringVar(self.w2)
                        self.mu = self.nameS
                        self.strvar_music.set(self.mu)
                        self.songN = tk.Label(self.w2, text = f"{self.strvar_music.get()}",background = '#425462', foreground = "#FBD2B2", font = self.timesnewR18)
                        self.songN.grid(column = 8, row = 6, padx = 20, sticky = tk.EW, columnspan = 2)
                            
                        self.songN.configure(text = f"{self.strvar_music.get()}")

                        # rand_music_list.pop(0)
                        cus_music_list.append(cus_music_list[0])
                        del cus_music_list[cus_music_list.index(cus_music_list[0])]
                        mixer.music.queue(cus_music_list[0])

                        def change():
                            self.nnn = cus_music_list[0].replace("main\playlist\\", "")
                            self.nameS = self.nnn.replace(".mp3", "")
                            self.mu = self.nameS
                            self.strvar_music.set(self.mu)
                            self.songN.configure(text = f"{self.strvar_music.get()}")
                        self.w2.after(round(self.songLength)*1000, change)
                            
                        def returnfunc():
                            return play(cus_music_list[0])
                        self.w2.after(round(self.songLength)*1000, returnfunc)
                x = cus_music_list[0]
                play(x)
                    
            except:
                if len(cus_music_list) < 1:
                    mixer.music.pause()
                    self.w.deiconify()
                    self.w2.destroy()
                    mb.showwarning("Error", "No music was added in the playlist")

    def DisplayImages(self):
        # get pictures
        self.picsFolder = "main\photos"
        list1 = []
        rand_pics_list = []

        # randomphoto
        a = os.listdir(self.picsFolder)
        for path in a:
            if os.path.isfile(os.path.join(self.picsFolder,path)):  
                list1.append(path)
                for i in list1:
                    p = "main\photos\\"
                    i = p+i
                    rand_pics_list.append(i)
        random.shuffle(rand_pics_list)
        try:
            # run photos
            def showpicFunc(x):
                if len(rand_pics_list) > 0:
                    self.img = ImageTk.PhotoImage(Image.open(rand_pics_list[0]))
                    self.showpic = tk.Label(self.w2, text = "", image = self.img, background = "#425462")
                    self.showpic.grid(column = 8, row = 2, sticky = tk.EW, columnspan = 2, rowspan = 4)
                    rand_pics_list.append(rand_pics_list[0])
                    del rand_pics_list[rand_pics_list.index(rand_pics_list[0])]
                    def change():  
                        self.img = ImageTk.PhotoImage(Image.open(rand_pics_list[0]))
                        self.showpic.configure(image = self.img)
                    self.w2.after(round(self.songLength)*1000, change)
                def returnfunc():
                    return showpicFunc(rand_pics_list[0])
                self.w2.after(round(self.songLength)*1000, returnfunc)
            x = rand_pics_list[0]
            showpicFunc(x)
        except:
            pygame.mixer.init()
            mixer.music.pause()
            self.w.deiconify()
            self.w2.destroy()
            mb.showerror("Error", "Please select music")
Started()