from tkinter import *
from tkinter import ttk, messagebox
from random import randint
from pygame import *
import sys

# Define the number of coins.
coins = 50

# Create the window. The window should be large enough to fit all the widgets.
# The colour purple also gives more of a casino look.
slot = Tk()
slot.geometry('670x320')
slot.title('Slot Machine Game')
slot.config(bg = 'purple')

# Create the main label title and place it on the top of the window.
mainslotlabel = Label(slot, text = 'Slot Machine', font = 'times 40 italic', bg = "light green")
mainslotlabel.grid(row = 0, column = 12)

#


# Create a label that will ask the user how many coins they would like to select.
# This should be above the combobox that changes the amount of coins that can be bet.
combolabel = Label(slot, text = 'How many coins would you like to bet?', bg = 'red', font = 'times 15 bold', relief = 'raised')
combolabel.grid(row = 7, column = 15, sticky = S)

# Create a combobox. This combobox should have 3 options to chose between so you can bet more for the chance to earn more coins in return.
# The combobox should be below the label asking how many coins the user would like to bet.
bettingoptions = ttk.Combobox(slot, values = (1,2,3))
bettingoptions.grid(row = 10, column = 15)

# Define choice to allow the user to chose between betting options.
def choice():
    betting = int(bettingoptions.get())
    return betting

# Create slot 1. Use big font and have a nice coloured background. The box should be 'raised'.
# The slot should be in the middle of the window and slightly to the left of the other slots.
slot1 = Label(slot, text = " ",font = "Verdana 70 bold", bg = "orange", relief = "raised")
slot1.grid(row = 2, column = 11)

# Create slot 2. Use the same font, but a different coloured background as slot 1. The box should also be 'raised'.
slot2 = Label(slot, text = " ",font = "Verdana 70 bold", bg = "red", relief = "raised")
slot2.grid(row = 2, column = 12)

# Create slot 3. use the same font, but a different coloured background as slot 1 and 2. The box should also be 'raised'.
slot3 = Label(slot, text = " ",font = "Verdana 70 bold", bg= "light blue", relief = "raised")
slot3.grid(row = 2, column = 13)

# This function will generate the 3 numbers that will be between 1-4.
# It is important to define 'play' in order to allow the button to carry out the functions to make the slot work.
def play():
    global coins
    betop = int(bettingoptions.get())
    # Spins will not work without enough coins.
    if coins < betop:
        messagebox.showinfo("error", "You do not have enough coins to spin")
    # Generate 3 numbers between 1-4.
    else:
        num1 = randint(1,4)
        num2 = randint(1,4)
        num3 = randint(1,4)
        slot1.config(text = num1)
        slot2.config(text = num2)
        slot3.config(text = num3)
        # If the user bets 1 coin, they will lose 1 coin every time they bet, but will only be rewarded 5 coins if they win.
        if betop == 1:
            # If all three generated numbers equal each other than the user will be rewarded coins.
            if num1 == num2 and num2 == num3:
                coins = coins + 5
                coinslabel.config(text=str(coins))
                # A message box will appear and congratulate the user for gaining 10 coins.
                messagebox.showinfo("Congratulations", "You have won 5 coins!")
                # When the user wins 5 coins, they will hear a cashier sound effect,
                mixer.init()
                mixer.music.load('chaching.mp3')
                mixer.music.play()
                # If the user does not win, they will lose a coin.
            else:
                coins = coins - 1
                coinslabel.config(text=str(coins))
                # They will also hear a sound effect of a coin being entered into the machine.
                mixer.init()
                mixer.music.load('coinenter.mp3')
                mixer.music.play()
            # The function below will perform the same task by rewarding the user 10 coins for betting 2. All three generated numbers must be equal for the reward.
        if betop == 2:
            if num1 == num2 == num3:
                coins = coins+10
                coinslabel.config(text=str(coins))
                # A message box will congratulate the user for winning 10 coins.
                messagebox.showinfo("Congratulations", "You have won 10 coins!")
                # Since 5 more coins isnt a big step up the same sound effect will be played to congratulate the user for winning coins.
                mixer.init()
                mixer.music.load('chaching.mp3')
                mixer.music.play()
            else:
                # If the user does not win they will lose 2 coins for betting.
                coins = coins-2
                coinslabel.config(text=str(coins))
                mixer.init()
                mixer.music.load('coinenter.mp3')
                mixer.music.play()
            # The function below will perform the same task by rewarding the user 15 coins for betting 3. All three generated numbers must be equal for the reward.
        if betop == 3:
            if num1 == num2 == num3:
                coins = coins + 15
                coinslabel.config(text = str(coins))
                # A message box will appear congratulating the user for winning 15 coins.
                messagebox.showinfo("Congratulations", "You have won 15 coins!")
                mixer.init()
                # Since 15 is the grand prize a more exciting and long song will play, which will congratulate the user for winning.
                mixer.music.load('moneymoney.mp3')
                mixer.music.play()
            # If the user doesnt win they will lose 2 coins for betting.
            else:
                coins = coins - 3
                coinslabel.config(text=str(coins))
                mixer.init()
                mixer.music.load('coinenter.mp3')
                mixer.music.play()

# Create a play button that will allow the function above to work by being clicked. The slots will run and simulate and coins will be removed or added.
btnPlay = Button(slot, text = 'Play', font = 'times 20 italic', fg = 'orange', command = play)
btnPlay.grid(row = 50, column = 12)

# This label shows "coins:" to label the number that will be inputted which would be the number of coins.
cointitlelabel = Label(slot, text = "Coins:", fg = 'Yellow', bg = 'orange', font = 'Verdana 30 bold', relief = 'raised')
cointitlelabel.grid(row =77, column = 11)

# This label will display the updated amount of coins after every play/spin.
coinslabel = Label(slot, text = "Coins", fg = 'yellow', bg = 'orange', font = 'verdana 30 bold', relief = 'raised')
coinslabel.grid(row=77, column=12)
coinslabel.config(text = str(coins))

# Create a box that displays the game rules and information on how to play the game.
# Define an infobox that will be activated by a feature I have learned on my own (lambda).
def infobox():
    messagebox.showinfo("Game rules and information","Game rules\n 1 coin bet = possibility of 5 coin reward\n 2 coin bet = possibility of 10 coin reward\n 3 coin bet = possibility of 15 coin reward.\n Select the amount of coins you would like to bet in the combo box below")
infobtn = Button(slot, text = 'Show rules and info', font = 'times 18 bold', fg = 'green', relief = 'raised', command = lambda: infobox())
infobtn.grid(row = 1, column = 15)

# Change the icon.
# On Mac OS we must use gif.
# I chose to use a picture of a casino slot.
if sys.platform.startswith('slot'):
    slot.iconbitmap('slotmac.gif')
else:
    logo = PhotoImage(file='slotmac.gif')
    slot.call('wm', 'iconphoto', slot._w, logo)

slot.mainloop()
