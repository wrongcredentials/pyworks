#Python Homework 3
#Задание №1

#Задание №2
import random

class CardDeck:
	def __init__(self):
		self.value = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
		self.suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
		self.cards = []
		self.first_card = ""
	
	def deck_create(self):
		for suit in self.suit:
			for value in self.value:
				new_card = [value, suit]
				self.cards.append(new_card)
		return self.cards

	def deck_shuffle(self):
		random.shuffle(self.cards)
		return self.cards

	def deck_pop(self):
		self.first_card = self.cards[0]
		self.cards = self.cards[1:]
		return self.first_card

	def card_suite(self):
		return self.first_card[1]

	def card_value(self):
		return self.first_card[0]


deck = CardDeck()
deck.deck_create()
deck.deck_shuffle()
for i in range(5):
	deck.deck_pop()
	print("Suite: ", deck.card_suite())
	print("Value: ", deck.card_value())


