# Blackjack card game

## Overview
This project is a simple implementation of the Blackjack card game using Python and object-oriented programming (OOP) principles. The game allows a user to play against the dealer, with game logic handling card values, gameplay flow, and determining the game outcome.

## Features
- User and dealer gameplay logic
- Calculation of card values (including Ace's special behavior)
- Determination of win/loss/tie scenarios
- Simplified object-oriented structure for easier maintenance and updates

## Files and Structure

- `blackjack.py`: The main game file that initializes the game, controls gameplay, and handles the interactions between the user and the dealer.
- `dealer.py`: Contains the logic for the dealer's gameplay, including decision-making based on standard Blackjack rules.
- `user.py`: Manages the user's gameplay, including drawing cards, deciding to hit or stand, and calculating the total score.
- `end_status.py`: Responsible for determining and displaying the result of the game (win, lose, or tie).
- `index.py`: A helper file used to manage different elements of the game, such as initializing game objects and managing interactions between components.
- `value.py`: Assigns values to the cards and calculates the user's and dealer's hand totals, handling special cases like the Ace card.

## How to Play
1. Run the `blackjack.py` file to start the game.
2. The user is prompted to either hit (draw another card) or stand (keep current hand).
3. The dealer plays automatically based on standard Blackjack rules (dealer must hit if their hand value is below 17).
4. The game ends when either the user or dealer wins, loses, or ties, and the result is displayed.

## Requirements
- Python 3.x


