from tkinter import *
from tkinter import font


class Entering:

    window = Tk()
    window.title("Calculator")
    window.geometry("355x500")
    board = Entry(window, bd=10, relief=SUNKEN, justify=RIGHT, font=font.Font(size=30), width=15)
    board.grid(row=0, columnspan=4, ipady=35)


class InsertClick(Entering):

    def button_1_click(self):
        self.board.insert(END, '1')

    def button_2_click(self):
        self.board.insert(END, '2')

    def button_3_click(self):
        self.board.insert(END, '3')

    def button_4_click(self):
        self.board.insert(END, '4')

    def button_5_click(self):
        self.board.insert(END, '5')

    def button_6_click(self):
        self.board.insert(END, '6')

    def button_7_click(self):
        self.board.insert(END, '7')

    def button_8_click(self):
        self.board.insert(END, '8')

    def button_9_click(self):
        self.board.insert(END, '9')

    def button_0_click(self):
        self.board.insert(END, '0')

    def button_comma_click(self):
        self.board.insert(END, ".")


class Math(Entering):

    def __init__(self):
        self.num_add = ""
        self.num_sub = ""
        self.num_multi = ""
        self.num_div = ""
        self.num_sqr = ""
        self.num_power = ""
        self.func = OtherFunctions()

    def add_bind(self, event):
        self.func.backspace()
        self.add()

    def sub_bind(self, event):
        self.func.backspace()
        self.subtraction()

    def multi_bind(self, event):
        self.func.backspace()
        self.multiplication()

    def div_bind(self, event):
        self.func.backspace()
        self.division()

    def equal_bind(self, event):
        self.func.backspace()
        self.equal()

    def add(self):
        self.num_add = self.board.get()
        self.board.delete(0, END)

    def subtraction(self):
        self.num_sub = self.board.get()
        self.board.delete(0, END)

    def multiplication(self):
        self.num_multi = self.board.get()
        self.board.delete(0, END)

    def division(self):
        self.num_div = self.board.get()
        self.board.delete(0, END)

    def sqr(self):
        self.num_sqr = self.board.get()
        self.board.delete(0, END)

    def power(self):
        self.num_power = self.board.get()
        self.board.delete(0, END)

    def too_much(self, result):
        if len(result) > 15:
            self.board.delete(0, END)
            self.board.insert(END, "Number too long!")
        else:
            self.board.insert(END, str(result))

    def equal(self):
        self.second_num = self.board.get()
        self.board.delete(0, END)
        if self.num_add != "":
            try:
                result = float(self.num_add) + float(self.second_num)
                result = round(result, 3)
                self.too_much(str(result))
            except ValueError:
                self.board.insert(END, "Enter Digit!")

        elif self.num_sub != "":
            try:
                result = float(self.num_sub) - float(self.second_num)
                result = round(result, 3)
                self.too_much(str(result))
            except ValueError:
                self.board.insert(END, "Enter Digit!")

        elif self.num_multi != "":
            try:
                result = float(self.num_multi) * float(self.second_num)
                result = round(result, 3)
                self.too_much(str(result))
            except ValueError:
                self.board.insert(END, "Enter Digit!")

        elif self.num_div != "":
            try:
                result = float(self.num_div) / float(self.second_num)
                result = round(result, 3)
                self.too_much(str(result))
            except ValueError:
                self.board.insert(END, "Enter Digit!")

        elif self.num_power != "":
            try:
                if self.num_power != "0" and self.num_power != '0.0':
                    result = float(self.num_power) ** 2
                    result = round(result, 3)
                    self.too_much(str(result))
                else:
                    self.board.insert(END, "1")
            except ValueError:
                self.board.insert(END, "Enter Digit!")

        elif self.num_sqr != "":
            try:
                result = float(self.num_sqr) ** (1/2)
                result = round(result, 3)
                self.too_much(str(result))
            except ValueError:
                self.board.insert(END, "Enter Digit!")

        self.__init__()


class OtherFunctions(Entering):

    def backspace(self):
        length = str(self.board.get())
        self.board.delete(len(length) - 1, END)

    def clean(self):
        self.board.delete(0, END)


class Interface(Entering):

    def __init__(self):

        self.click = InsertClick()
        self.other = OtherFunctions()
        self.calc = Math()
        self.font_size = font.Font(size=24)

    def buttons(self):

        button1 = Button(self.window, text="1", command=self.click.button_1_click, bg="light gray", font=self.font_size)
        button1.grid(row=4, column=0, ipady=4, ipadx=19)

        button2 = Button(self.window, text="2", command=self.click.button_2_click, bg="light gray", font=self.font_size)
        button2.grid(row=4, column=1, ipady=4, ipadx=19)

        button3 = Button(self.window, text="3", command=self.click.button_3_click, bg="light gray", font=self.font_size)
        button3.grid(row=4, column=2, ipady=4, ipadx=19)

        button4 = Button(self.window, text="4", command=self.click.button_4_click, bg="light gray", font=self.font_size)
        button4.grid(row=3, column=0, ipady=4, ipadx=19)

        button5 = Button(self.window, text="5", command=self.click.button_5_click, bg="light gray", font=self.font_size)
        button5.grid(row=3, column=1, ipady=4, ipadx=19)

        button6 = Button(self.window, text="6", command=self.click.button_6_click, bg="light gray", font=self.font_size)
        button6.grid(row=3, column=2, ipady=4, ipadx=19)

        button7 = Button(self.window, text="7", command=self.click.button_7_click, bg="light gray", font=self.font_size)
        button7.grid(row=2, column=0, ipady=4, ipadx=19)

        button8 = Button(self.window, text="8", command=self.click.button_8_click, bg="light gray", font=self.font_size)
        button8.grid(row=2, column=1, ipady=4, ipadx=19)

        button9 = Button(self.window, text="9", command=self.click.button_9_click, bg="light gray", font=self.font_size)
        button9.grid(row=2, column=2, ipady=4, ipadx=19)

        button0 = Button(self.window, text="0", command=self.click.button_0_click, bg="light gray", font=self.font_size)
        button0.grid(row=5, column=1, ipady=6, ipadx=19)

        button_comma = Button(self.window, text=",", command=self.click.button_comma_click, bg="light gray", font=self.font_size)
        button_comma.grid(row=5, column=2, ipady=6, ipadx=24)

        button_clean = Button(self.window, text="C", command=self.other.clean, bg="light gray", font=self.font_size)
        button_clean.grid(row=1, column=2, ipady=4, ipadx=16)

        button_backspace = Button(self.window, text="<-", command=self.other.backspace, bg="light gray", font=self.font_size)
        button_backspace.grid(row=5, column=0, ipady=6, ipadx=13)

        button_add = Button(self.window, text="+", command=self.calc.add, bg="light gray", font=self.font_size)
        button_add.grid(row=4, column=3, ipady=4, ipadx=20)

        button_subtraction = Button(self.window, text="-", command=self.calc.subtraction, bg="light gray", font=self.font_size)
        button_subtraction.grid(row=3, column=3,ipady= 5, ipadx=24)

        button_multiplication = Button(self.window, text="x", command=self.calc.multiplication, bg="light gray", font=self.font_size)
        button_multiplication.grid(row=2, column=3, ipady=4, ipadx=22)

        button_division = Button(self.window, text="/", command=self.calc.division, bg="light gray", font=self.font_size)
        button_division.grid(row=1, column=3,ipady=4, ipadx=25)

        button_equal = Button(self.window, text="=", command=self.calc.equal, bg="light gray", font=self.font_size)
        button_equal.grid(row=5, column=3, ipady=6, ipadx=20)

        button_sqr = Button(self.window, text="sqr", command=self.calc.sqr, bg="light gray", font=self.font_size)
        button_sqr.grid(row=1, column=1, ipady=4, ipadx=6)

        button_power = Button(self.window, text="x^2", command=self.calc.power, bg="light gray", font=self.font_size)
        button_power.grid(row=1, column=0, ipady=4, ipadx=5)

        self.window.bind("<+>", self.calc.add_bind)
        self.window.bind("<minus>", self.calc.sub_bind)
        self.window.bind("<*>", self.calc.multi_bind)
        self.window.bind("</>", self.calc.div_bind)
        self.window.bind("<=>", self.calc.equal_bind)


def main():
    run = Interface()
    run.buttons()
    run.window.mainloop()


if __name__ == '__main__':
    main()
