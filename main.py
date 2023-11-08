import requests
import json
from tkinter import *

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


from tkinter import *

# Defining the Window
root = Tk()
root.title("JAPAFX")
root.configure(bg='#36393E')

# Creating some default appearance related settings for window elements
padx = 5
pady = 5
bg = '#4A4D52'
bgi = '#8ADBC8'
fg = '#9EF8AE'
font = ('Arial', 14)
lightblack = '#5D636C'
gray = '#DBE5E3'

# Defining Label
pairLabel = Label(root, text="Pair: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
stopLabel = Label(root, text="Stop: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
tpLabel = Label(root, text="TP1: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)


# Defining Input
virionInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
bmiInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
bmiInput.insert(0, "kg")
ageInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
ageInput.insert(0, "0-24 Months")
genderInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
genderInput.insert(0, "Male or Female")
symptomOnsetInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
symptomOnsetInput.insert(0, "Old or Recent")

# Gridding Widgets
virionLabel.grid(row=0, column=0)
virionInput.grid(row=0, column=1)
bmiLabel.grid(row=1, column=0)
bmiInput.grid(row=1, column=1)
ageLabel.grid(row=2, column=0)
ageInput.grid(row=2, column=1)
genderLabel.grid(row=3, column=0)
genderInput.grid(row=3, column=1)
symptomOnsetLabel.grid(row=4, column=0)
symptomOnsetInput.grid(row=4, column=1)

# Declaring and gridding all the output labels necessary
    infectabilityLabel = Label(root, text="Infectability: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    durationLabel = Label(root, text="Duration: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    infectabilityOutput = Label(root, text= infectabilityReport, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    durationOutput = Label(root, text= durationReport, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    infectabilityLabel.grid(row=6, column=0)
    durationLabel.grid(row=7, column=0)
    infectabilityOutput.grid(row=6, column=1)
    durationOutput.grid(row=7, column=1)

# Declaring and Gridding Calculate Button
calculateButton = Button(root, text="Calculate", command=calculate, fg=fg, bg=bg,font=font)
calculateButton.grid(row=5, column=0)





# have to change all labels to tp1 tp2 and also make a new method for creating new labels 

root.mainloop() 


