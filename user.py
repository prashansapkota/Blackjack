from random import randint

# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

hand_value = 0


# Initial two cards
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



# Asking user to hit or stay
while hand_value < 21:
    print(f"You have {hand_value}. Hit (y/n)?", end= " ")
    user_input = input("").strip().lower()
    
    if user_input == "y":
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

    elif user_input == "n":
        break
    else:
        print("Sorry I didn't get that.")
        

# Final hand output
print(f"Final hand: {hand_value}.")

# Check for Blackjack or Bust
if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21:
    print("BUST.")
