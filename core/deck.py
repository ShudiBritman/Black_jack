import random

from urllib3.util import is_fp_closed


def create_card(rank:str, suit:str):
    card = {}
    card["rank"] = rank
    card["suit"] = suit
    return card


def build_standard_deck():
    list_suites = ["H", "C", "D", "S"]
    list_rank = ["J", "Q", "K", "A"]
    dec_of_cards = []

    for i in range(len(list_suites)):
        for j in range(2, 11):
            card = create_card(str(j), list_suites[i])
            dec_of_cards.append(card)

        for j in list_rank:
            card = create_card(j, list_suites[i])
            dec_of_cards.append(card)
    return dec_of_cards



def shuffle_by_suit(deck, swaps=5000):
    for _ in range(swaps):
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        if i != j:
            is_divisible = chack_suit(deck[i], j)
            if is_divisible:
                deck = swap(deck, i, j)
    return deck


def swap(list, i1, i2):
    list[i1], list[i2] = list[i2], list[i1]

    return list


def chack_suit(card, index):
    dividers = {
        "H":5,
        "C":3,
        "D":2,
        "S":7
            }
    if index % dividers[card["suit"]] == 0:
        return True
    else:
        return False









 # if index % 5 == 0:
 #            return True
 #        else:
 #            return False
 #    elif card["suite"] == "C":
 #        if index % 3 == 0:
 #            return True
 #        else:
 #            return False
 #    elif card["suite"] == "D":
 #        if index % 2 == 0:
 #            return True
 #        else:
 #            return False
 #    elif card["suite"] == "S":
 #        if index % 7 == 0:
 #            return True
 #        else:
 #            return False
