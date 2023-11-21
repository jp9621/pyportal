import requests
import json
import time
from tkinter import *
import pandas as pd
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

# Defining the Window
root = Tk()
root.title("")
root.configure(bg='#36393E')
targets = [];
targetsMet = [];
global maxrr
maxrr = 0.0

def price(pair):

    accountID = "101-001-26231816-001"
    access_token = "e498e28946731fbce23b09fc3bd50d09-cea6d8762bafefb600198e685cad980b"
    api = API(access_token=access_token)

    params = {
        "instruments": pair
    }

    r = pricing.PricingInfo(accountID=accountID, params=params)
    rv = api.request(r)

    # Extracting the price from the response
    price = rv['prices'][0]['bids'][0]['price'] 
    return price

def log(pair, maxrr):
    pairLabel2 = Label(root, text="Pair: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    sessionLabel = Label(root, text="Session: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    biastfLabel = Label(root, text="Bias TF: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    entrytfLabel = Label(root, text="Entry TF: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    conftfLabel = Label(root, text="Confirmation TF: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    conftypeLabel = Label(root, text="Confirmation Type: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    maxrrLabel = Label(root, text="Max RR: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    setuptypeLabel = Label(root, text="Setup Type: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    breakevenLabel = Label(root, text="Breakeven: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    TP1Label = Label(root, text="Target 1: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    TP2Label = Label(root, text="Target 2: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    runnersLabel = Label(root, text="Runners: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    commentLabel = Label(root, text="Comments: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    


    if (targetsMet[1]):
        be = True
    
    if (targetsMet[2]):
        tp1 = True
    elif (targetsMet[2] == None):
        tp1 = False
    else:
        tp1 = False
    
    if (targetsMet[3]):
        tp2 = True
    elif (targetsMet[3] == None):
        tp2 = False
    else:
        tp2 = False

    if (targetsMet[4]):
        rs = True
    elif (targetsMet[4] == None):
        rs = False
    else:
        rs = False

    pairOutput = Label(root, text=pair, fg=fg, bg=bg, font=font, padx=padx, pady=pady)

    sessionInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
    biastfInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
    entrytfInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
    conftfInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
    conftypeInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)

    maxxrrOutput = Label(root, text=maxrr, fg=fg, bg=bg, font=font, padx=padx, pady=pady)

    setuptypeInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)

    breakevenOutput = Label(root, text=be, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    TP1Output = Label(root, text=tp1, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    TP2Output = Label(root, text=tp2, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    runnersOutput = Label(root, text=rs, fg=fg, bg=bg, font=font, padx=padx, pady=pady)

    commentInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
    createFileButton = Button(root, text="Create File", command=lambda: createFile())

    pairLabel2.grid(row=8, column=0)
    sessionLabel.grid(row=9, column=0)
    biastfLabel.grid(row=10, column=0)
    entrytfLabel.grid(row=11, column=0)
    conftfLabel.grid(row=12, column=0)
    conftypeLabel.grid(row=13, column=0)
    maxrrLabel.grid(row=14, column=0)
    setuptypeLabel.grid(row=15, column=0)
    breakevenLabel.grid(row=16, column=0)
    TP1Label.grid(row=17, column=0)
    TP2Label.grid(row=18, column=0)
    runnersLabel.grid(row=19, column=0)
    commentLabel.grid(row=20, column=0)
    createFileButton.grid(row=21, column=0)

    pairOutput.grid(row=8, column=1)
    sessionInput.grid(row=9, column=1)
    biastfInput.grid(row=10, column=1)
    entrytfInput.grid(row=11, column=1)
    conftfInput.grid(row=12, column=1)
    conftypeInput.grid(row=13, column=1)
    maxxrrOutput.grid(row=14, column=1)
    setuptypeInput.grid(row=15, column=1)
    breakevenOutput.grid(row=16, column=1)
    TP1Output.grid(row=17, column=1)
    TP2Output.grid(row=18, column=1)
    runnersOutput.grid(row=19, column=1)
    commentInput.grid(row=20, column=1)
    

    def createFile():
        csv(pair, sessionInput.get(), biastfInput.get(), entrytfInput.get(), conftfInput.get(), conftypeInput.get(), maxrr, setuptypeInput.get(), be, tp1, tp2, rs, commentInput.get())
        fileStatusUpdate = Label(root, text="File Created", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
        fileStatusUpdate.grid(row=21, column=1)







def csv(currency_pair, session, biastf, entrytf, conftf, conftype, maxrr, setuptype, be, TP1, TP2, rs, comments):
    csvcontent = f'"{currency_pair}","{session}","{biastf}","{entrytf}","{conftf}","{conftype}",' \
                 f'"{maxrr}","{setuptype}","{be}","{TP1}","{TP2}","{rs}","{comments}"\n'

    try:
        with open("log.csv", "a") as outputFile:
            outputFile.write(csvcontent)
        print("CSV data appended successfully.")
    except Exception as e:
        print("Unable to open the CSV file:", str(e))


    
def track(currency_name, targets, stoploss, initial_price):
    # Get the price for the currency pair using price() function
    current_price = float(price(currency_name))

    targets_met = [False] * len(targets)

    # Check if targets are met
    for i in range(len(targets)):
        if (current_price >= targets[i] and stoploss < current_price) or (current_price <= targets[i] and stoploss > current_price):
            targets_met[i] = True

    return targets_met


def targetAdd(target):
    targets.append(float(target));

def order():
    pair = pairInput.get()
    stop = float(stopInput.get())
    targets.append(float(tpInput.get()))
    initialPrice = float(price(pair))

    pairtrackLabel = Label(root, text="PAIR: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    stoptrackLabel = Label(root, text="STOPLOSS: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    tptrackLabel = Label(root, text="RUNNERS: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    pairtrackLabel.grid(row=4, column=0)
    stoptrackLabel.grid(row=5, column=0)
    tptrackLabel.grid(row=6, column=0)

    pairInput.configure(state='readonly')
    stopInput.configure(state='readonly')
    tpInput.configure(state='readonly')
    orderButton.config(state='disabled')

    def track_and_update_labels():
        global maxrr
        tpOutput = "NOT MET";
        stopOutput = "NOT MET"
        currentPrice = float(price(pair))
        targetsMet = track(pair, targets, stop, initialPrice)
        stop_loop = False

        newmaxrr = (currentPrice - initialPrice)/(initialPrice - stop)
        if (newmaxrr > maxrr):
            maxrr = newmaxrr

        for i in range(len(targetsMet)):
            if targetsMet[i]:
                tpOutput = "MET"
                stop_loop = True
                break

        if (initialPrice > stop and currentPrice < stop) or (initialPrice < stop and currentPrice > stop):
            stopOutput = "MET"
            stop_loop = True

        pairOutputLabel.config(text=currentPrice)
        stopOutputLabel.config(text=stopOutput)
        tpOutputLabel.config(text=tpOutput)
        if (not stop_loop):
            root.after(1000, track_and_update_labels)  # Schedule the function to be called again after 15 seconds
        else:
            logButton = Button(root, text="Log", command=lambda: log())
            logButton.grid(row=7, column=0)
        
        

    # Initialize labels
    pairOutputLabel = Label(root, text="", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    stopOutputLabel = Label(root, text="", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    tpOutputLabel = Label(root, text="", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    pairOutputLabel.grid(row=4, column=1)
    stopOutputLabel.grid(row=5, column=1)
    tpOutputLabel.grid(row=6, column=1)

    # Start the update loop
    track_and_update_labels()
    




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
orderButton = Button(root, text="Order", command=lambda: order())

# Gridding Widgets
pairLabel.grid(row=0, column=0)
pairInput.grid(row=0, column=1)
stopLabel.grid(row=1, column=0)
stopInput.grid(row=1, column=1)
tpLabel.grid(row=2, column=0)
tpInput.grid(row=2, column=1)
tpOrderButton.grid(row=2, column=3)
orderButton.grid(row=3, column=0)

root.mainloop() 



