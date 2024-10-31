import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw5 import Patient, Card, Deck, Triangle, Rectangle, Circle



def test_patient_add_test():
    patient = Patient("John Doe", ["fever", "cough"])
    patient.add_test("covid", True)
    assert patient.tests["covid"] is True

def test_patient_has_covid_with_test():
    patient = Patient("Jane Doe", [])
    patient.add_test("covid", True)
    assert patient.has_covid() == 0.99

def test_patient_has_covid_without_test():
    patient = Patient("Jane Doe", ["fever", "cough"])
    assert patient.has_covid() == 0.25  # 0.05 + 0.1 (fever) + 0.1 (cough)


def test_card_initialization():
    card = Card("Hearts", "A")
    assert card.suit == "Hearts"
    assert card.value == "A"

def test_deck_initialization():
    deck = Deck()
    assert len(deck.cards) == 52  

def test_deck_shuffle():
    deck = Deck()
    first_card = deck.cards[0]
    deck.shuffle()
    assert first_card != deck.cards[0] or deck.cards != Deck().cards

def test_deck_draw():
    deck = Deck()
    card = deck.draw()
    assert len(deck.cards) == 51  
    assert isinstance(card, Card)


# 测试 PlaneFigure 的子类 Triangle
def test_triangle_perimeter():
    triangle = Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_perimeter() == 12  # 3 + 4 + 5

def test_triangle_surface():
    triangle = Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_surface() == 3.0  # 0.5 * 3 * 2



def test_rectangle_perimeter():
    rectangle = Rectangle(a=3, b=4)
    assert rectangle.compute_perimeter() == 14  # 2 * (3 + 4)

def test_rectangle_surface():
    rectangle = Rectangle(a=3, b=4)
    assert rectangle.compute_surface() == 12  # 3 * 4


# 测试 PlaneFigure 的子类 Circle
def test_circle_perimeter():
    circle = Circle(radius=5)
    assert round(circle.compute_perimeter(), 2) == 31.42  # 2 * pi * 5,

def test_circle_surface():
    circle = Circle(radius=5)
    assert round(circle.compute_surface(), 2) == 78.54  # pi * 5^2
