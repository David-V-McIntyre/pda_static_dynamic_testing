import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.seven_of_hearts = Card("hearts", 7)
        self.eight_of_hearts = Card("hearts", 8)
        self.nine_of_hearts = Card("hearts", 9)
        self.ten_of_hearts = Card("hearts", 10)
        self.jack_of_hearts = Card("hearts", 11)
        self.queen_of_hearts = Card("hearts", 12)
        self.king_of_hearts = Card("hearts", 13)
        self.ace_of_diamonds = Card("hearts", 1)
        self.queen_of_spades = Card("spades", 12)
        self.two_of_clubs = Card("hearts", 2)

    def test_card_has_suite(self):
        self.assertEqual("hearts", self.seven_of_hearts.suit)

    def test_card_has_value(self):
        self.assertEqual(12, self.queen_of_spades.value)

    def test_check_for_ace_true(self):
        ace_status = check_for_ace(self.ace_of_diamonds)
        self.assertEqual(True, ace_status)

    def test_check_for_ace_false(self):
        ace_status = check_for_ace(self.queen_of_hearts)
        self.assertEqual(False, ace_status)
    
    def test_highest_card_card2(self):
        card2_high = highest_card(self.two_of_clubs, self.queen_of_hearts)
        self.assertEqual(self.queen_of_hearts, card2_high)

    def test_highest_card_card1(self):
        card1_high = highest_card(self.jack_of_hearts, self.seven_of_hearts)
        self.assertEqual(self.jack_of_hearts, card1_high)

    def test_cards_total(self):
        cards = [self.seven_of_hearts, self.eight_of_hearts, self.queen_of_spades]
        total = cards_total(cards)
        self.assertEqual("You have a total of 27", total)

    def test_cards_total(self):
        cards = [self.two_of_clubs, self.king_of_hearts, self.seven_of_hearts]
        total = cards_total(cards)
        self.assertEqual("You have a total of 22", total)