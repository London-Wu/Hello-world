from tkinter import *

class Application(Frame):
    def say(self):
        print('hello,this is the first program written by tkinter!')

    def window(self):
        self.QUIT=Button(self,text='QUIT',fg='red',bg='blue',command=self.quit)
        #self.QUIT = Button(self)
        #self.QUIT["text"] = "QUIT"
        #self.QUIT["fg"]   = "red"
        #self.QUIT["command"] =  self.quit
        self.QUIT.pack(side='left')
        print(self.QUIT.config())#{'relief': ('relief', 'relief', 'Relief', 'raised', 'groove')}

        self.say=Button(self,text='hello!',command=self.say)
        #self.hi_there["text"] = "Hello",
        #self.hi_there["command"] = self.say_hi
        self.say.pack(side='left')

    def __init__(self,master):
        super().__init__()
        self.pack()
        self.window()
root=Tk()
app=Application(root)
app.mainloop()
root.destroy()
