import random
from game_data import data
from art import logo1
from art import logo2
import os

def contenstant_selection(data):
    first_competitor = random.choice(data)
    return first_competitor


def contest(competitor1, competitor2):
    print(logo1)
    print(f"Compare A: {competitor1['name']}, {competitor1['description']}, from {competitor1['country']}")
    print(logo2)
    print(f"Against B: {competitor2['name']}, {competitor2['description']}, from {competitor2['country']}")
    print("Who has more followers? Type 'A' or 'B'")


def followers_comparison(competitor1, competitor2):
    return competitor1 if competitor1['follower_count'] > competitor2['follower_count'] else competitor2
    # if competitor1['follower_count'] > competitor2['follower_count']:
    #     return competitor1
    # elif competitor1['follower_count'] < competitor2['follower_count']:
    #     return competitor2


def guess_verification(winner, first_contenstant, second_contenstant):
    print(f"The followers winner is: {winner['name']}")
    choice = input("Who has more followers? ").lower()
    return first_contenstant if choice == 'a' else second_contenstant


def higher_or_lower(first_contestant, second_contestant, consecutives):
    print(f">>> Your streak is: {consecutives}")
    os.system('clear')
    contest(first_contestant, second_contestant)
    print(f">>> Your streak is: {consecutives}")
    winner = followers_comparison(first_contestant, second_contestant)
    player_choice = guess_verification(winner, first_contestant, second_contestant)
    if winner == player_choice:
        first_competitor = player_choice
        second_competitor = contenstant_selection(data)
        return higher_or_lower(first_competitor, second_competitor, consecutives + 1)
    else:
        print(f">>> I'm sorry you lose. Your streak was: {consecutives}")
        return None


while True:
    first_participant = contenstant_selection(data)
    second_participant = contenstant_selection(data)
    if first_participant == second_participant:
        continue
    else:
        break

higher_or_lower(first_participant, second_participant, 0)