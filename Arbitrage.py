from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt 

window = tk.Tk()
window.title("Arbitrage")
window.geometry("900x450")
TAB_CONTROL = ttk.Notebook(window)
Tab1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(Tab1, text='Convert')
Tab2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(Tab2, text='Currencies')
Tab3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(Tab3, text='Graph')
TAB_CONTROL.pack(expand =1, fill = "both")

speech3 = Label(Tab3, text = "Press the button to update the graph", bg = "black",fg = "white")
speech3.pack()
speech2 = Label(Tab2, text = "Select a currency from the drop-down box to see the exchange rates", bg = "black",fg = "white")
speech2.pack()
speech = Label(Tab1, text ="Select the currency you wish to convert on the left and then select the currency you wish to convert to on the right.", bg = "black",fg = "white")
speech.pack()
def show():
    values = [i for i in range(1,100)]
    y = random.randint(0,98)
    x = random.randint(0,1)
    value = int(textbox.get())
    if clicked.get() != clicked2.get():
        if x == 1:
            value = value + (value*values[y]/100)
        else:
            value = value - (value*values[y]/100)
    myLabel["text"] = str(round(value,2))
def show2():
    values = [random.randint(100,200) for _ in range(6)]


    if clicked3.get() == "USD":
        words = ["EUR","GBP","CND","JPY","TTD","JMD"]
    elif clicked3.get() == "EUR":
        words = ["USD","GBP","CND","JPY","TTD","JMD"]
    elif clicked3.get() == "GBP":
        words = ["USD","EUR","CND","JPY","TTD","JMD"]
    elif clicked3.get() == "CND":
        words = ["USD","EUR","GBP","JPY","TTD","JMD"]
    elif clicked3.get() == "JPY":
        words = ["USD","EUR","GBP","CND","TTD","JMD"]
    elif clicked3.get() == "TTD":
        words = ["USD","EUR","GBP","CND","JPY","JMD"]
    else:
        words = ["USD","EUR","GBP","CND","JPY","TTD"]
    Label1["text"] = words[0] + " "+ str(values[0])
    Label2["text"] = words[1] + " "+ str(values[1])
    Label3["text"] = words[2] + " "+ str(values[2])
    Label4["text"] = words[3] + " "+ str(values[3])
    Label5["text"] = words[4] + " "+ str(values[4])
    Label6["text"] = words[5] + " "+ str(values[5])

    
    
    
    
clicked = StringVar()
clicked.set("JMD")
clicked2 = StringVar()
clicked2.set("USD")
clicked3 = StringVar()
clicked3.set("JMD")
drop = OptionMenu(Tab1, clicked, "USD","EUR","GBP","CND","JPY","TTD","JMD")
drop.pack()
textbox = Entry(Tab1, width= 20, bg = "white")
textbox.pack()
drop2 = OptionMenu(Tab1, clicked2, "USD","EUR","GBP","CND","JPY","TTD","JMD")
drop2.pack()
drop3 = OptionMenu(Tab2, clicked3, "USD","EUR","GBP","CND","JPY","TTD","JMD")
drop3.pack()
button = Button(Tab1, text = "Convert", command = show).pack()
button2 = Button(Tab2, text = "Update", command = show2).pack()

myLabel = Label(Tab1,text = "")
myLabel.pack()
Label1 = Label(Tab2, text = "")
Label2 = Label(Tab2, text = "")
Label3 = Label(Tab2, text = "")
Label4 = Label(Tab2, text = "")
Label5 = Label(Tab2, text = "")
Label6 = Label(Tab2, text = "")
Label1.pack()
Label2.pack()
Label3.pack()
Label4.pack()
Label5.pack()
Label6.pack()
window.mainloop()
