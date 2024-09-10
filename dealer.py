
from random import randint
hand_value = 0
#Generating two random cards
for i in range(2):
    card_rank = randint(1, 13)
    if card_rank == 1:
        card_name = "Ace"
        card_value = 11
         
    elif card_rank == 11:
        card_name = "Jack"
        card_value = 10
    elif card_rank == 12:
        card_name = "Queen"
        card_value = 10
    elif card_rank == 13:
        card_name = "King"
        card_value = 10
    else:
        card_name = str(card_rank)
        card_value = card_rank

    if card_rank == 1 or card_rank == 8:
        drew_prefix = "Drew an "
    else:
        drew_prefix = "Drew a "

    print(drew_prefix + card_name)
    hand_value += card_value

#printing hand_value only if hand_value is less than17
while hand_value < 17:
    print(f"Dealer has {hand_value}.")
    
    # Drawing another card
    card_rank = randint(1, 13)

    if card_rank == 1:
        card_name = "Ace"
        card_value = 11
        aces += 1  
    elif card_rank == 11:
        card_name = "Jack"
        card_value = 10
    elif card_rank == 12:
        card_name = "Queen"
        card_value = 10
    elif card_rank == 13:
        card_name = "King"
        card_value = 10
    else:
        card_name = str(card_rank)
        card_value = card_rank

    
    if card_rank == 1 or card_rank == 8:
        drew_prefix = "Drew an "
    else:
        drew_prefix = "Drew a "

    print(drew_prefix + card_name)
    hand_value += card_value

print(f"Final hand: {hand_value}.")

if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21:
    print("BUST.")