"""!usr/bin/python
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "MAR 02 2019 - till date."
"""
import os as gd, subprocess as sp, time as t
from tkinter import *
from tkinter import (messagebox as mb, filedialog as fd)
from PIL import *
#TODO, bind Keys
#TODO Encrypt location text file for enhanced security
while True: #keep the tkinter window open even after the destroy statement from child window. A freaking solution to not being able to call a destroed tkinter window. Truly happy with myself (^?^)
    try:
        def abtF ():
            abtP = Tk()
            abtP.title("iDER@About-Us")
            abtP.geometry("610x350+340+200")
            titLab = Label (abtP, text = "About Us", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
            aboutUs = "iDER Software is yet another file hider app with multiple features.\nThis project was written and is still managed by Jimoh Idris Olanshile, a computer programmer and a security & privacy advocate.\n\nThe first version of iDER just like the first version of most of the apps I have developed started with just a command line interface.\nHowever, I wanted more functionalities, ease of use and above all I wanted to put it out there for everyone to use for free and I knew I couldn't do that without an alluring User Interface and so i set out to write the GUI version.\n\nUse iDER Software to hide your sensitive files in a highly security conscious manner. We care about your privacy, and so should you.\nCONTACT US:\nEmail: ider@telon.com\nMobile Number: +233203450788\n"
            txt = Text(abtP, width = 70, height = 17, wrap = WORD)
            txt.insert(INSERT, aboutUs)
            txt.place(x=22, y=60)
            abtP.mainloop()
            
        def howtF ():
            howtP = Tk()
            howtP.title("iDER@How-To")
            howtP.geometry("610x350+340+200")
            titLab = Label (howtP, text = "How to iDER", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
            howText = ""
            txt = Text(howtP, width = 70, height = 15, wrap = WORD)
            txt.insert(INSERT, howText)
            txt.place(x=25, y=60)
            howtP.mainloop()

        def dontF ():
            line = "-" * 70
            dontP = Tk()
            dontP.title("iDER@Assist-us")
            dontP.geometry("610x350+340+200")
            titLdon = Label (dontP, text = "Assist The Programmer", font = ("times new roman", 15, "bold")).place (x=0,y=25,relwidth=1)
            donText = "I truly appreciate your interest to make a donation as your donation would go a long way in the developnment and the continual improvement of TeLon no matter how little it may be, Thank you in advance.\n\n\n" + line + "\nBank Name: GtBank\nAccount Name: Jimoh Idris Olanshile\nAccount Number: 0202884092\nPhone Number: +2348159344489"
            txt = Text(dontP, width = 70, height = 10, wrap = WORD)
            txt.insert(INSERT, donText)
            txt.place(x=25, y=80)
            dontP.mainloop()

        def clr(tt=0): #for testing purposes
            t.sleep (tt)
            gd.system ("cls")
        def uhALL ():
            try:
                hiddenF = open (relPth + "\\filenames.txt", "r")
                files = hiddenF.readlines ()
                if files == []: #if the list is empty, which is the case if the files have been unhidden by the user.
                    mb.showerror ("Error", "Hide a file to continue")
                else:
                    res = mb.askquestion ("Confirmation", "Do you really want to unhide all files?")
                    if res == "no":pass
                    else:
                        for fPth in files:
                            ######str manipulation (right partition) to remove new line
                            fPth = fPth.rpartition("\n")
                            fPth = fPth [0]
                            ####more str manipulation (left partition) to remove "1:" from the file path
                            fPth = fPth.partition (": ")
                            fPth = fPth [2]
                            fPth = fPth.replace("/", "\\") #replace / to the windows version \, and also make it \\ in order to be in sync with path.join
                            gd.system ("attrib " + "\"" + fPth + "\"" + " -h -r -s -a")
                            ###create folder to move all unhidden files if it doesnt exist
                            uhPth = relPth + "\\Unhidden Files"
                            if gd.path.exists (uhPth) == True: pass
                            else:
                                gd.mkdir (uhPth)
                            gd.system ("move " + "\"" + fPth + "\"" + " " + "\"" + uhPth + "\"") #would have loved to check the output of this operation and perform an IFTTT operation on it but sp doesnt work that close with files, I just have to make do with the the OS's ystem class
                            clr()
                        hiddenF = open ("./filenames.txt", "w") #open the file in write mod e to delete all files after unhiding them all.
                        hiddenF.close()
                        mb.showinfo ("Success", "Files have been unhidden and moved to!!!\n" + uhPth)
                        gd.chdir ("./Unhidden Files")
                        gd.system ("start.")
            except FileNotFoundError: #gets thrown if the text file to be read hasnt beeen created at all, meaning the user is a first time user or has deleted the file.
                mb.showerror ("Error", "Hide a file to continue!!!")

        def h():#TODO add time of hiding at the top of each operation, #TODO, new idea with unhiding files by launching filedialog
            fPth = fd.askopenfilenames (title = "Choose file(s) to hide")
            if fPth == "":
                mb.showerror ("Error", "You need to choose a file to continue")
            else:
                resH = mb.askquestion ("Confirmation", "Proceed to hide file(s) ?")
                if resH == "yes":
                    num = 0
                    for p in fPth:
                        num += 1
                        gd.system ("attrib " + "\"" + p + "\"" + " +h +r +s +a")
                        files = open ("./filenames.txt", "a") #open text file to save files for unhiding. files are opened in "a" appending mode; "a" mode doesnt overwrite existing file if it exists unlike "w"
                        files.write (str (num) + ": " + p + "\n")
                        files.close () #close the file save our changes, written texts dont appear unless you close.
                    mb.showinfo ("Success", "File(s) has been hidden and path has been saved to filenames.txt.")

        def uh():
            def doUh():
                fPth = uhVar.get()
                if fPth == "": #if its empty. echo an error
                    mb.showerror ("Error", "You need to put a file to proceed!!!")
                else:
                    resU = mb.askquestion ("Confirmation", "Do you really want to unhide these file(s)?")
                    if resU == "yes":
                        uhOut = sp.check_output ("attrib " + "\"" + fPth + "\"" + " -h -r -s -a")
                        if "not found" in str(uhOut) or "not correct" in str(uhOut): #handle error that gets thrown if the right file or the right file structure wasnt provided.
                            mb.showerror ("Error", "Value not understood\nCheck that you've put in the right file")
                        else:mb.showinfo ("Success", "File has been unhidden.")
            try:
                hiddenFiles = open ("./filenames.txt", "r") #open the file in read only mode.
                h = hiddenFiles.read() #read contents of the open file. #thehiddenfiles
                if h == "":
                    mb.showerror ("Error", "All files have been unhidden")
                else:
                    hMain.destroy ()
                    uh = Tk()
                    uh.title ("Hidden Files")
                    uh.geometry ("650x400+320+150")
                    bgPic=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/back.png")
                    uhBackground = Label(uh, image=bgPic).place (relwidth=1, relheight=1)
                    uhText = Text (uh, height = 2, width = 75, wrap = WORD, state = "normal")
                    uhText.place (y = 30, x = 23)
                    uhText.insert (INSERT, "::Hidden Files::Copy & Paste the file you would like to unhide to comtinue")
                    uhText.insert (INSERT, "\n" + "+" * 75 + "\n\n")
                    fileText = Text (uh, height = 15, width = 60, wrap = WORD)
                    fileText.place (y = 80, x =80)
                    fileText.insert(INSERT, h)
                    uhVar = StringVar ()
                    uhLabel = Label (uh, text = "File", bg = "RED", fg = "WHITE").place (x = 170, y = 350)
                    uhEntry = Entry (uh, textvariable = uhVar, width = 40, relief = GROOVE).place (x = 200, y = 350)
                    uhBtn = Button (uh, text = "Go", command = doUh).place (x = 450, y = 348)
                    hiddenFiles.close() #close opened file.
                    uh.mainloop()
            except FileNotFoundError: #built in exception that gets raised when the text file doesnt exist, meaning; the file hasnt been created which also means that the user havent hidden any file.
                mb.showerror("Error", "Hide a file to continue!!!")

        relPth = gd.path.join("C:\\", "virtualenvironment", "py", "iDer")
        gd.chdir (relPth)
        hMain = Tk()
        ########create app menu
        menubar = Menu(hMain)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Hide", command=h)
        filemenu.add_command(label="Unhide", command=uh)
        filemenu.add_command(label="Unhide ALL", command=uhALL)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=hMain.quit)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="Donate", command=dontF)
        helpmenu.add_command(label="About Us", command=abtF)
        helpmenu.add_command(label="How to use", command=howtF)

        hMain.config(menu=menubar)
        hMain.geometry ("650x400+320+150")
        hMain.title ("iDer: Powered by TeLon")
        bgPic=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/back.png")
        hMainLogo=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/cn.png")
        hMainBackground = Label(hMain, image=bgPic)
        hMainBackground.place (relwidth=1, relheight=1)
        title = Label(hMain, text = "File Hider", font = ("times new roman", 30, "bold"), bg = "#2896e0", fg = "WHITE", bd = 10, relief = FLAT)
        title.place (x=0,y=0,relwidth=1)
        hMainFrame = Frame (hMain, bg="WHITE")
        hMainFrame.place(x=170, y=150)
        logoL = Label(hMainFrame, image = hMainLogo, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
        hBtn = Button(hMainFrame, relief = GROOVE, command = h, text = "Hide", bg = "#2896e0", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 0, pady = 10)           
        uhBtn = Button(hMainFrame, relief = GROOVE, text = "Unhide", command = uh, bg = "#2896e0", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 1)
        uhALL = Button(hMain, relief = GROOVE, text = "Unhide All", command = uhALL, bg = "RED", width = 10, fg = "WHITE", font = ("times new roman", 15, "bold")).place(x = 530, y = 15)
        hMain.mainloop()
    except TclError: #Error gets called if the window was destroyed with the menu button exit key
        break


                        ##########DONE##############
            #create function to unhide all files at once.
            #Unhidden files should be automatically moved to a folder
            #prompt user before unhiding all files

            #TODO, users should be able to view and select their hidden files in a more friendly way
            #TODO, add feature to hide and unhide a whole folder
