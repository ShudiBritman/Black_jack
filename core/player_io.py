def ask_player_action():
    choose = 0
    while not choose:
        choose = input("What you want? 'H' to hit, 'S' to stand")
        choose = choose.capitalize()
        if choose != "S" and choose != "H":
            print("Please choose 'S' or 'H' ")
            choose = 0
    return choose



