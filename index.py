# Take a number between 1 and 13 representing a card as input. Print out the card name as output. If the given card is:

# 1: print “Drew an Ace”
# 2-10: print “Drew a [number]” (ex: if the number is 5, it'll print “Drew a 5”). If the card is an 8 then print out "an" instead of "a" to be grammatically correct.
# 11: print “Drew a Jack”
# 12: print “Drew a Queen”
# 13: print “Drew a King”
# Any other number: print "BAD CARD"

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
    
    
    
