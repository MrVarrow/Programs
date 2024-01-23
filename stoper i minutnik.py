import time
from tkinter import *
from datetime import date
from tkinter import messagebox
#zablokowac start w timer

#zablokowac przycisk start w stopwatch

class App:
    window = Tk()

    def __init__(self):
        self.window.title('Clock')
        self.window.geometry('470x300')
        self.window.resizable(False, False)
        self.window.configure(bg='light gray')
        self.sw_counter = 1
        self.t_counter = 1

    def layout(self):
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=2)
        self.window.rowconfigure(2, weight=1)
        obj = Stopwatch()
        timer = Timer()

        self.clock_lbl = Label(text='', font=('Arial', 15))
        self.clock_lbl.grid(row=0, column=1, ipadx=65, ipady=20, padx=10, pady=10)
        self.clock_update()

        self.date_lbl = Label(text='', font=('Arial', 15))
        self.date_lbl.grid(row=0, column=0, ipadx=55, ipady=20, padx=10, pady=10)
        self.date_update()

        stopwatch_button = Button(text='Stopwatch', command=obj.stopwatch_window, font=('Arial', 15))
        stopwatch_button.grid(row=1, column=0, ipady=5, ipadx=20, pady=20)

        timer_button = Button(text='Timer', command=timer.timer_window, font=('Arial', 15))
        timer_button.grid(row=1, column=1, ipady=5, ipadx=45, pady=20)

        exit_button = Button(text="Exit", command=self.window.destroy, font=('Arial', 15))
        exit_button.grid(row=2, column=1, ipady=5, ipadx=10, sticky=SE, padx=10, pady=10)

    def clock_update(self):
        actual_time = time.strftime("%H:%M:%S")
        self.clock_lbl.configure(text=actual_time)
        self.window.after(1000, self.clock_update)

    def date_update(self):
        actual_date = str(date.today())
        self.date_lbl.configure(text=actual_date)
        self.window.after(1000, self.date_update)

    def time_convert(self, seconds):
        minutes = seconds // 60
        seconds = float(seconds % 60)
        hours = minutes // 60
        minutes = minutes % 60
        seconds = round(seconds)
        return "{0}:{1}:{2}".format(int(hours), int(minutes), seconds)


class Stopwatch(App):

    def stopwatch_window(self):
        if self.sw_counter < 2:
            self.stopwatch_win = Toplevel(self.window)
            self.stopwatch_win.geometry('300x300')
            self.stopwatch_win.title('Stopwatch')
            self.stopwatch_win.configure(bg='light gray')
            self.stopwatch_win.resizable(False, False)

            sw_lbl = Label(self.stopwatch_win, text="Stopwatch:", font=('Arial', 15))
            sw_lbl.grid(row=0, column=0, columnspan=2, pady=10, padx=75, ipadx=20, ipady=5)

            self.sw_start_b = Button(self.stopwatch_win, text="Start", command=self.sw_start, font=('Arial', 15))
            self.sw_start_b.grid(row=3, column=0, ipady=5, ipadx=13, padx=20, sticky=W)

            self.sw_time_lbl = Label(self.stopwatch_win, text="00:00:00", font=('Arial', 15), width=10)
            self.sw_time_lbl.grid(row=1, column=0, columnspan=2, pady=10, padx=75, ipadx=20, ipady=5)

            self.final_time_lbl = Label(self.stopwatch_win, text='', font=('Arial', 15), width=10)
            self.final_time_lbl.grid(row=2, column=0, columnspan=2, pady=10, padx=75, ipadx=20, ipady=5)

            self.sw_stop_b = Button(self.stopwatch_win, text="Stop", command=self.sw_stop, font=('Arial', 15))
            self.sw_stop_b.grid(row=3, column=1, ipady=5, ipadx=15, padx=20, sticky=E)

            sw_exit = Button(self.stopwatch_win, text="Exit", command=self.sw_exit, font=('Arial', 10))
            sw_exit.grid(row=4, column=1, ipadx=10, padx=10, pady=35, sticky=SE)

            self.sw_counter += 1

            self.stopwatch_win.protocol("WM_DELETE_WINDOW", self.when_closing)
        else:
            messagebox.showinfo("Error", "You can't open another window of the same type")

    def sw_start(self):
        self.start_time = time.time()
        self.stopwatch_update()
        self.sw_start_b.configure(state=DISABLED)

    def sw_stop(self):
        final_time = self.sw_time_lbl.cget("text")
        self.final_time_lbl.configure(text=final_time)
        self.stopwatch_win.after_cancel(self.sw_update)
        self.sw_time_lbl.configure(text="00:00:00")
        self.sw_start_b.configure(state=ACTIVE)

    def stopwatch_update(self):
        time_elapsed = time.time() - self.start_time
        convert = self.time_convert(time_elapsed)
        self.sw_time_lbl.configure(text=convert)
        self.sw_update = self.stopwatch_win.after(1000, self.stopwatch_update)

    def sw_exit(self):
        self.stopwatch_win.destroy()
        self.sw_counter = 1

    def when_closing(self):
        self.stopwatch_win.destroy()
        self.sw_counter = 1


class Timer(App):

    def timer_window(self):
        if self.t_counter < 2:
            self.timer_win = Toplevel(self.window)
            self.timer_win.geometry('300x300')
            self.timer_win.title('Timer')
            self.timer_win.configure(bg='light gray')
            self.timer_win.resizable(False, False)

            self.timer_win.columnconfigure(3, weight=1)

            t_lbl = Label(self.timer_win, text="Timer", font=('Arial', 15))
            t_lbl.grid(row=0, column=0, columnspan=4, ipadx=40, ipady=5, padx=50, pady=10)

            self.t_start_b = Button(self.timer_win, text="Start", command=self.t_start, font=('Arial', 15))
            self.t_start_b.grid(row=5, column=0, columnspan=2, ipadx=15, ipady=5)

            self.t_time_lbl = Label(self.timer_win, text="00:00:00", font=('Arial', 15), width=10)
            self.t_time_lbl.grid(row=3, column=0, columnspan=4, ipadx=40, ipady=5, padx=70, pady=15)

            self.timeup_lbl = Label(self.timer_win, text="", font=('Arial', 15), width=10, bg='light gray')
            self.timeup_lbl.grid(row=4, column=0, columnspan=4, ipadx=40, padx=70, pady=5)

            self.t_stop_b = Button(self.timer_win, text="Stop", command=self.t_stop, font=('Arial', 15))
            self.t_stop_b.grid(row=5, column=1, columnspan=2, ipadx=18, ipady=5)

            t_exit = Button(self.timer_win, text="Exit", command=self.t_exit, font=('Arial', 10))
            t_exit.grid(row=6, column=2, columnspan=2, pady=5, padx=5, ipady=5, ipadx=10, sticky=SE)

            self.h_box = Spinbox(self.timer_win, from_=0, to=23, wrap=True, font=('Arial', 15), width=3)
            self.h_box.grid(row=1, column=0, sticky=W, padx=25)

            self.min_box = Spinbox(self.timer_win, from_=0, to=59, wrap=True, font=('Arial', 15), width=3)
            self.min_box.grid(row=1, column=1, sticky=W, padx=20)

            self.sec_box = Spinbox(self.timer_win, from_=0, to=59, wrap=True, font=('Arial', 15), width=3)
            self.sec_box.grid(row=1, column=2, sticky=W, padx=15)

            Label(self.timer_win, text='h', font=('Arial', 15), bg='light gray').grid(row=1, column=0, sticky=E)
            Label(self.timer_win, text='m', font=('Arial', 15), bg='light gray').grid(row=1, column=1, sticky=E)
            Label(self.timer_win, text='s', font=('Arial', 15), bg='light gray').grid(row=1, column=2, sticky=E)

            self.t_counter += 1

            self.timer_win.protocol("WM_DELETE_WINDOW", self.t_when_closing)
        else:
            messagebox.showinfo("Error", "You can't open another window of the same type")

    def t_display(self):
        t_converted = self.time_convert(self.sec)
        if self.sec > 0:
            self.t_time_lbl.configure(text=t_converted)
            self.t_refresh = self.timer_win.after(1000, self.t_display)
            self.sec = self.sec - 1
        elif self.sec == 0:
            self.t_time_lbl.configure(text="00:00:00")
            self.timeup_lbl.configure(text="Time is up!")
            self.t_start_b.configure(state=ACTIVE)

    def t_start(self):
        h = self.h_box.get()
        m = self.min_box.get()
        s = self.sec_box.get()
        self.sec = int(s) + (int(m) * 60) + (int(h) * 3600)
        self.t_display()
        self.t_start_b.configure(state=DISABLED)

    def t_stop(self):
        self.timer_win.after_cancel(self.t_refresh)
        self.t_time_lbl.configure(text="00:00:00")
        self.t_start_b.configure(state=ACTIVE)

    def t_exit(self):
        self.timer_win.destroy()
        self.t_counter = 1

    def t_when_closing(self):
        self.timer_win.destroy()
        self.t_counter = 1


def main():
    run = App()
    run.layout()
    mainloop()


if __name__ == '__main__':
    main()
