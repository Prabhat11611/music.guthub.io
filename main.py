from tkinter import*
import tkinter.messagebox
import os
import time
from PIL import Image,ImageTk
from pygame import mixer
from tkinter import filedialog
from mutagen.mp3 import MP3     # It is being used to find the song Length.
mixer.init()

#root=Tk()       # These two lines are for creating interface. Variable name can be anything.
#root.mainloop()

class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        # Designing the Interface
        self.root.title('Music_Player')
        self.root.geometry('700x400')
        self.root.configure(background="orange")
#------------------------------------------------------------------------------------#
        #Menu Button
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)
                # File Section

        # Function for Open File
        def OpenFile():
            global filename
            filename=filedialog.askopenfilename()
        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=OpenFile)
        self.submenu.add_command(label='Exit', command=self.root.destroy)
                # About Section
        def About():
            tkinter.messagebox.showinfo('About','This System is purely designed using Python Programming Language. Basically this is made to add it as a Poject for my Portfolio Website.')

        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='About',menu=self.submenu2, command=About)

#------------------------------------------------------------------------------------#
        # Adding Label 
        self.label=Label(text="Prabhat's Music Application....",bg="orange").place(x=50,y=20)

#------------------------------------------------------------------------------------#
        # Song Information
        def song():
            self.filelabel['text']='Current Music:- '+ os.path.basename(filename)

        self.filelabel=Label(text="Music Information will be displayed here.\n First Go to File \n Click on Open\n Select the Music\n Click on Play Button",bg="orange")
        self.filelabel.place(x=350,y=80)

        # Song Length
        def length_bar():
            # Select mp3 songs
            song_mut=MP3(filename)
            # get length of songs
            song_mut_length=song_mut.info.length
            # convert into minute and second
            convert_song_mut_length=time.strftime('%M:%S',time.gmtime(song_mut_length))
            print(convert_song_mut_length)
            # Label
            self.lengthbar=Label(self.root,text='Total_Length:-00:00',bg='black',fg='white',font=20).place(x=5,y=270)
#------------------------------------------------------------------------------------#
        # Adding Image to the Interface
        self.photo=ImageTk.PhotoImage(file='Image\Interface.png')
        photo=Label(self.root,image=self.photo,bg="orange",bd=0).place(x=30,y=50)
#------------------------------------------------------------------------------------#
        # Creating Buttons
            # Function for Play Button
        def play():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    print('Music is Playing now.')
                    self.label2['text']='Music is Playing, Enjoy....'
                    song()
                except: 
                    #pass                    # Pass simply runs the program and does not show any error.
                    tkinter.messagebox.showerror("Error","File not found.")
            else:
                mixer.music.unpause()
                self.label2['text']='Music is now unpaused.'

            # Play Button
        self.photo2=ImageTk.PhotoImage(file='Image\play-button.png')
        photo2=Button(self.root,image=self.photo2,bg="orange",bd=0,command=play).place(x=30,y=200)

#------------------------------------------------------------------------------------#

            # Function for Pause Button
        def pause():
            global paused
            paused=TRUE
            mixer.music.pause()
            print('Music has been Pused.')
            self.label2['text']='Music_Paused.'

            # Pause Button
        self.photo3=ImageTk.PhotoImage(file='Image\pause-button.png')
        photo3=Button(self.root,image=self.photo3,bg="orange",bd=0,command=pause).place(x=80,y=200)

#------------------------------------------------------------------------------------#
            # Previous Button
        self.photo4=ImageTk.PhotoImage(file='Image\previous.png')
        photo4=Button(self.root,image=self.photo4,bg="orange",bd=0).place(x=130,y=200)

#------------------------------------------------------------------------------------#
            # Next Button
        self.photo5=ImageTk.PhotoImage(file='Image\coming-button.png')
        photo5=Button(self.root,image=self.photo5,bg="orange",bd=0).place(x=180,y=200)

#------------------------------------------------------------------------------------#
            # Function for Stop Button
        def stop():
            mixer.music.stop()
            print('Music has been Pused.')
            self.label2['text']='Music_Stopped.'

            # Stop Button
        self.photo6=ImageTk.PhotoImage(file='Image\stop-button.png')
        photo6=Button(self.root,image=self.photo6,bg="orange",bd=0,command=stop).place(x=230,y=200)
#------------------------------------------------------------------------------------#
        
        # Function for Volume Bar
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)

        # Volume Image
        self.photo7=ImageTk.PhotoImage(file='Image\Volume.png')
        photo7=Button(self.root,image=self.photo7,bg="orange",bd=0).place(x=30,y=270)


        # Volume 
        self.scale=Scale(self.root,from_=0,to=100, orient=HORIZONTAL,length=150,bg='gold',command='volume')
        self.scale.set(30)
        self.scale.place(x=80,y=260)
#------------------------------------------------------------------------------------#
        # Footer Label
        self.label2=Label(self.root,text='You are listening to Prabhat Music World....',font=10)
        self.label2.pack(side=BOTTOM,fill=X)

root=Tk()
obj=musicplayer(root)
root.mainloop()