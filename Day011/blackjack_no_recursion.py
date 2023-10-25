import random
# import os
# from art import logo


def initial_hands():
    initial_player_hand = []
    initial_dealer_hand = []

    initial_dealer_hand += [random.choice(cards), random.choice(cards)]
    initial_player_hand += [random.choice(cards), random.choice(cards)]

    while sum(initial_dealer_hand) != 22 and sum(initial_player_hand) != 22:
        print(f"Your cards: [{initial_player_hand}], current score: {sum(initial_player_hand)}")
        print(f"Computer's first card: {initial_dealer_hand[0]}")
        return {'player' : initial_player_hand, 'dealer' : initial_dealer_hand}


def new_card(dict_hands, participant):
    for person in dict_hands:
        if person == participant:
            dict_hands[person] += [random.choice(cards)]
    return dict_hands


def show_score(both_hands):
    print(f"Your cards {both_hands['player']}, current score: {sum(both_hands['player'])}")
    print(f"Computer's cards {both_hands['dealer']}, current score: {sum(both_hands['dealer'])}")


def play_again():
    again = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")    
    if again == 'y':
        return True
    else:
        return False


def new_game():
#        os.system('clear')
    hands = initial_hands()
    flag = False
    while flag == False:
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if more_cards == 'n':
            flag = True
            continue
        else:
            hands = new_card(hands, 'player')
            print(f"Your cards {hands['player']}, current score: {sum(hands['player'])}")
            print(f"Computer's first card: {hands['dealer'][0]}")
            if sum(hands['player']) > 21:
                show_score(hands)
                print("You lose :(")
                return None

    player_score = sum(hands['player'])
    dealer_score = sum(hands['dealer'])
    if dealer_score > player_score:
        show_score(hands)
        print("You lose :(")
        return None
    elif dealer_score == player_score:
        show_score(hands)
        print("Draw")
        return None
    else:
        while dealer_score < 17 or dealer_score < player_score:
            hands = new_card(hands, 'dealer')
            dealer_score = sum(hands['dealer'])
            if dealer_score > player_score and dealer_score <= 21:
                show_score(hands)
                print("You lose :(")
                return None
            elif dealer_score < player_score: # <<<<< Cuando llega a este punto el dealer ha pedido carta y no se cumple la condicion del while
                continue
            elif dealer_score == player_score:
                show_score(hands)
                print("Draw")
                return None
            elif dealer_score > 21:
                show_score(hands)
                print("You win :)")
                return None
            elif dealer_score == 21 and player_score ==21:
                show_score(hands)
                print("You lose :(")
                return None

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while play_again():
    new_game()
