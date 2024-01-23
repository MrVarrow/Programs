import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Interface:
    window = Tk()

    def __init__(self):
        self.window.title("Notepad")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(bg="light gray")
        self.notes = []
        self.recent_notes = []

    def layout(self):
        top_frame = Frame(self.window, bg='gray')
        center = Frame(self.window, bg="light gray")
        recent = Frame(self.window, bg="light gray")
        bottom = Frame(self.window, bg="light gray")

        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=2)
        self.window.grid_columnconfigure(0, weight=1)

        recent.grid(row=2, sticky=EW)
        top_frame.grid(row=0, sticky=EW)
        center.grid(row=1, sticky=EW)
        bottom.grid(row=3, sticky=EW)

        top_lbl = Label(top_frame, text="Your notes", font=("Arial", 25), bg="gray")
        top_lbl.grid(padx=170)

        choose_lbl = Label(center, text="Choose your note to open:", font=("Arial", 25), bg="light gray")
        choose_lbl.grid(column=0, row=0, pady=20, padx=60)

        choose_button = Button(center, text="Open", font=("Arial", 15), bg="gray", command=self.open_file)
        choose_button.grid(column=0, row=1, sticky=E, padx=50, ipadx=25)

        self.notes_list = ttk.Combobox(center, values=self.notes, font=("Arial", 15))
        self.notes_list.set("Pick an option")
        self.notes_list.grid(column=0, row=1, sticky=W, padx=50, pady=30)
        self.combobox_update()

        recent_lbl = Label(recent, text="Your last created notes:", font=("Arial", 25), bg="light gray")
        recent_lbl.grid(row=0, column=0, columnspan=5, padx=80, pady=10)

        self.recent1 = Button(recent, text="Empty", font=("Arial", 12), bg="gray", width=8, height=5, wraplength=75,
                              state=DISABLED)
        self.recent1.grid(row=1, column=0, pady=30)

        self.recent2 = Button(recent, text="Empty", font=("Arial", 12), bg="gray", width=8, height=5, wraplength=75,
                              state=DISABLED)
        self.recent2.grid(row=1, column=1, pady=30)

        self.recent3 = Button(recent, text="Empty", font=("Arial", 12), bg="gray", width=8, height=5, wraplength=75,
                              state=DISABLED)
        self.recent3.grid(row=1, column=2, pady=30)

        self.recent4 = Button(recent, text="Empty", font=("Arial", 12), bg="gray", width=8, height=5, wraplength=75,
                              state=DISABLED)
        self.recent4.grid(row=1, column=3, pady=30)

        self.recent5 = Button(recent, text="Empty", font=("Arial", 12), bg="gray", width=8, height=5, wraplength=75,
                              state=DISABLED)
        self.recent5.grid(row=1, column=4, pady=30)

        new_note = Button(bottom, text="Add new note", command=self.title, font=("Arial", 15), bg="gray")
        new_note.grid(row=0, column=1, sticky=E, padx=215, pady=10)

        delete_note = Button(bottom, text="Delete note", font=("Arial", 15), bg="gray", command=self.delete)
        delete_note.grid(row=0, column=0, padx=10, pady=10)

        self.load_files()
    def combobox_update(self):
        self.notes_list.configure(values=self.notes)
        self.window.after(1000, self.combobox_update)

    def delete(self):
        picked_file_d = "{}.txt".format(self.notes_list.get())
        os.remove(picked_file_d)
        self.notes.remove(self.notes_list.get())

    def title(self):
        title_win = Toplevel(self.window)
        title_win.title("Enter Title")
        title_win.resizable(False, False)
        title_win.geometry("300x150")

        title_lbl = Label(title_win, text="Please enter title of your note:", font=("Arial", 12))
        title_lbl.grid(row=0, padx=50, pady=15)

        self.title_entry = Entry(title_win, font=("Arial", 12))
        self.title_entry.grid(row=1, pady=5)

        self.ok_button = Button(title_win, text='OK', command=self.get_title, font=("Arial", 15), bg="gray")
        self.ok_button.grid(row=2, padx=100, ipadx=20, pady=15)

    def get_title(self):
        self.new_title = self.title_entry.get()
        if any(element == self.new_title for element in self.notes):
            messagebox.showinfo(title="Error", message="File with that name already exists")
        else:
            self.notes.append(self.new_title)
            self.callback()
            new_file = open("{}.txt".format(self.new_title), "w+")
            new_file.close()
            self.title_entry.delete(0, END)

    def open_file(self):
        picked_file = "{}.txt".format(self.notes_list.get())
        os.startfile(picked_file)

    def callback(self):
        if len(self.notes) == 1:
            self.recent1.configure(text=self.notes[-1], state=ACTIVE)
            self.recent1.configure(command=lambda m=self.recent1.cget('text'): self.which_button(m))
            self.recent2.configure(text="Empty", state=DISABLED)
            self.recent3.configure(text="Empty", state=DISABLED)
            self.recent4.configure(text="Empty", state=DISABLED)
            self.recent5.configure(text="Empty", state=DISABLED)
        elif len(self.notes) == 2:
            self.recent2.configure(text=self.notes[-1], state=ACTIVE)
            self.recent2.configure(command=lambda m=self.recent2.cget('text'): self.which_button(m))
            self.recent3.configure(text="Empty", state=DISABLED)
            self.recent4.configure(text="Empty", state=DISABLED)
            self.recent5.configure(text="Empty", state=DISABLED)
            self.recent1.configure(text=self.notes[-2], state=ACTIVE)
        elif len(self.notes) == 3:
            self.recent3.configure(text=self.notes[-1], state=ACTIVE)
            self.recent3.configure(command=lambda m=self.recent3.cget('text'): self.which_button(m))
            self.recent4.configure(text="Empty", state=DISABLED)
            self.recent5.configure(text="Empty", state=DISABLED)
            self.recent1.configure(text=self.notes[-3], state=ACTIVE)
            self.recent2.configure(text=self.notes[-2], state=ACTIVE)
        elif len(self.notes) == 4:
            self.recent4.configure(text=self.notes[-1], state=ACTIVE)
            self.recent4.configure(command=lambda m=self.recent4.cget('text'): self.which_button(m))
            self.recent5.configure(text="Empty", state=DISABLED)
            self.recent1.configure(text=self.notes[-4], state=ACTIVE)
            self.recent2.configure(text=self.notes[-3], state=ACTIVE)
            self.recent3.configure(text=self.notes[-2], state=ACTIVE)
        elif len(self.notes) == 5:
            self.recent5.configure(text=self.notes[-1], state=ACTIVE)
            self.recent5.configure(command=lambda m=self.recent5.cget('text'): self.which_button(m))
            self.recent1.configure(text=self.notes[-5], state=ACTIVE)
            self.recent2.configure(text=self.notes[-4], state=ACTIVE)
            self.recent3.configure(text=self.notes[-3], state=ACTIVE)
            self.recent4.configure(text=self.notes[-2], state=ACTIVE)
        elif len(self.notes) > 5:
            self.recent5.configure(text=self.notes[-1], state=ACTIVE)
            self.recent1.configure(text=self.notes[-5], state=ACTIVE)
            self.recent2.configure(text=self.notes[-4], state=ACTIVE)
            self.recent3.configure(text=self.notes[-3], state=ACTIVE)
            self.recent4.configure(text=self.notes[-2], state=ACTIVE)
            self.recent1.configure(command=lambda m=self.recent1.cget('text'): self.which_button(m))
            self.recent2.configure(command=lambda m=self.recent2.cget('text'): self.which_button(m))
            self.recent3.configure(command=lambda m=self.recent3.cget('text'): self.which_button(m))
            self.recent4.configure(command=lambda m=self.recent4.cget('text'): self.which_button(m))
            self.recent5.configure(command=lambda m=self.recent5.cget('text'): self.which_button(m))
        else:
            pass

    def which_button(self, y):
        recent_file = "{}.txt".format(y)
        try:
            os.startfile(recent_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Info", message="File is already deleted, removing shortcut")
            if y == self.recent1.cget('text'):
                self.recent1.configure(text="Empty", state=DISABLED)
            elif y == self.recent2.cget('text'):
                self.recent2.configure(text="Empty", state=DISABLED)
            elif y == self.recent3.cget('text'):
                self.recent3.configure(text="Empty", state=DISABLED)
            elif y == self.recent4.cget('text'):
                self.recent4.configure(text="Empty", state=DISABLED)
            elif y == self.recent5.cget('text'):
                self.recent5.configure(text="Empty", state=DISABLED)
            self.callback()

    def load_files(self):
        for txt in os.listdir():
            if txt.endswith(".txt"):
                txt = txt[:-4]
                self.notes.append(txt)
                self.callback()
                print(txt)


def main():
    run = Interface()
    run.layout()
    mainloop()


if __name__ == "__main__":
    main()
