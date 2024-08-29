
#Print Card Name
card_number = int(input(" "))
if card_number >= 1 and card_number <= 13:
    if card_number == 1:
        print("Drew an Ace")
    elif card_number >= 2 and card_number <= 7:
        print("Drew a " + str(card_number))
    elif card_number == 8:
        print("Drew an 8")
    elif card_number >= 9 and card_number <= 10:
        print("Drew a " + str(card_number))
    elif card_number == 11:
        print("Drew a Jack")
    elif card_number == 12: 
        print("Drew a Queen")
    else:
        print("Drew a King")
else:
    print("BAD CARD") 
    
    
    
