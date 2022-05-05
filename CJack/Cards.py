import random

class Cards:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
    def toString(self):
        print(f"{self.name} {self.value}")
    def check(self, card):
        if (self.value > card.value):
            return 1
        elif (self.value == card.value):
            return 0
        else: 
            return -1 

def getDeck():
    cards = []
    
    ace = Cards("Ace", 11)
    cards.append(ace)
    deuce = Cards("Deuce", 2)
    cards.append(deuce)
    Three = Cards("Three", 3)
    cards.append(Three)
    Four = Cards("Four", 4)
    cards.append(Four)
    Five = Cards("Five", 5)
    cards.append(Five)
    Six = Cards("Six", 6)
    cards.append(Six)
    Seven = Cards("Seven", 7)
    cards.append(Seven)
    Eight = Cards("Eight", 8)
    cards.append(Eight)
    Nine = Cards("Nine", 9)
    cards.append(Nine)
    Ten = Cards("Ten", 10)
    cards.append(Ten)
    Jack = Cards("Jack", 10)
    cards.append(Jack)
    Queen = Cards("Queen", 10)
    cards.append(Queen)
    King = Cards("King", 10)
    cards.append(King)
    
    newCards = [x for x in cards for _ in range(32)]
    random.shuffle(newCards)
    return newCards