import webbrowser
from playsound import playsound
from tkinter import *
import pygame

screen = Tk()
screen.title("משפחת שווץ")

pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\solom\\Desktop\\Code\\Python\\Mishpachat Shvetz\\soundOfPstttt.mp3")


def press(button):
    pygame.mixer.music.play()
    if button == 1:
        webbrowser.open("https://www.youtube.com/watch?v=XsFe56c_k2c")
    elif button == 2:
        webbrowser.open("https://www.youtube.com/watch?v=qeF3Sx_IGvE")
    elif button == 3:
        webbrowser.open("https://www.youtube.com/watch?v=IsCTJhkO624&t=29s")


msg = Label(text= ":" + "בחר את הפרק שתרצה לראות" , font=20)
msg.grid(row=0 , column=0)

E1 = Button(text="פרק 1" , padx = 400 , pady = 100 , command = lambda : press(1))
E2 = Button(text="פרק 2" , padx = 400 , pady = 100 , command = lambda : press(2))
E3 = Button(text="פרק 3" , padx = 400 , pady = 100 , command = lambda : press(3))


E1.grid(row = 1 , column = 0)
E2.grid(row = 2 , column = 0)
E3.grid(row = 3 , column = 0)
pygame.mixer.music.play()
#time.sleep(5)
#winsound.PlaySound("soundOfPstttt.wav" ,)
screen.mainloop()

