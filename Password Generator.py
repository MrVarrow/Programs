from tkinter import *
import pyperclip
import random
import string
import secrets


class Generator:
    window = Tk()

    board = Entry(window, font=('Arial', 14), bg='light gray')
    board.grid(row=6, sticky=W, padx=70)

    def __init__(self):
        self.window.title('Password generator')
        self.window.geometry('450x600')
        self.window.configure(bg='dimgray')

        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_characters = string.punctuation
        self.all_chars = self.letters + self.digits + self.special_characters

        self.option_type = ['Only letters', 'Letters,numbers',
                            "Letters,numbers,special characters"]
        self.var_type = StringVar()
        self.var_type.set("Select password type")

        self.options_len = ['6', '7', '8', '9', '10', '11', '12']
        self.var_len = StringVar()
        self.var_len.set("Select password length")

    def copy_password(self):
        to_copy = self.board.get()
        pyperclip.copy(to_copy)

    def get_value_type(self):
        val_type = self.var_type.get()
        return val_type

    def get_value_len(self):
        val_len = self.var_len.get()
        return val_len

    def create_password(self):
        self.password = ''
        final_var_type = self.get_value_type()
        final_var_len = int(self.get_value_len())
        self.board.delete(0, END)

        if final_var_type == 'Only letters':
            for i in range(final_var_len):
                self.password += ''.join(secrets.choice(self.letters))
            self.board.insert(0, self.password)


        elif final_var_type == 'Letters,numbers':
            for i in range(final_var_len):
                self.password += ''.join(secrets.choice(self.letters + self.digits))
            self.board.insert(0, self.password)


        elif final_var_type == 'Letters,numbers,special characters':
            for i in range(final_var_len):
                self.password += ''.join(secrets.choice(self.all_chars))
            self.board.insert(0, self.password)

    def layout_create(self):
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=0)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=0)
        self.window.rowconfigure(5, weight=2)
        self.window.rowconfigure(6, weight=1)
        self.window.rowconfigure(7, weight=1)

        choose_len = Label(self.window, text='Choose password length:', bg='gray', font=('Arial',14),padx= 10,pady=10)
        choose_len.grid(row=1)

        choose_type = Label(self.window, text='Choose password type:', bg='gray', font=('Arial',14),padx= 17,pady=10)
        choose_type.grid(row=3)

        self.select_type = OptionMenu(self.window, self.var_type, *self.option_type)
        self.select_type.grid(row=4)

        self.select_len = OptionMenu(self.window, self.var_len, *self.options_len)
        self.select_len.grid(row=2)

        button_generate = Button(self.window, text='Generate password', command=self.create_password, font=(
        "Arial", 14), bg='powder blue')
        button_generate.grid(row=5)

        button_exit = Button(self.window, text='Exit', command=self.window.destroy, font=('Arial',16), bg='powder blue')
        button_exit.grid(row=7, sticky=E, padx=20)

        button_copy = Button(self.window, text='Copy', command=self.copy_password, font=('Arial',12), bg='powder blue')
        button_copy.grid(row=6, sticky=E, padx=50)

        welcome = Label(self.window, text="Welcome to password generator!", font=('Arial', 18), bg='lightblue2', padx=50,
                        pady=30)
        welcome.grid(row=0)

def main():
    run = Generator()
    run.layout_create()
    mainloop()

if __name__ == '__main__':
    main()








