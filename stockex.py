import tkinter
from wallstreet import Stock, Call, Put
firstclick=True
class StockApp_Tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        self.entry = tkinter.Entry(self,text="Enter the company")
        self.entry.insert(0,"Enter the Company")
        self.entry.grid(column=0,row=0,sticky='EWNS')
        button= tkinter.Button(self, text=u"Check Stock",command=self.OnButtonClick)
        button.grid(column=1,row=0,sticky='EWNS')
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,anchor="center",fg="white",bg="#35ad8f",textvariable=self.labelVariable)
        label.grid(column=0,row=1,rowspan=2,columnspan=2,sticky='EWNS')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=2)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry.bind('<FocusIn>',self.on_entry_click)
        
        
    def OnButtonClick(self):
        user=(self.entry.get())
        s=Stock(user)
        self.labelVariable.set("Hello the current price is " + str(s.price)+"\n \n" + " The change in stock value was " + str(s.change) + " since " + str(s.last_trade))
      


    def OnPressEnter(self,event):
        self.labelVariable.set("You pressed Return")
        
    def on_entry_click(self,event):
        global firstclick
        if firstclick:
            firstclick = False
            self.entry.delete(0, "end")
if __name__ == "__main__":
    app=StockApp_Tk(None)
    app.title('Stock Exchange')
    app.mainloop()
    


'''print("The current price is", s.price)
print("")
print("")
print("The change in stock value was ", s.change, " since ", s.last_trade)
'''
