from tkinter import *
import pandas as pd
from pandastable import Table, config


class AddressBook:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x610")
        self.root.resizable(False, False)
        self.root.title("Address book")
        self.df = pd.DataFrame(columns=['name', 'last name', 'phone', 'date of birth'])

    def layout(self):
        top_frame = Frame(self.root, bg="gray")
        self.center = Frame(self.root, bg="light gray")
        bottom = Frame(self.root, bg="red")

        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=2)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky=EW)
        self.center.grid(row=1, sticky=NSEW)
        bottom.grid(row=2, sticky=EW)

        heading = Label(top_frame, text="Your address book:", font=("Arial", 20), bg="gray")
        heading.grid(padx=270, pady=20)

        add_new_button = Button(bottom, text="Add new", bg="gray", font=("Arial", 15), command=self.add_new)
        add_new_button.grid(row=0, column=0, pady=10, padx=120, ipadx=5)

        delete_button = Button(bottom, text="Delete", bg="gray", font=("Arial", 15), command=self.delete)
        delete_button.grid(row=0, column=4, pady=10, padx=120, ipadx=5)

        exit_button = Button(bottom, text="Exit", bg="gray", font=("Arial", 15), command=self.root.destroy)
        exit_button.grid(row=0, column=5, pady=10, padx=50, ipadx=10)

        self.load_excel()
        self.pt = Table(self.center, dataframe=self.df, rows=1, cols=4, width=1000, maxcellwidth=1500)
        self.pt.show()

    def load_excel(self):
        self.df_old = pd.read_excel('output.xlsx')
        print(self.df_old)
        self.df = self.df_old

    def add_new(self):
        self.add_root = Toplevel(self.root)
        self.add_root.title("Add new")
        self.add_root.geometry("400x200")
        self.add_root.resizable(False, False)

        self.add_root.grid_columnconfigure(0, weight=1)
        self.add_root.grid_columnconfigure(1, weight=1)

        add_lbl = Label(self.add_root, text="Add new to the list:", font=("Arial", 15))
        add_lbl.grid(row=0, column=0, columnspan=2)

        name_lbl = Label(self.add_root, text="Name: ", font=("Arial", 15))
        name_lbl.grid(row=1, column=0, padx=20)

        last_name_lbl = Label(self.add_root, text="Last name: ", font=("Arial", 15))
        last_name_lbl.grid(row=2, column=0, padx=20)

        phone_lbl = Label(self.add_root, text="Phone number: ", font=("Arial", 15))
        phone_lbl.grid(row=3, column=0, padx=20)

        age_lbl = Label(self.add_root, text="Date of birth: ", font=("Arial", 15))
        age_lbl.grid(row=4, column=0, padx=20)

        self.name_entry = Entry(self.add_root, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, padx=20)

        self.last_name_entry = Entry(self.add_root, font=("Arial", 12))
        self.last_name_entry.grid(row=2, column=1, padx=20)

        self.phone_entry = Entry(self.add_root, font=("Arial", 12))
        self.phone_entry.grid(row=3, column=1, padx=20)

        self.age_entry = Entry(self.add_root, font=("Arial", 12))
        self.age_entry.grid(row=4, column=1, padx=20)

        ok_button = Button(self.add_root, text="OK", bg="gray", font=("Arial", 12), command=self.ok_button)
        ok_button.grid(row=5, column=1, pady=10, sticky=E, padx=20, ipadx=20)

        cancel_button = Button(self.add_root, text="Cancel", bg="gray", font=("Arial", 12), command=self.add_root.destroy)
        cancel_button.grid(row=5, column=0, pady=10, sticky=W, padx=20)

    def delete(self):
        self.delete_root = Toplevel(self.root)
        self.delete_root.title("Delete")
        self.delete_root.geometry("400x200")
        self.delete_root.resizable(False, False)

        self.delete_root.grid_columnconfigure(0, weight=1)
        self.delete_root.grid_columnconfigure(1, weight=1)

        self.entry_num = Entry(self.delete_root)
        self.entry_num.grid()

        submit_button = Button(self.delete_root, text="Submit", bg="gray", font=("Arial", 12), command=self.submit_del)
        submit_button.grid()

    def submit_del(self):
        number = int(self.entry_num.get())
        self.df = self.df.drop(self.df.index[number - 1])
        self.page()
        self.df.to_excel('output.xlsx', index=False)
        self.delete_root.destroy()

    def ok_button(self):
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        phone = self.phone_entry.get()
        date_of_birth = self.age_entry.get()
        data = [name, last_name, phone, date_of_birth]
        self.df.loc[len(self.df.index)] = data
        self.df.to_excel('output.xlsx', index=False)
        self.page()
        self.add_root.destroy()

    def page(self):
        self.pt = Table(self.center, dataframe=self.df, rows=20, cols=4, width=1000, maxcellwidth=1500)
        self.pt.show()
        self.pt.redraw()
        options = {'font': 'Arial', 'fontsize': 12 }
        config.apply_options(options, self.pt)


def main():
    run = AddressBook()
    run.layout()
    mainloop()


if __name__ == "__main__":
    main()
