import tkinter


class Main:
    def __init__(self):
        self.Window()
    
    def Window(self):
        tkinter.Tk().wm_withdraw()

        win = tkinter.Toplevel()
        win.geometry("500x650+400+50")
        
        win.protocol("WM_DELETE_WINDOW", exit)
        win.mainloop()

Main()
