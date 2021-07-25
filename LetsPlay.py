from tkinter import *
# from tkinter import messagebox
from random import *
from PIL import ImageTk, Image


class Dice(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.menu_arquivo = Menu(self.menu, tearoff=False)
        self.menu_arquivo.add_command(label='Sair', command=self.quit)
        self.menu.add_cascade(label='Arquivo', menu=self.menu_arquivo)

        # Define features of Game Window
        self.geometry(f'400x400+'
                      f'{int((self.winfo_screenwidth()/2) - (400/2))}+{int((self.winfo_screenheight()/2) - (400/2))}')  # Geometry and position on screen
        self.title('Dice guessing game')  # Window title
        self.iconphoto(True, PhotoImage(file='Da.png'))  # Icon / My signature
        self.config(background='white')
        # self.img = ImageTk.PhotoImage(Image.open('D1.png'))
        self.dices = {}
        # Store all images inside a dictionary
        for dicenb in range(1, 7):
            self.img = ImageTk.PhotoImage(Image.open(f'D{dicenb}.png'))
            self.dices[dicenb] = self.img

        # Dice Frame
        self.dice_frame = Frame(self)
        self.dice_frame.pack()
        # Dice image inside Dice Frame
        self.diceimg = Label(self.dice_frame, image=self.img, border=0)
        self.diceimg.pack()
        # Set a tuple to store default font
        fonttext = ('Verdana', 10)
        fontnumbersize = ('Verdana', 25)
        # Message befor numbers
        self.message_frame = Frame(self)
        self.message_frame.pack()
        message = 'Which number do you think the dice is going to stop at?'
        self.message_label = Label(self.message_frame, text=message, font=fonttext, background='white')
        self.message_label.pack()
        # Numbers to choose Frame
        self.n_choose_frame1 = Frame(self, background='white')
        self.n_choose_frame1.pack()
        self.n_choose_frame2 = Frame(self, background='white')
        self.n_choose_frame2.pack()
        # Numbered buttons
        self.n1 = Button(self.n_choose_frame1, text='1', width=3, font=fontnumbersize,
                         command=self.opn1, background='white')
        self.n1.pack(side=LEFT, anchor=N, padx=3)
        self.n2 = Button(self.n_choose_frame1, text='2', width=3, font=fontnumbersize,
                         command=self.opn2, background='white')
        self.n2.pack(side=LEFT, anchor=N, padx=3)
        self.n3 = Button(self.n_choose_frame1, text='3', width=3, font=fontnumbersize,
                         command=self.opn3, background='white')
        self.n3.pack(side=LEFT, anchor=N, padx=3)
        self.n4 = Button(self.n_choose_frame2, text='4', width=3, font=fontnumbersize,
                         command=self.opn4, background='white')
        self.n4.pack(side=LEFT, anchor=S, padx=3 )
        self.n5 = Button(self.n_choose_frame2, text='5', width=3, font=fontnumbersize,
                         command=self.opn5, background='white')
        self.n5.pack(side=LEFT, anchor=S, padx=3)
        self.n6 = Button(self.n_choose_frame2, text='6', width=3, font=fontnumbersize,
                         command=self.opn6, background='white')
        self.n6.pack(side=LEFT, anchor=S, padx=3)

        # Victorious?
        self.r_frame = Frame(self)
        self.r_frame.pack()
        self.result = Label(self.r_frame, background='white')
        self.result.pack()

        self.tempo = 0

    # Button 1
    def opn1(self):
        start = True
        randimg = randint(1, 6)
        self.result.config(text='')
        self.diceimg.config(image=self.dices[randimg])

        if self.tempo > 0.95:
            self.tempo = 0
            start = False  # Stop the next image from appearing
            # self.after_cancel(cancela)
            if randimg == 1:  # Check if user choice equals dice, if so, the message 'You Won' will appear
                self.result.config(text='You Won', font=('Verdana', 20), fg='green')
            else:
                self.result.config(text='Better luck next time!', font=('Verdana', 20), fg='red')

        self.tempo += 0.05
        # A simple timer to change image e make it more dynamic
        if start:
            if self.tempo < 0.3:
                self.after(100, self.opn1)
            elif self.tempo < 0.7:
                self.after(200, self.opn1)
            elif self.tempo < 1:
                self.after(300, self.opn1)

    # Button 2
    def opn2(self):
        start = True
        randimg = randint(1, 6)
        self.result.config(text='')
        self.diceimg.config(image=self.dices[randimg])

        if self.tempo > 0.95:
            self.tempo = 0
            start = False  # Stop the next image from appearing
            # self.after_cancel(cancela)
            if randimg == 2:  # Check if user choice equals dice, if so, the message 'You Won' will appear
                self.result.config(text='You Won', font=('Verdana', 20), fg='green')
            else:
                self.result.config(text='Better luck next time!', font=('Verdana', 20), fg='red')

        self.tempo += 0.05
        # A simple timer to change image e make it more dynamic
        if start:
            if self.tempo < 0.3:
                self.after(100, self.opn2)
            elif self.tempo < 0.7:
                self.after(200, self.opn2)
            elif self.tempo < 1:
                self.after(300, self.opn2)

    # Button 3
    def opn3(self):
        start = True
        randimg = randint(1, 6)
        self.result.config(text='')
        self.diceimg.config(image=self.dices[randimg])

        if self.tempo > 0.95:
            self.tempo = 0
            start = False  # Stop the next image from appearing
            # self.after_cancel(cancela)
            if randimg == 3:  # Check if user choice equals dice, if so, the message 'You Won' will appear
                self.result.config(text='You Won', font=('Verdana', 20), fg='green')
            else:
                self.result.config(text='Better luck next time!', font=('Verdana', 20), fg='red')

        self.tempo += 0.05

        # A simple timer to change image e make it more dynamic
        if start:
            if self.tempo < 0.3:
                self.after(100, self.opn3)
            elif self.tempo < 0.7:
                self.after(200, self.opn3)
            elif self.tempo < 1:
                self.after(300, self.opn3)

    # Button 4
    def opn4(self):
        start = True
        randimg = randint(1, 6)
        self.result.config(text='')
        self.diceimg.config(image=self.dices[randimg])

        if self.tempo > 0.95:
            self.tempo = 0
            start = False  # Stop the next image from appearing
            # self.after_cancel(cancela)
            if randimg == 4:  # Check if user choice equals dice, if so, the message 'You Won' will appear
                self.result.config(text='You Won', font=('Verdana', 20), fg='green')
            else:
                self.result.config(text='Better luck next time!', font=('Verdana', 20), fg='red')

        self.tempo += 0.05
        # A simple timer to change image e make it more dynamic
        if start:
            if self.tempo < 0.3:
                self.after(100, self.opn4)
            elif self.tempo < 0.7:
                self.after(200, self.opn4)
            elif self.tempo < 1:
                self.after(300, self.opn4)

    # Button 5
    def opn5(self):
        start = True
        randimg = randint(1, 6)
        self.result.config(text='')
        self.diceimg.config(image=self.dices[randimg])

        if self.tempo > 0.95:
            self.tempo = 0
            start = False  # Stop the next image from appearing
            # self.after_cancel(cancela)
            if randimg == 5:  # Check if user choice equals dice, if so, the message 'You Won' will appear
                self.result.config(text='You Won', font=('Verdana', 20), fg='green')
            else:
                self.result.config(text='Better luck next time!', font=('Verdana', 20), fg='red')

        self.tempo += 0.05
        # A simple timer to change image e make it more dynamic
        if start:
            if self.tempo < 0.3:
                self.after(100, self.opn5)
            elif self.tempo < 0.7:
                self.after(200, self.opn5)
            elif self.tempo < 1:
                self.after(300, self.opn5)

# Button 6
    def opn6(self):
        start = True
        randimg = randint(1, 6)
        self.result.config(text='')
        self.diceimg.config(image=self.dices[randimg])

        if self.tempo > 0.95:
            self.tempo = 0
            start = False  # Stop the next image from appearing
            # self.after_cancel(cancela)
            if randimg == 6:  # Check if user choice equals dice, if so, the message 'You Won' will appear
                self.result.config(text='You Won', font=('Verdana', 20), fg='green')
            else:
                self.result.config(text='Better luck next time!', font=('Verdana', 20), fg='red')

        self.tempo += 0.05
        # A simple timer to change image e make it more dynamic
        if start:
            if self.tempo < 0.3:
                self.after(100, self.opn6)
            elif self.tempo < 0.7:
                self.after(200, self.opn6)
            elif self.tempo < 1:
                self.after(300, self.opn6)


if __name__ == '__main__':
    app = Dice()
    app.mainloop()
