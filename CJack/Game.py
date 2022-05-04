from Database.DB_Functions import DB

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
        id, username, joined, chips, wins, losses, chips_won, chips_lost = i
        print(f"ID: {id} | Username: {username} | Chips: {chips}| Joined: {joined} | Wins: {wins} | Losses: {losses} | Earnings: {chips_won} | Lost Chips: {chips_lost}")


def login():
    user_input = -1
    while user_input != 1 and user_input != 2 and user_input !=3:
        print("Please select from the following options:")
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
        
def home_screen(user):
    print(user)
    pass
        
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