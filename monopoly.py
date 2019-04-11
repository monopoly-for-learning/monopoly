class Space:
    def __init__(self, name=None):
        self.name = name

    def action(self):
        pass

    
class NoActionSpace(Space):
    def __init__(self, name):
        super().__init__(name=name)


class GoToJail(Space):
    def __init__(self, name):
        super().__init__(self, name="GoToJail")
        
    def action(self, player):
        player.go_to_jail()


class Player:
    def __init__(self,board):
       self.board = board
       self.position = board.spaces[0]
       self.jail = 0
       self.cash = 1500

    def go_to_jail():
       self.position = self.board.jail_space
       self.jail = 3
       

    def _balance(self, amount):
        self.cash += amount
#This is my attempt to make the change you mentioned about ther being a destination added to player.pay
    def pay(self,amount, destination):
        self._balance(amount * -1)
        destination += amount
#This is the method for the playing being able to recieve money. I'm not sure if we'll ever use it
    def recieve(self,amount):
        self._balance(amount)

    

class Board:
    def __init__(self, jail_space):
        self.jail_space = NoActionSpace("Jail")
        self.spaces = [NoActionSpace("Go"),self.jail_space, NoActionSpace("Free Parking"), GoToJail()]


class CardSpace(Space):
    def __init__(self, deck=deck, **kwargs):
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

class TaxSpace(Space):
    def __init__(self, amount=0, **kwargs):
        super().__init__(self,**kwargs)
        self.amount = amount

    def action(self, player):
        self.player.pay(self.amount)

class IncomeTax(TaxSpace):
    def __init__(self):
        super().__init__(name="Income Tax", amount = 200)

        
class LuxuryTax(TaxSpace):
    def __init__(self):
        super().__init__(name="Luxury Tax", amount = 75)

#This is my first stab at making the property classes on my own

"""
I think i was trying to hard to think about the logic of the space. Because you know a lot can happen when you
land on a space. From it asking you to buy it to you paying regular rent vs monopoly rent vs houses and stuff
but i think the logic of all the different posibilities is what i'll write when i make the game itself
for the time being i just need all the possibilities to be accounted for within the class
"""        

class property(space):
    def __init__(self, price, rent, mortgage_amount, unmortgage_amount, **kwargs):
        super().__init__(self,**kwargs)
        self.price = price
        self.rent = rent
        self.mortage_amount = mortgage_amount
        self.unmortgage_amount = mortgage_amount
        self.mortgage_status = False
        self.owner = None


    if mortage_status = True:
        rent = 0

    def buy_property(player, price):
        self.player.cash -= price
        self.owner = player.name
"""
I'm wondering if setting owner to be player name would be what i want here. Like is it just a cosmetic change?
So in the future when someone lands there and i make a player.pay statment for the victim player
and i pass in the victims name and rent amount and then when i try to pass in owner as the perameter for
destination of course it can't send the funds to player.name it needs to go to player.cash
i'm wonder if need to set owner = player.cash or if there's more python statement. I don't think i can make
owner just player on it's own, can i? Please let me know. 
"""        
        
    def offer_property(name, description, price):
        #we need to display the description of the property here. That's why i created that property
        answer = input(f"would you like to buy {name}. for {price}.? Type y or n")
        #I looked into how to actually create a yes or no button briefly
        #It looks like that's does with tinker but i'm not sure we're going down that path
        if answer = 'y':
            self.player.buy_property()
            print(f'you have paid {price} for {name}')
        #At this point i'm wondering how we're going to address our players. Will we let them pick names?
        #Or will they be named the piece they select? Probably the latter.
        #This code will be updated later

    if owned_status == None:
        self.player.offer_property().action()

    def mortgage_property(mortgage_amount, player):
        self.player.recieve(mortgage_amount)
        #Do i need to keep including self here? I already said self.mortage_status = mortage_status        
        mortgage_status = True

    def unmortage_property(unmortgage_amount, player):
        self.player.pay(unmortgage_amounnt)
        mortgage_status = False
        
        
        

        
        
