# calculator
from tkinter import *
import sys


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        lab_one = Label(self, text="____________", font="Arial 20").grid(row=0, column=0, columnspan=3, sticky=W)
        lab_sing = Label(self, text="__ ", font="Arial 20").grid(row=1, column=0, columnspan=3, sticky=W)
        lab_two = Label(self, text="____________", font="Arial 20").grid(row=2, column=0, columnspan=3, sticky=W)

        self.ent_calk = Entry(self)
        self.ent_calk.grid(row=3, column=0, ipadx=30, ipady=7, columnspan = 2,  sticky=W)

        self.button_num = StringVar()
        self.button_num.set(None)

        #but = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        # button_num = [1,2,3,4,5,6,7,8,9]
        # column = 0
        # row = 4
        # for i in button_num:
        #     Button(self, text=i, width=15, height=1, command=lambda: self.check_num(i)).grid(row=row, column=column, sticky=W)
        #     column += 1
        #     if column % 3 == 0:
        #         row += 1
        #         column = 0

        but_one = Button(self, text=1, width=15, height=1, command=lambda: self.check_num(1)).grid(row=4, column=0, sticky=W)
        but_two = Button(self, text=2, width=15, height=1, command=lambda: self.check_num(2)).grid(row=4, column=1, sticky=W)
        but_three = Button(self, text=3, width=15, height=1, command=lambda: self.check_num(3)).grid(row=4, column=2, sticky=W)
        but_four = Button(self, text=4, width=15, height=1, command=lambda: self.check_num(4)).grid(row=5, column=0, sticky=W)
        but_five = Button(self, text=5, width=15, height=1, command=lambda: self.check_num(5)).grid(row=5, column=1, sticky=W)
        but_six = Button(self, text=6, width=15, height=1, command=lambda: self.check_num(6)).grid(row=5, column=2, sticky=W)
        but_seven = Button(self, text=7, width=15, height=1, command=lambda: self.check_num(7)).grid(row=6, column=0, sticky=W)
        but_eight = Button(self, text=8, width=15, height=1, command=lambda: self.check_num(8)).grid(row=6, column=1, sticky=W)
        but_nine = Button(self, text=9, width=15, height=1, command=lambda: self.check_num(9)).grid(row=6, column=2, sticky=W)

        but_zero = Button(self, text="0", width=15, height=1, command=lambda: self.check_num(0)).grid(row=7, column=0, sticky=W)

        but_clear = Button(self, text="C", width=15, height=1, command=self.ent_clear).grid(row=7, column=1, sticky=W)

        but_complete = Button(self, text="=", width=15, height=1, command=self.txt_complate).grid(row=7, column=2, sticky=W)

        # ___________________________________________________sing buttom____________________________________________________
        but_amount = Button(self, text="+", width=15, height=1, command=lambda: self.check_sing("+")).grid(row=8, column=0, sticky=W)

        but_difference = Button(self, text="-", width=15, height=1, command=self.txt_complate).grid(row=8, column=1, sticky=W)

        but_myltiply = Button(self, text="*", width=15, height=1, command=self.txt_complate).grid(row=8, column=2, sticky=W)

        but_division = Button(self, text="/", width=15, height=1, command=self.txt_complate).grid(row=9, column=0, sticky=W)

        but_whole = Button(self, text="//", width=15, height=1, command=self.txt_complate).grid(row=9, column=1, sticky=W)

        but_remainder_division  = Button(self, text="%", width=15, height=1, command=self.txt_complate).grid(row=9, column=2, sticky=W)

        # self.button_sing = StringVar()
        # self.button_sing.set(None)
        # sings = ["+", "-", "*", "/", "//", "%"]
        # column1 = 0
        # row = 8
        # for x in sings:
        #     Button(self, text=x, background="#555", command=lambda: self.check_num(x),  width=15, height=1).grid(row=row, column=column1, sticky=W)
        #     column1 += 1
        #     if column1 == 3:
        #         row += 1
        #         column1 = 0

    def check_sing(self, sing):
        self.sing = sing
        num_one = self.ent_calk.get()
        self.lab_one["text"] = num_one
        self.lab_sing["text"] = sing
        self.ent_calk.delete(0, END)


    def check_num(self, number):
        self.number=number
        self.ent_calk.insert(0, number)


    def ent_clear(self):
        self.ent_calk.delete(0, END)


    def txt_complate(self):

        a = self.ent_calk.get()
        c = self.button_sing.get()

        if c == "+":
            d = a + b
            self.ent_calk.delete(0.0, END)
            self.ent_calk.insert(0.0, d)
        elif c == "-":
            d = a - b
            self.ent_calk.delete(0.0, END)
            self.ent_calk.insert(0.0, d)
        elif c == "*":
            d = a * b
            self.ent_calk.delete(0.0, END)
            self.ent_calk.insert(0.0, d)
        elif c == "/":
            d = a / b
            self.ent_calk.delete(0.0, END)
            self.ent_calk.insert(0.0, d)
        else:
            sys.exit()

root=Tk()
root.title("calculate")
root.geometry("420x300")
app=Application(root)

root.mainloop()

