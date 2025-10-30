from numpy.ma.core import choose

from core.player_io import ask_player_action
from utils.utils import check_who_won, check_if_pass, is_won


def calculate_hand_value(hand):
    rank_value = {
        "A":1
                }
    sum_of_hund = 0
    for i in range(len(hand)):
        rank = hand[i]["rank"]
        if rank.isdigit():
            value = int(rank)
            sum_of_hund += value
        else:
            if rank == "A":
                value = 1
                sum_of_hund += value
            else:
                value = 10
                sum_of_hund += value
    return sum_of_hund


def deal_two_each(deck, player, dealer):
    for i in range(4):
        temp = deck.pop(0)
        if i < 2:
            player["hand"].append(temp)
        else:
            dealer["hand"].append(temp)
    p_hand = calculate_hand_value(player["hand"])
    d_hand = calculate_hand_value(dealer["hand"])
    print(f"The value of the hand the player has is: {p_hand}")
    print(f"The value of the hand the dealer has is: {d_hand}")
    return

def dealer_play(deck, dealer):
    dealer_hand = 1
    while dealer_hand < 17:
        temp = deck.pop(0)
        dealer["hand"].append(temp)
        print(f"A card has been added to the dealer {temp}")
        dealer_hand = calculate_hand_value(dealer["hand"])
        print(f"total of the dealer is {dealer_hand}")
    won = is_won(dealer_hand)
    if won:
        return "Won"
    if dealer_hand > 21:
        return False
    else:
        return True


def player_play(deck, player):
    temp = deck.pop(0)
    player["hand"].append(temp)
    sum_of_hand = calculate_hand_value(player["hand"])
    print(f"A card has been added to you {temp}")
    print(f"Your total is {sum_of_hand}")
    won = is_won(sum_of_hand)
    if won:
        return "Won"
    is_pass = check_if_pass(sum_of_hand)
    if is_pass:
        return False
    else:
        return True




def run_full_game(deck, player, dealer):
    deal_two_each(deck, player, dealer)
    play = True
    d_play = True
    p_play = True
    won = False
    while play and not won:
        choose = ask_player_action()
        if choose == "H":
            p_play = player_play(deck, player)
            if p_play == "Won":
                won = True
                winner = "player"
            play = p_play
        else:
            d_play = dealer_play(deck, dealer)
            if d_play == "Won":
                won = True
                winner = "dealer"
            play =  d_play
    if won:
        print(f"Winner is {winner}")
    elif d_play:
        won = check_who_won(player, dealer)
        print(f"Winner is {won}")
    elif p_play:
        print(f"winner is player")



