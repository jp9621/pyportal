import requests
import json
import time
from tkinter import *

# Defining the Window
root = Tk()
root.title("JAPAFX")
root.configure(bg='#36393E')
targets = [];

def write_callback(response, data):
    response += data
    return response

def price(currency_pair):
    url = f"https://api-fxpractice.oanda.com/v3/accounts/101-001-26231816-001/pricing?instruments={currency_pair}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer f18a87ad84976c1010503042a9621689-8ff03716635ad7204a2c83b52cea3d36"
    }

    try:
        response = ""
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Parse the JSON response
        json_response = response.json()

        # Output the price of the instrument
        for instrument in json_response["prices"]:
            price = instrument["asks"][0]["price"]
            return float(price)

    except requests.exceptions.RequestException as e:
        print(f"Failed to perform connection: {e}")

    return 0.0

def track(currency_name, targets, stoploss, initial_price):
    # Get the price for the currency pair using price() function
    current_price = price(currency_name)

    targets_met = [False] * len(targets)

    # Check if targets are met
    for i in range(len(targets)):
        if ((current_price >= targets[i] and stoploss < current_price) or
           (current_price <= targets[i] and stoploss > current_price)):
            targets_met[i] = True
            print(f"Target {targets[i]} met")

        if ((current_price < stoploss and stoploss < initial_price) or
           (current_price > stoploss and stoploss > initial_price)):
            print("Stopped Out")

    # Return the list of targets met
    return targets_met

def csv(currency_pair, session, biastf, entrytf, conftf, conftype, maxrr, setuptype, be, TP1, TP2, rs, comments):
    csvcontent = f'"{currency_pair}","{session}","{biastf}","{entrytf}","{conftf}","{conftype}",' \
                 f'"{maxrr}","{setuptype}","{be}","{TP1}","{TP2}","{rs}","{comments}"\n'

    try:
        with open("log.csv", "a") as outputFile:
            outputFile.write(csvcontent)
        print("CSV data appended successfully.")
    except Exception as e:
        print("Unable to open the CSV file:", str(e))

def targetAdd(target):
    targets.append(target);

def orderButton(targets):
    pair = pairInput.get()
    stop = stopInput.get()

    tpList = targets
    initialPrice = price(pair)

    tpList = targets
    initialPrice = price(pair)

    pairtrackLabel = Label(root, text="PAIR: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    stoptrackLabel = Label(root, text="STOPLOSS: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    tptrackLabel = Label(root, text="RUNNERS: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)

    pairtrackLabel.grid(row=4, column=0)
    stoptrackLabel.grid(row=5, column=0)
    tptrackLabel.grid(row=6, column=0)
        

    while True:
      
        tpOutput = "NOT MET";
        stopOutput = "NOT MET"
        while True:
            currentPrice = price(pair)
            targetsMet = track(pair, tpList, stop, initialPrice)
            for i in range(len(targetsMet)):
                if (targetsMet[i]):
                    tpOutput = "MET"
            if ((initialPrice > stop and currentPrice < stop) or (initialPrice < stop and currentPrice > stop)):
                stopOutput = "MET"
                break
            pairOutputLabel = Label(root, text=pair, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
            stopOutputLabel = Label(root, text=stopOutput, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
            tpOutputLabel = Label(root, text=tpOutput, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
            pairOutputLabel.grid(row=4, column=1)
            stopOutputLabel.grid(row=5, column=1)
            tpOutputLabel.grid(row=6, column=1)
            time.sleep(15)
        




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
tpOrderButton = Button(root, text="+", command=targetAdd(tpInput.get()))


# Gridding Widgets
pairLabel.grid(row=0, column=0)
pairInput.grid(row=0, column=1)
stopLabel.grid(row=1, column=0)
stopInput.grid(row=1, column=1)
tpLabel.grid(row=2, column=0)
tpInput.grid(row=2, column=1)
tpOrderButton.grid(row=2, column=3)


# Declaring and Gridding Calculate Button
orderButton = Button(root, text="Order", command=orderButton(targets), fg=fg, bg=bg,font=font)
orderButton.grid(row=3, column=0)

root.mainloop() 


