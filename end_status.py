hand_value = int(input(""))
if hand_value < 4 or hand_value > 31:
    print("BAD HAND VALUE!")
else:
    if hand_value == 21:
        print("BLACKJACK!")
    else:
        print("BUST.")