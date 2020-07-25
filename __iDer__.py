"""!/usr/bin/env python3
__AUTHOR = "Olanshile Jimoh"
__DATE = "MAR 02 2020 - till date."
"""
import os as gd, subprocess as sp, time
def first_run():
    gd.system ("pip install pyAesCrypt")
    gd.system ("pip install mysql.connector")
    gd.system ("pip install pillow")
    gd.system ("cls")
first_run()
from tkinter import *
from tkinter import (messagebox as mb, filedialog as fd)
from PIL import *
from pyAesCrypt import (encryptFile as enc, decryptFile as dec)
import mysql.connector
from mysql.connector import connection
global relPth, Pth, uhPth
relPth = gd.path.join("C:\\", "iDer", "Scripts", "iDer")
Pth = gd.path.join (relPth, ".iden", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}", "{N3A8E5F9-E63F-D7D8-DD7A-I7671A- HBC781}\\")
uhPth = relPth + "\\Unhidden Files"
config = {"user":"root","password":"whi***d","host":"127.0.0.1","database":"ider"}
while True: #keep the tkinter window open even after the destroy statement from child window. A freaking solution to not being able to call a destroyed tkinter window.
    try:
        def iDer():
            def updateF():
                #this functio should send the user to ider's download page to check for latest updates
                mb.showinfo ("Hello","We are on it!!!")

            def abtF ():
                abtP = Tk()
                abtP.configure (background = "#363277")
                abtP.title("iDER@About-Us")
                abtP.iconbitmap (relPth + "\\Include\\images\\logo.ico")
                abtP.geometry("610x350+340+200")
                Label (abtP, text = "About Us", bg = "#363277", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=15,relwidth=1)
                aboutUs = "iDER is a File Hiding Software geared towards absolute privacy.\nThis project was written and is currently being managed by Olanshile Jimoh, a computer programmer and security/privacy advocate.\n\nThe first version of iDER just like the first version of most of the apps we have written started with just a command line interface.\n\nHowever, we wanted more functionalities, ease of use and above all we wanted to put it out there for everyone to use with ease. But, we knew we couldn't do that without an alluring User Interface and so we set out to write the GUI version.\n\nUse iDER Software to hide your sensitive files in an highly security conscious manner. We care about your privacy, and so should you.\n\nCONTACT US\nEmail: ider@telon.com.ng"
                txt = Text(abtP, width = 70, height = 17, wrap = WORD)
                txt.insert(INSERT, aboutUs)
                txt.place(x=22, y=60)
                abtP.resizable(False, False)
                abtP.mainloop()
                
            def howtF ():
                howtP = Tk()
                howtP.configure (background = "#363277")
                howtP.title("iDER@How-To")
                howtP.iconbitmap (relPth + "\\Include\\images\\logo.ico")
                howtP.geometry("610x350+340+200")
                Label (howtP, text = "iDer's Quick Guide", bg = "#363277", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=15,relwidth=1)
                howText = """Hi there, this is a simple and straightforward how-to guide on using the file hiding software.\n\nFEATURES\nHide: Click the hide button and select the file(s) to hide in the next\npage that pops up and select open. Select "Yes" to proceed to hide the\nfile(s) you have chosen.\n\nUnhide: Click the unhide button, a dialog should pop up containing\nall your hidden files. To unhide, select the file(s) you'd like to\nunhide and then click the "Open" button to proceed to unhide the file(s).\n\nUnhide All: To unhide all files at once, click the "Unhide All" button\nand select "Yes" to proceed to unhide all files."""
                txt = Text(howtP, width = 70, height = 15, wrap = WORD)
                txt.insert(INSERT, howText)
                txt.place(x=22, y=60)
                howtP.resizable(False, False)
                howtP.mainloop()

            def dontF ():
                line = "-" * 70
                dontP = Tk()
                dontP.configure (background = "#363277")
                dontP.title("iDER@Contribute")
                dontP.iconbitmap (relPth + "\\Include\\images\\logo.ico")
                dontP.geometry("610x350+340+200")
                Label (dontP, text = "Work with us", bg = "#363277", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=25,relwidth=1)
                donText = "Hello, if you'd like to assist the programmer you can get in touch with us for Sponsorship, Investment, Grants, Donations and Technical Contributions. Your assistance would definitely go a long way in the continous developnment and improvement of iDER File Hiding Software.\n\nThank you in advance.\n" + line + "\nName: Olanshile Jimoh\nEmail Address: info@telon.com.ng\nLinkedIn: Olanshile Jimoh\nTwitter: Olanshile Jimoh"
                txt = Text(dontP, width = 70, height = 10, wrap = WORD)
                txt.insert(INSERT, donText)
                txt.place(x=22, y=80)
                dontP.resizable(False, False)
                dontP.mainloop()

            def clr(tt=0): #dev
                time.sleep (tt)
                gd.system ("cls")

            def viewF ():
                #CREATE FOLDER TO MOVE UNHIDDEN FILES if !exists
                if gd.path.exists (uhPth) == True: pass
                else:
                    gd.mkdir (uhPth)#else create the folder
                cur.execute ("SELECT file FROM documents WHERE UName = " + "\"" + u + "\" ")
                for p in cur: #temp uh
                    p = p[0]
                    gd.system (anon + "\"" + p + "\"" + " -h -r -s -a")
                    clr()
                fileto = fd.askopenfilename (title = "Hidden file(s) should be visible here: Select file to view", initialdir = Pth)
                #for loop to hide files after user has selected the file to view
                cur.execute ("SELECT file FROM documents WHERE UName = " + "\"" + u + "\" ")
                for p in cur:
                    p = p[0]
                    gd.system (anon + "\"" + p + "\"" + " +h +r +s +a")
                    clr()
                if fileto == "":pass
                else:
                    res = mb.askquestion ("Confirmation", "Do you really want to view this file?")
                    if res == "no":pass
                    else:
                        lFile = "\"" + fileto + "\""
                        lFile = lFile.replace ("/", "\\")
                        gd.system (anon + lFile + " -h -r -s -a")
                        F2d = fileto #unlike system, enc doesnt require the path to the quoted
                        newF2d = fileto.rpartition (".ider")[0]
                        dec (F2d, newF2d, password, bufferSize)
                        #print (newF2d)
                        gd.system ("move " + "\"" + newF2d.replace ("/", "\\") + "\"" + " " + "\"" + uhPth + "\"")
                        fileToView = newF2d.replace ("/", "\\")
                        fileToView = fileToView.rpartition ("}")
                        fileToView = fileToView [2]
                        fileToOpen = ("\"" + uhPth + fileToView + "\"")
                        print (fileToOpen)
                        time.sleep(5)
                        output = gd.system ("\"" + fileToOpen + "\"")
                        if output == 1:mb.showerror ("Error", "Something Happened")
                        else:
                            time.sleep (10)
                            gd.system ("del " + fileToOpen)
