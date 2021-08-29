from flask import Flask, request, render_template, url_for

import random


print("~~~~~~~~ TEMA VIII ~~~~~~~~")
print()
print()



card_list = []



class Card:

    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
    

class Deck:
  

    def AddCard(value, symbol, card_list):
        if value in {'A','J','Q','K','2','3','4','5','6','7','8','9','10'}:
            if {'inima rosie', 'inima neagra', 'trefla', 'romb'}:
                card_list.append(Card(value,symbol))
            else:
                raise ValueError("Not a valid symbol")
        else:
            raise ValueError("Not a valid value")


    def DeleteCard(answer, card_list):
        for item in card_list:
            if item.value == answer:
                card_list.remove(item)


    def Deck_shuffle(card_list):
        random.shuffle(card_list)
   














app = Flask(__name__)


@app.route('/main', methods = ["POST", "GET"])
def main():
    return "~~~~~~~~~~~~~~~~~~~~~~  Tema VIII ~~~~~~~~~~~~~~~~~~~~~~   \n\n\nHow many card do you want to add to the deck? [ADD THE NUMBER IN THE URL <>]"



@app.route('/deck/<number>', methods = ['GET'])
def choice(number):
    
    return "Enter the [value] of the card and the [symbol] (Form)"



@app.route('/deck/add', methods = ["POST"])
def deck():
    val = request.form['value']
    sim = request.form['symbol']
    Deck.AddCard(val,sim,card_list)

    return f"The card {val} of {sim} was succesfully added to the deck"
    

@app.route('/deck/print', methods = ['GET'])
def print():
 
    temp = " "
    for obj in card_list:
        temp += (obj.value + "---" + obj.symbol + "\n")

    return temp

@app.route('/deck/delete', methods = ['POST'])
def delete():
    discriminated = request.form['delete']

    Deck.DeleteCard(discriminated,card_list)
    return f"The card {discriminated} was deleted succesfully from the deck"

@app.route('/deck/shuffle', methods = ['GET'])
def shuffle():
    Deck.Deck_shuffle(card_list)
    return f"Deck was shuffled succefuslly"







    


if __name__ == "__main__":
    app.run()

    