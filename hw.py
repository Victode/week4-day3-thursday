import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}




class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0   
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def set_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Game:
    def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.set_ace()


    def hit_or_stand(deck,hand):
        
        while True:
            query= input("Would you like to Hit or Stand?\n'h' or 's'")
            
            if query.lower() == 'h':
                hit= (deck,hand)  

            elif query.lower() == 's':
                playing = False
            else:
                print("Sorry, please try again.")
                continue
            break


    def show_some(player,dealer):
        print("\nDealer's Hand")
        print("<card hidden>")
        print(dealer.cards[1])
        print("\nPlayer's Hand: ", *player.cards)
            
    def show_all(player,dealer):
        print("\nDealer's Hand:", *dealer.cards)
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand: ", *player.cards)
        print("Player's Hand = ", player.value)



    def player_busts(player,dealer):
        print("Player busts! You lose!")

    def player_wins(player,dealer):
        print("Player wins! Well done!")


    def dealer_busts(player,dealer):
        print("Dealer busts! You win!")
        
    def dealer_wins(player,dealer):
        print("Dealer wins! You lose!")
        
    def push(player,dealer):
        print("Dealer and Player tie!")    

    while True:
        print("Let's play a game.")
        
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        show_some(player_hand, dealer_hand)
        
    
            
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand,dealer_hand) 
        
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand)

            break

        if player_hand.value <= 21:
            
            while dealer_hand.value <17:
                hit(deck, dealer_hand)
        
            show_all(player_hand,dealer_hand)
            
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand)

            else:
                push(player_hand,dealer_hand)
            
        

        
        new_game = input("Play again?\n'y' or 'n'  ")
        if new_game.lower() == 'y':
            playing = True
            continue
        elif new_game.lower() == 'n':
            print('Thanks for playing! ')
            break
        else:
            print("Sorry, please try again.")   