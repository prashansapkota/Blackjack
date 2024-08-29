card_number = int(input("Enter card number: "))
if card_number >= 1 and card_number <= 13:
    if card_number == 1: 
        print("Your hand value is 11.")
    elif card_number >= 2 and card_number <= 9:
        print("Your hand value is " + str(card_number) + ".")
    else:
        print("Your hand value is 10.")
else:
       print("BAD CARD")