# Bingo_Low_Level_Design
Repository contains a low level design for a Bingo Game

## Description
We have to design a simple variation for Bingo Game. In this game, a player will be dealt a set of 25 cards. Each card would have a random number between 1-50

Player1  cards: <br />
31  &nbsp;43  &nbsp;9   &nbsp;2	  &nbsp;49<br />
31	&nbsp;41	&nbsp;47	&nbsp;47	&nbsp;2<br />
22	&nbsp;32	&nbsp;13	&nbsp;33	&nbsp;12<br />
35	&nbsp;8	  &nbsp;38	&nbsp;32	&nbsp;45<br />
18	&nbsp;48	&nbsp;28	&nbsp;45	&nbsp;31<br />

A host (or computer) will call out unique random numbers between 1-50. A player is supposed to cross off all instances of the called out number from his set of cards. If a player crosses off all numbers in a row, column or diagonal. He wins. 

## Functionality:
  1.	Player will be dealt set of cards (randomly between 1-50)
  2.	Host will keep calling out numbers. (randomly between 1-50)
  3.	Player must cross off the numbers from his cards. And if he crosses out a complete row, column or diagonal he wins the game.
  4.	All moves by the host must be stored to validate the winner. 

## Entities:
  1. CardSet: A set of cards to be dealt to every player in the game.
  2. Player: User who is playing.
  3. BingoGame: The game dictates the rules for dealing cards and winning the game.
 
## Expectations:
  1. Code should be functionally correct, even if it is not logical optimal.
  2. Code should be modular and readable.
  3. Code should be able to incorporate incoming requirements or changes.
