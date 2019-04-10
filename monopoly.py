class Space:
    def __init__(self, name=None, **kwargs):
        self.name = name

    def action(self):
        pass


class NoActionSpace(Space):
    def __init__(self, name):
        super().__init__(name=name)


class GoToJail(Space):
    def __init__(self):
        super().__init__(self, name="GoToJail")

    def action(self, player):
        player.go_to_jail()


class TaxSpace(Space):
    def __init__(self, tax=0, **kwargs):
        super().__init__(self, **kwargs)
        self.tax = tax


    def action(self, player):
        player.pay(self.tax)


class IncomeTax(TaxSpace):
    def __init__(self):
        super().__init__(name="Income Tax", tax=20)


class LuxuryTax(TaxSpace):
    def __init__(self):
        super().__init__(name="Luxury Tax", tax=75)


class CardSpace(Space):
    def __init__(self, deck=None, **kwargs):
        super().__init__(**kwargs)
        self.deck = deck

    def action(self):
        self.deck.next_card().action()


class ChanceSpace(CardSpace):
    def __init__(self):
        super().__init__(name="Chance", deck=ChanceCards)


class CommunityChestSpace(CardSpace):
    def __init__(self):
        super().__init__(name="Community Chest", deck=CommunityChestCards)


class Player:
    def __init__(self, board):
        self.board = board
        self.position = self.board.spaces[0]
        self.jail = 0
        self.cash = 1500

    def go_to_jail(self):
        self.position = self.board.jail_space
        self.jail = 3

    def _balance(self, amount):
        self.cash += amount
        # trigger money generating workflow if self.cash is < 0

    def pay(self, amount):
        self._balance(amount * -1)
        # add logic about where the money goes (to another player, to free parking, etc)




class Board:
    JAIL = NoActionSpace("Jail")
    SPACES = [NoActionSpace("Go"),
              JAIL,
              NoActionSpace("Free Parking"),
              GoToJail()
              ]

    def __init__(self):
        self.spaces = self.make_board()

    def make_board():
        return [space for space in self.SPACES]

    @property
    def jail(self):
        def return JAIL


players = [Player(board[0]), Player(board[0]), Player(board[0]), Player(board[0])]