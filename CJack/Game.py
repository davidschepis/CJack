from Database.DB_Functions import DB
import Cards
import time

def splash_screen():
    print(".------..------..------..------..------.")
    print("|C.--. ||J.--. ||A.--. ||C.--. ||K.--. |")
    print("| :/\: || :(): || (\/) || :/\: || :/\: |")
    print("| :\/: || ()() || :\/: || :\/: || :\/: |")
    print("| '--'C|| '--'J|| '--'A|| '--'C|| '--'K|")
    print("`------'`------'`------'`------'`------'")
    
def score_screen():
    scores = DB.get_scores()
    for i in scores:
        id, username, joined, wins, losses, pushes = i
        print(f"ID: {id} | Username: {username} | Joined: {joined} | Wins: {wins} | Losses: {losses} | Pushes: {pushes}")
    user_input = -1
    while user_input != 1:
        print("1. Return")
        try:
            user_input = int(input())
        except ValueError:
            continue
    login()

def login():
    user_input = -1
    while user_input != 1 and user_input != 2 and user_input !=3 and user_input != 4:
        print("\nPlease select from the following options:")
        print("1. Login")
        print("2. Signup")
        print("3. Check Scores")
        print("4. Quit")
        try:
            user_input = int(input())
        except ValueError:
            continue
    if user_input == 1:
        login_screen()
    elif user_input == 4:
        exit()
    elif user_input == 3:
        score_screen()
    else:
        signup_screen()
        
def get_sum(cards):
    sum = 0
    for i in cards:
       sum += i.value
    return sum 

def hit_stay():
    user_input = -1
    while(user_input != 1 and user_input != 2):
        print("1. Hit")
        print("2. Stay")
        try:
            user_input = int(input())
            return user_input
        except ValueError:
            continue
        
def bj(deck):
    dealer_cards = []
    dealer_cards.append(deck.pop())
    dealer_cards.append(deck.pop())
    
    player_cards = []
    player_cards.append(deck.pop())
    player_cards.append(deck.pop())
    
    print(f"\nDealer shows a {dealer_cards[0].name}")
    print(f"You have a {player_cards[0].name} and {player_cards[1].name}, total = {get_sum(player_cards)}")
    
    while hit_stay() != 2:
        new_card = deck.pop()
        player_cards.append(new_card)
        print(f"You drew a {new_card.name}, total = {get_sum(player_cards)}")
        time.sleep(1)
        if get_sum(player_cards) > 21:
            print("You bust!")
            print(f"Dealer had a {dealer_cards[0].name} and {dealer_cards[1].name}, total = {get_sum(dealer_cards)}")
            return -1
    
    print(f"Dealer has {dealer_cards[0].name} and {dealer_cards[1].name}")
    while get_sum(dealer_cards) < 17:
        new_card = deck.pop()
        dealer_cards.append(new_card)
        print(f"Dealer drew a {new_card.name}, total = {get_sum(dealer_cards)}")
        time.sleep(1)
    if get_sum(dealer_cards) > 21:
        print(f"You win!, dealer busted with {get_sum(dealer_cards)}")
        return 1
    elif get_sum(player_cards) > get_sum(dealer_cards):
        print(f"You win!, dealer has {get_sum(dealer_cards)}")
        return 1
    elif get_sum(player_cards) == get_sum(dealer_cards):
        print(f"You push, dealer has {get_sum(dealer_cards)}")
        return 0
    else:
        print(f"You lose, dealer has {get_sum(dealer_cards)}")
        return -1

def play_bj(user):
    username, id = user
    print(" _          _   _      ______ _             ")
    print("| |        | | ( )     | ___ \ |           ")
    print("| |     ___| |_|/ ___  | |_/ / | __ _ _   _")
    print("| |    / _ \ __| / __| |  __/| |/ _` | | | |")
    print("| |___|  __/ |_  \__ \ | |   | | (_| | |_| |")
    print("\_____/\___|\__| |___/ \_|   |_|\__,_|\__, |")
    print("                                       __/ |")
    print("                                      |___/ ")
    deck = Cards.getDeck()
    while True:
        if len(deck) < 10:
            break
        user_input = -1
        while user_input != 1 and user_input != 2:
            print("1. New Game")
            print("2. Quit")
            try:
                user_input = int(input())
            except ValueError:
                continue
        if user_input == 2:
            home_screen(user)
            break
        else:
            result = bj(deck)
            if result == 1:
                DB.increment_wins(id)
            elif result == -1:
                DB.increment_losses(id)
            else:
                DB.increment_pushes(id)
    
            
def home_screen(user):
    username, id = user
    wins, losses, pushes = DB.get_user_data(id)
    print(f"\nWelcome {username}!")
    print(f"Wins: {wins} | Losses: {losses} | Pushes: {pushes}\n")
    user_input = -1
    while user_input != 1 and user_input != 2 and user_input !=3:
        print("Please select from the following optons:")
        print("1. Play Blackjack!")
        print("2. Logout")
        print("3. Quit")
        try:
            user_input = int(input())
        except ValueError:
            continue
    if user_input == 3:
        exit()
    elif user_input == 2:
        login()
    else:
        play_bj(user)
    
def signup_screen():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    result = DB.signup(username, password)
    if not result:
        print("Please select a different username\n")
        login()
    home_screen(result)

def login_screen():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    result = DB.login(username, password)
    if not result:
        print("Unable to login")
        login()
    home_screen(result)

def start():
    splash_screen()
    login()
    
start()