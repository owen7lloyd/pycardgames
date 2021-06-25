from random import shuffle


class Card:
    def __init__(self, rank_idx, suit_idx):
        self.suit = suit_idx
        self.rank = rank_idx
        self.suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        self.ranks = [
            None,
            None,
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'Jack',
            'Queen',
            'King',
            'Ace',
        ]

    def __lt__(self, card):
        return self.rank < card.rank

    def __gt__(self, card):
        return self.rank > card.rank

    def __eq__(self, card):
        return self.rank == card.rank

    def __repr__(self):
        return f'{self.ranks[self.rank]} of {self.suits[self.suit]}'


class Deck:
    def __init__(self):
        self.cards = []
        for rank in range(2, 15):
            for suit in range(4):
                self.cards.append(Card(rank, suit))

    def draw(self):
        if len(self.cards) == 0:
            print('There are no cards left in the deck!')
            return
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.score = 0
        self.wins = 0
        self.card: Card
        self.hand: [Card]
        self.name = name

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

    def __repr__(self):
        return self.name.capitalize()


def win_round(winner):
    winner.score += 1
    print(f'{winner} won this round.')


def draw(player1, player2):
    print(f'{player1} drew {player1.card} and {player2} drew {player2.card}')


def winner(player1, player2):
    if player1 > player2:
        player1.wins += 1
        return player1.name
    elif player1 < player2:
        player2.wins += 1
        return player2.name
    else:
        return 'It was a tie so no one'


class Game:
    def __init__(self):
        self.player1 = Player(input('Enter the name of player 1: '))
        self.player2 = Player(input('Enter the name of player 2: '))
        self.deck = Deck()

    def war(self):
        print('Beginning war!')
        self.deck.shuffle()
        while len(self.deck.cards) > 1:
            response = input('Press q to quit and any key to start ')
            if response == 'q':
                break
            self.player1.card = self.deck.draw()
            self.player2.card = self.deck.draw()
            draw(self.player1, self.player2)
            if self.player1.card > self.player2.card:
                win_round(self.player1)
            else:
                win_round(self.player2)

        print(f'War is over. {winner(self.player1, self.player2)} wins!')

    def reset(self):
        self.player1.score = 0
        self.player2.score = 0
        self.deck = Deck()
