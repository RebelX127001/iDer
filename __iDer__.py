"""!usr/bin/python
__AUTHOR = "Idris Olanshile Jimoh"
__DATE = "MAR 02 2020 - till date."
__VERSION = "3"
"""
while True: #keep the tkinter window open even after the destroy statement from child window. A freaking solution to not being able to call a destroyed tkinter window.
    try:
        def ex():
            res = mb.askquestion ("Confirmation", "Do you really want to leave?")
            if res == "no":pass
            else:hMain.quit()

        def updateF():
            #this functio should send the user to ider's download page to check for latest updates
            mb.showinfo ("Attention","We are on it!!!")

        def abtF ():
            abtP = Tk()
            abtP.configure (background = "#363277")
            abtP.title("iDER@About-Us")
            abtP.geometry("610x350+340+200")
            titLab = Label (abtP, text = "About Us", bg = "#363277", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=15,relwidth=1)
            aboutUs = "iDER is a File Hiding Software geared towards absolute privacy.\nThis project was written and managed by Olanshile Jimoh, a computer programmer and security/privacy advocate.\n\nThe first version of iDER just like the first version of most of the apps we have written started with just a command line interface.\n\nHowever, we wanted more functionalities, ease of use and above all we wanted to put it out there for everyone to use with ease. But, we knew we couldn't do that without an alluring User Interface and so we set out to write the GUI version.\n\nUse iDER Software to hide your sensitive files in an highly security conscious manner. We care about your privacy, and so should you.\n\nCONTACT US\nEmail: ider@telon.com.ng"
            txt = Text(abtP, width = 70, height = 17, wrap = WORD)
            txt.insert(INSERT, aboutUs)
            txt.place(x=22, y=60)
            abtP.mainloop()
            
        def howtF ():
            howtP = Tk()
            howtP.configure (background = "#363277")
            howtP.title("iDER@How-To")
            howtP.geometry("610x350+340+200")
            titLab = Label (howtP, text = "iDer's Quick Guide", bg = "#363277", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=15,relwidth=1)
            howText = """Hi there, this is a simple and straightforward how-to guide on using the file hiding software.\n\nFEATURES\nHide: Click the hide button and select the file(s) to hide in the next\npage that pops up and select open. Select "Yes" to proceed to hide the\nfile(s) you have chosen.\n\nUnhide: Click the unhide button, a dialog should pop up containing\nall your hidden files. To unhide, select the file(s) you'd like to\nunhide and then click the "Open" button to proceed to unhide the file(s).\n\nUnhide All: To unhide all files at once, click the "Unhide All" button\nand select "Yes" to proceed to unhide all files."""
            txt = Text(howtP, width = 70, height = 15, wrap = WORD)
            txt.insert(INSERT, howText)
            txt.place(x=22, y=60)
            howtP.mainloop()

        def dontF ():
            line = "-" * 70
            dontP = Tk()
            dontP.configure (background = "#363277")
            dontP.title("iDER@Contribute")
            dontP.geometry("610x350+340+200")
            titLdon = Label (dontP, text = "Work with us", bg = "#363277", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=25,relwidth=1)
            donText = "Hello, if you'd like to assist the programmer you can get in touch with us for Sponsorship, Investment, Grants, Donations and Technical Contributions. Your assistance would definitely go a long way in the continous developnment and improvement of iDER File Hiding Software.\n\nThank you in advance.\n" + line + "\nName: Olanshile Jimoh\nEmail Address: info@telon.com.ng\nLinkedIn: Olanshile Jimoh\nTwitter: Olanshile Jimoh"
            txt = Text(dontP, width = 70, height = 10, wrap = WORD)
            txt.insert(INSERT, donText)
            txt.place(x=22, y=80)
            dontP.mainloop()

        def clr(tt=0): #for testing purposes
            t.sleep (tt)
            gd.system ("cls")
        def uhALL ():
            Pth = gd.path.join (relPth, ".iden", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}\\")
            try:
                hiddenF = open (Pth + "system/neddih.xml", "r")
                files = hiddenF.readlines ()
                if files == []: #if the list is empty, which is the case if the files have been unhidden by the user.
                    mb.showerror ("Error", "Hide a file to continue")
                else:
                    res = mb.askquestion ("Confirmation", "Do you really want to unhide all files?")
                    if res == "no":pass
                    else:
                        for f in files:
                            ######str manipulation (right partition) to remove new line
                            f = f.rpartition("\n")
                            f = f [0]
                            f = f.replace("/", "\\") #replace / to the windows version \, and also make it \\ in order to be in sync with path.join
                            f = f.rpartition("\\")
                            f = f[2]
                            gd.system (anon + "\"" + Pth + f + "\"" + " -h -r -s -a")
                            ###create folder to move all unhidden files if it doesnt exist
                            uhPth = relPth + "\\Unhidden Files"
                            if gd.path.exists (uhPth) == True: pass #if file exists, do nothing
                            else:
                                gd.mkdir (uhPth)#else create the folder
                            
                            fNew = f.rpartition (".ider")[0]
                            try:dec (Pth + f, fNew, password, bufferSize)
                            except OSError:pass
                            gd.system ("move " + "\"" + Pth + fNew + "\"" + " " + "\"" + uhPth + "\"")
                            gd.system ("del " + "\"" + Pth + f + "\"")
                            #clr()
                        hiddenF = open (Pth + "system\\neddih.xml", "w") #open the file in write mode to delete all files after unhiding them all.
                        hiddenF.close()
                        #mb.showinfo ("Success", "Files have been unhidden and moved to!!!\n" + uhPth)
                        uhPth = gd.path.join ("C:\\", "virtualenvironment", "iDer", "Unhidden Files")
                        gd.chdir(uhPth)
                        gd.system ("start.")
            except FileNotFoundError: #gets thrown if the text file to be read hasnt beeen created at all, meaning the user is a first time user or has deleted the file.
                mb.showerror ("Error", "Hide a file to continue!!!")

        def h():
            Pth = gd.path.join (relPth, ".iden", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}\\")
            gd.chdir (Pth)
            fP = fd.askopenfilenames (title = "Select file(s) to hide")
            if fP == "":
                mb.showerror ("Error", "You need to select a file to continue")
            else:
                resH = mb.askquestion ("Confirmation", "Proceed to hide file(s) ?")
                if resH == "yes":
                    for p in fP:
                        p = p.replace ("/", "\\")
                        gd.system ("move " + "\"" + p + "\"" + " " + "\"" + Pth + "\"")
                        fn = p.rpartition ("\\")
                        fn = fn [2]
                        F2e = Pth + fn
                        newF2e = Pth + fn + ".ider"
                        enc (F2e, newF2e, password, bufferSize)
                        #print (F2e)
                        gd.system ("del " + "\"" + F2e + "\"")
                        gd.system (anon + "\"" + newF2e + "\"" + " +h +r +s +a")
                        files = open ("system/neddih.xml", "a")
                        files.write (newF2e + "\n")
                        files.close()
                        #clr()
                    mb.showinfo ("Success", "File(s) have been securely hidden.")

        def uh():
            #CREATE FOLDER TO MOVE UNHIDDEN FILES if !exists
            uhPth = relPth + "\\Unhidden Files"
            if gd.path.exists (uhPth) == True: pass
            else:
                gd.mkdir (uhPth)#else create the folder
            #####TEMPORARILY UNHIDE THE FILES IN THE HIDDEN FOLDER
            Pth = gd.path.join (relPth, ".iden", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}\\")
            tFile = open (Pth + "system/neddih.xml", "r")
            F = tFile.readlines()
            if F == []:
                mb.showerror ("Error", "Hide a file to continue")
            else:
                for p in F: #temp uh
                    p = p.rpartition ("\n")
                    p = p[0]
                    gd.system (anon + "\"" + p + "\"" + " -h -r -s -a")
                    #clr()
                files = fd.askopenfilenames (title = "Hidden should be visible here: Select file(s) to unhide", initialdir = Pth)
                #for loop to hide files after user has selected the main files to unhide
                for p in F:
                    p = p.rpartition ("\n")
                    p = p[0]
                    gd.system (anon + "\"" + p + "\"" + " +h +r +s +a")
                    
                if files == "":
                    mb.showerror ("Error", "You need to select a file to continue")
                else:
                    res = mb.askquestion ("Confirmation", "Do you really want to unhide this file(s)?")
                    if res == "no":pass
                    else:
                        for f in files: #MAIN LOOP: unhide user selected files
                            lFile = "\"" + f + "\""
                            lFile = lFile.replace ("/", "\\")
                            gd.system (anon + lFile + " -h -r -s -a")
                            F2d = f #unlike system, enc doesnt require the path to the quoted
                            newF2d = f.rpartition (".ider")[0]
                            dec (F2d, newF2d, password, bufferSize)
                            #print (newF2d)
                            gd.system ("move " + "\"" + newF2d.replace ("/", "\\") + "\"" + " " + "\"" + uhPth + "\"")
                            gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                            #clr()
                        gd.chdir(uhPth)
                        gd.system ("start.")

        password = "passToUse"
        bufferSize = 64 * 1024
        anon = "attrib "
        relPth = gd.path.join("C:\\", "virtualenvironment", "iDer", "Scripts", "iDer")
        gd.chdir (relPth)
        hMain = Tk()
        menubar = Menu(hMain)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Run", menu=filemenu)
        filemenu.add_command(label="Hide", command=h)
        filemenu.add_command(label="Unhide", command=uh)
        filemenu.add_command(label="Unhide ALL", command=uhALL)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=ex)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=helpmenu)
        helpmenu.add_command(label="Help", command=dontF)
        helpmenu.add_command(label="Update", command=updateF)
        helpmenu.add_command(label="About Us", command=abtF)

        hMain.config(menu=menubar)
        hMain.geometry ("650x400+320+150")
        hMain.title ("iDer: Powered by TeLon")
        bgPic=PhotoImage(file="C:/Virtualenvironment/iDer/Scripts/iDer/Include/images/ider-back.png")
        hMainLogo=PhotoImage(file="C:/Virtualenvironment/iDer/Scripts/iDer/Include/images/logo.png")
        hMainBackground = Label(hMain, image=bgPic)
        hMainBackground.place (relwidth=1, relheight=1)
        title = Label(hMain, text = "File Hider", font = ("ROBOTO", 30, "bold"), bg = "#8E388E", fg = "WHITE", bd = 10, relief = FLAT)
        title.place (x=0,y=30,relwidth=1)
        hMainFrame = Frame (hMain, bg="WHITE")
        hMainFrame.place(x=170, y=120)
        logoL = Label(hMainFrame, image = hMainLogo, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
        hBtn = Button(hMainFrame, relief = FLAT, command = h, text = "Hide", bg = "#42327A", activebackground = "#0F2F6D", activeforeground = "WHITE", width = 6, fg = "WHITE", font = ("ROBOTO", 15, "bold")).grid(row = 4, column = 0, pady = 10)           
        uhBtn = Button(hMainFrame, relief = FLAT, text = "Unhide", command = uh, bg = "#42327A", activebackground = "#0F2F6D", activeforeground = "WHITE", width = 6, fg = "WHITE", font = ("ROBOTO", 15, "bold")).grid(row = 4, column = 1)
        uhALL = Button(hMain, relief = FLAT, text = "Unhide All", command = uhALL, bg = "#42327A", width = 10, activebackground = "#42327A", activeforeground = "WHITE", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place(x = 530, y = 120)
        quickG = Button(hMain, relief = FLAT, text = "Quick Guide >>", command = howtF, bg = "#233072", activebackground = "#233072", activeforeground = "WHITE", width = 15, fg = "WHITE", font = ("ROBOTO", 8, "")).place(x = 565, y = 380)
        hMain.mainloop()
    except TclError: #gets called if the window was destroyed with the menu button exit key
        break


                        ##########DONE##############
            #add menus
            #create function to unhide all files at once.
            #Unhidden files should be automatically moved to a folder
            #prompt user before unhiding all files
            #Change background image and a logo
            #users should be able to view and select their hidden files in a more friendly way: resume with this.
            #Encrypt the files after anonymization
            

            #TODO Setup to create all needed folders at once if !exist, also add commonly used folder path to variable for easy access
            #TODO Port to sqlite, to solve::::>> remove files from file after file has been unhidden

            #PROBLEMS:
                #Files remain in the textfile after calling uh(). This problem has actually been solved in uhAll() but same solution can not be applied; read throUgh to code to figure oUt the why.
                #should map and compare the fd input to the lines in the xml file. if present, truncate. >> not feasible, use sqlite instead
                #very slow when trying to unhide after a lot of files has been hidden.
