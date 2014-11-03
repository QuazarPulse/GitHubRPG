##RPG Games by Hugo and Hugo

##Fonction principale + ouverture
import tkinter

class mainMenu_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='ES')

if __name__ == "__main__":
    app = mainMenu_tk(None)
    app.title('RPG Games')
    app.mainloop()
    
