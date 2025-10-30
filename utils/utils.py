


def calculater_hand_value(hand):
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


def check_if_pass(sum_of_hand):
    if sum_of_hand > 21:
        print("You have exceeded the amount and are disqualified!")
        return True
    else:
        return False
def is_won(sum_of_hand):
    if sum_of_hand == 21:
        return True
    else:
        return False

def check_who_won(player, dealer):
    sum_player = calculater_hand_value(player["hand"])
    sum_dealer = calculater_hand_value(dealer["hand"])
    if sum_player > 21:
        return "dealer"
    elif sum_dealer > sum_player:
        return "dealer"
    else:
        return "dealer"