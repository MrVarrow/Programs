from tkinter import *


class Layout:
    window = Tk()
    entry_things = Entry(window, font=('Arial', 15))
    entry_things.grid(row=2, column=1, columnspan=2, sticky=N, ipadx=50)

    def __init__(self):
        self.window.title('To do list')
        self.window.geometry('1000x700')
        self.window.resizable(False, False)
        self.window.configure(bg='light gray')
        self.create = Create()

    def interface(self):
        self.window.rowconfigure(4, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)

        lbl_welcome = Label(self.window, text="Welcome!", bg='gray', font=('Arial', 30))
        lbl_welcome.grid(row=0, column=1, columnspan=2, ipadx=200, ipady=25, pady=20, sticky=N)

        lbl_enter = Label(self.window, text="Enter things to do:", font=('Arial', 15), bg='light gray')
        lbl_enter.grid(row=1, column=1, columnspan=2, sticky=N, pady= 10)

        submit_button = Button(self.window, text="Submit", command=self.create.submit, font=('Arial', 15))
        submit_button.grid(row=1, column=2, rowspan=2, padx=20, sticky=E, ipadx=15)

        lbl_things = Label(self.window, text="Yours things to do:", font=('Arial', 30), bg='gray')
        lbl_things.grid(row=3, column=1, columnspan=2, ipadx=130, ipady=25, pady=20, sticky=N)

        button_clear = Button(self.window, text="Clear list", command=self.create.clear_list, font=('Arial', 15))
        button_clear.grid(row=8, column=0, ipadx=30, padx=10, pady=10, sticky=S)

        button_exit = Button(self.window, text="Exit", command=self.window.destroy, font=('Arial', 15))
        button_exit.grid(row=8, column=3, ipadx=50, padx=10, pady=10, sticky=S)

        button_delete_last = Button(self.window, text="Delete last task", command=self.create.delete_last, font=('Arial', 15))
        button_delete_last.grid(row=7, column=0, padx=10, pady=10, sticky=S)


class Create(Layout):

    def __init__(self):
        self.list = []

    def popup(self, text):
        popup = Toplevel(self.window)
        popup.geometry('300x155')
        popup.title('Error')
        popup.configure(bg='gray')

        message = Label(popup, text=text, font=('Arial', 14), bg='gray')
        message.grid(sticky=N, row=0, ipady=10,ipadx=5)

        accept_error = Button(popup, text="OK", command=popup.destroy, font=('Arial', 15), bg='light gray')
        accept_error.grid(sticky=S, pady=50, row=1, ipadx=30)

    def submit(self):
        file_txt = open('Thing to do.txt', 'r+')
        thing = self.entry_things.get()
        self.entry_things.delete(0, END)

        if len(self.list) <= 9:
            self.list.append(thing + '\n')
            file_txt.writelines(self.list)
            file_txt.close()
            self.add_checkbuttons()
        else:
            file_txt.close()
            self.popup("That's maxiumum number of tasks")

    def clear_list(self):
        file_txt = open('Thing to do.txt', 'r+')
        file_txt.truncate()
        self.remove_checbotton()
        self.list = []
        file_txt.close()

    def add_checkbuttons(self):
        length = len(self.list)

        if length == 1:
            self.c1 = Checkbutton(self.window, text=self.list[0], font=('Arial', 12))
            self.c1.grid(row=4, column=1, pady=10, padx=10, sticky=S)

        elif length == 2:
            self.c2 = Checkbutton(self.window, text=self.list[1], font=('Arial', 12))
            self.c2.grid(row=5, column=1, pady=10, padx=10, sticky=S)

        elif length == 3:
            self.c3 = Checkbutton(self.window, text=self.list[2], font=('Arial', 12))
            self.c3.grid(row=6, column=1, pady=10, padx=10, sticky=S)

        elif length == 4:
            self.c4 = Checkbutton(self.window, text=self.list[3], font=('Arial', 12))
            self.c4.grid(row=7, column=1, pady=10, padx=10, sticky=S)

        elif length == 5:
            self.c5 = Checkbutton(self.window, text=self.list[4], font=('Arial', 12))
            self.c5.grid(row=8, column=1, pady=10, padx=10, sticky=S)

        elif length == 6:
            self.c6 = Checkbutton(self.window, text=self.list[5], font=('Arial', 12))
            self.c6.grid(row=4, column=2, pady=10, padx=10, sticky=S)

        elif length == 7:
            self.c7 = Checkbutton(self.window, text=self.list[6], font=('Arial', 12))
            self.c7.grid(row=5, column=2, pady=10, padx=10, sticky=S)

        elif length == 8:
            self.c8 = Checkbutton(self.window, text=self.list[7], font=('Arial', 12))
            self.c8.grid(row=6, column=2, pady=10, padx=10, sticky=S)

        elif length == 9:
            self.c9 = Checkbutton(self.window, text=self.list[8], font=('Arial', 12))
            self.c9.grid(row=7, column=2, pady=10, padx=10, sticky=S)

        elif length == 10:
            self.c10 = Checkbutton(self.window, text=self.list[9], font=('Arial', 12))
            self.c10.grid(row=8, column=2, pady=10, padx=10, sticky=S)

    def remove_checbotton(self):
        self.c1.destroy()
        self.c2.destroy()
        self.c3.destroy()
        self.c4.destroy()
        self.c5.destroy()
        self.c6.destroy()
        self.c7.destroy()
        self.c8.destroy()
        self.c9.destroy()
        self.c10.destroy()

    def delete_last(self):
        if len(self.list) == 1:
            self.c1.destroy()
        elif len(self.list) == 2:
            self.c2.destroy()
        elif len(self.list) == 3:
            self.c3.destroy()
        elif len(self.list) == 4:
            self.c4.destroy()
        elif len(self.list) == 5:
            self.c5.destroy()
        elif len(self.list) == 6:
            self.c6.destroy()
        elif len(self.list) == 7:
            self.c7.destroy()
        elif len(self.list) == 8:
            self.c8.destroy()
        elif len(self.list) == 9:
            self.c9.destroy()
        elif len(self.list) == 10:
            self.c10.destroy()

        file_txt = open('Thing to do.txt', 'r+')
        self.list.pop()
        file_txt.truncate()
        file_txt.writelines(self.list)
        file_txt.close()


def main():
    file_txt = open('Thing to do.txt', 'r+')
    file_txt.truncate()
    file_txt.close()
    run = Layout()
    run.interface()
    mainloop()


if __name__ == '__main__':
    main()
