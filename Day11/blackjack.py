import random

def deal_card():
    """Returns a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)      
        
    return sum(cards)

def compare(users_score, dealers_score):
    if users_score == dealers_score:
        return "Draw"
    elif dealers_score == 0:
        return "Lose, opp has a BJ!"
    elif users_score == 0:
        return "Win, u have a BJ!"
    elif users_score > 21:
        return "U lose, too many!"
    elif dealers_score > 21:
        return "U win, opponent went too many!"
    elif users_score > dealers_score:
        return "U win!"
    else:
        return "U lose!"    
    
def play_game():
    user_cards = []
    dealer_cards = []
    dealer_score = 1
    user_score = 1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Ur cards: {user_cards}, current score: {user_score}")
        print(f"Dealers first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw or type 'n' to stand!").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)


    print(f"Ur final hand is: {user_cards} and the final score is: {user_score}.")
    print(f"Dealers final hand is: {dealer_cards} and the final score is: {dealer_score}") 
    print(compare(user_score, dealer_score))

while input("Wanna play? 'y' or 'n'?: ") == "y":
    print("\n" * 100)
    play_game()