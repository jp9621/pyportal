import requests
import json
import time
from tkinter import *
import pandas as pd
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

def targetAdd(target):
    targets.append(float(target));


# Defining the Window
root = Tk()
root.title("JAPAFX")
root.configure(bg='#36393E')
targets = [];

# Creating some default appearance related settings for window elements
padx = 5
pady = 5
bg = '#4A4D52'
bgi = '#F4C73F'
fg = '#E1F174'
font = ('Arial', 14)
lightblack = '#5D636C'
gray = '#DBE5E3'

# Defining Label
pairLabel = Label(root, text="Pair: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
stopLabel = Label(root, text="Stop: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
tpLabel = Label(root, text="TP1: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)


# Defining Input
pairInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
stopInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
tpInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
tpOrderButton = Button(root, text="+", command=lambda: targetAdd(tpInput.get()))



# Gridding Widgets
pairLabel.grid(row=0, column=0)
pairInput.grid(row=0, column=1)
stopLabel.grid(row=1, column=0)
stopInput.grid(row=1, column=1)
tpLabel.grid(row=2, column=0)
tpInput.grid(row=2, column=1)
tpOrderButton.grid(row=2, column=3)


# Declaring and Gridding Calculate Button
orderButton = Button(root, text="Order", fg=fg, bg=bg,font=font)
orderButton.grid(row=3, column=0)

root.mainloop() 