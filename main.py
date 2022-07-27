# Prateek Balhara
# 21st July 2022
import random

MATRIX_SIZE = 5
UPPER_LIMIT_FOR_CARDS = 50
TOTAL_MOVES_BY_HOST = 10
##  Cards dealt to a Player ##
class CardSet:
    def __init__(self, cards = None):
        if not cards:
            cards = Bingo.dealCards()
        self.cards = cards

    def getCards(self):
        '''
        Getter to return cards. In case Player 1 has to show cards.
        :return: cards
        '''
        return self.cards

    def markCard(self, row, col):
        self.cards[row][col] = 0

## Player
class Player:
    def __init__(self, playerName: str):
        self.name = playerName
        self.cardSet = CardSet()

    def getName(self) -> str:
        '''
        Getter for name
        :return: name
        '''
        return self.name

    def makeMove(self, number: int):
        '''
        Player will make a move. If the number is found in the cards dealt to the player. The player will cross it off
        :param number: number called out by host
        :return: None
        '''
        for rowIndex, row in enumerate(self.cardSet.getCards()):
            for colIndex, card in enumerate(row):
                if number == card:
                    print(self.name , "number found")
                    self.cardSet.markCard(rowIndex, colIndex)

    def printCards(self):
        '''
        Print all player cards on screen
        :return: None
        '''
        print(self.getName(), " cards: ")
        for rowIndex, row in enumerate(self.cardSet.getCards()):
            for colIndex, card in enumerate(row):
                print(abs(self.cardSet.getCards()[rowIndex][colIndex]), end = "\t")
            print()

    def hasWon(self) -> bool:
        '''
        Check if the player has won the game.
        Check row, col and diagonals
        :return: True/False
        '''
        rowWon =  [True] * MATRIX_SIZE
        colWon = [True] * MATRIX_SIZE
        daigonalWon = True
        reverseDaigonalWon = True

        for rowIndex, row in enumerate(self.cardSet.getCards()):
            for colIndex, card in enumerate(row):
                if card>0:
                    if (rowWon[rowIndex] or colWon[colIndex]):
                        rowWon[rowIndex] = False
                        colWon[colIndex] = False

                    if rowIndex == colIndex:
                        daigonalWon = False

                    if (rowIndex+colIndex+1) == MATRIX_SIZE:
                        reverseDaigonalWon = False

        return any(rowWon) or any(colWon) or daigonalWon or reverseDaigonalWon

##  BINGO GAME ##
class Bingo:
    def __init__(self, players):
        self._currentMove = 0
        self.players = players
        self.moves = set()

    @staticmethod
    def dealCards():
        '''
        Deal a new set of cards
        :return: Cards
        '''
        return [[random.randint(1,UPPER_LIMIT_FOR_CARDS) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    def nextMove(self):
        '''
        return Number called out by Host
        :return: RANDOM number between 1-UPPER_LIMIT_FOR_CARDS
        '''
        self._currentMove += 1
        if self._currentMove <= TOTAL_MOVES_BY_HOST:
            move =  random.randint(1,UPPER_LIMIT_FOR_CARDS)
            # Making sure that the move is unique
            while move in self.moves:
                move = random.randint(1, UPPER_LIMIT_FOR_CARDS)
            self.moves.add(move)
            return move

    def playGame(self) -> Player:
        # host starts calling out the numbers.
        move = self.nextMove()
        while move:
            print("Host's next move: ", move)
            for player in self.players:
                player.makeMove(move)
                if player.hasWon():
                    return player

            move = self.nextMove()


if __name__ == '__main__':
    # Create Players
    player1 = Player("Player1")
    player2 = Player("Player2")
    player1.printCards()
    player2.printCards()
    # Create Game and Start Game
    winner =  Bingo([player1, player2]).playGame()
    # Print the result for winner
    if winner:
        print("Bingo!!! ",winner.getName())
    else:
        print("Nobody won! Better luck next time")