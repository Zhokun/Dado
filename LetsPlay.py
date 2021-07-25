from random import *
from tkinter import *
from tkinter import messagebox


class Dice(Tk):
    """ This is a simple dice guessing game
            We're gonna have numbers to click and a dice to show the result
    """
    def __init__(self):
        Tk.__init__(self)
        # Set main features for the game window
        self.dicelist = []
        self.geometry('400x400+2000+500')
        self.title('Dice Guessing Game')
        # Load images into a dict
        # for dicenumber in range(1, 7):
        #     imgdice = PhotoImage(file=f'D{dicenumber}.jpg')
        #     self.dicelist.append(imgdice)

        # Define Frames to position elements such as dice image and buttons
        # Dice frame positioned in the middle of screen
        self.dice_frame = LabelFrame(self, text='Dice')
        self.dice_frame.pack()
        self.mess = Label(self.dice_frame, text='teste')
        self.mess.pack()
        # Frame to position all numbers from 1 to 6
        self.choice = LabelFrame(self, text='Choice')
        self.choice.pack()

        # Imagem
        img = PhotoImage(file='dicesimg/D2.jpg')
        self.imgdice = Label(self.dice_frame, image=None)
        self.config(image=img)

        self.button_start = Button(self.choice, text='start', )
        self.button_start.pack(side=LEFT)
        self.button_stop = Button(self.choice, text='stop', )


# Start the app in case it is executed from main file
if __name__ == '__main__':
    app = Dice()
    app.mainloop()
