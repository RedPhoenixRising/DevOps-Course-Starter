from todo_app.data.card import Card
import json

class List:
    def __init__(self, json_input):
        self.cards = []
        self.raw_cards = json_input['cards']
        self.name = json_input['name']
        self.id = json_input['id']
        self.init_cards(self.raw_cards)

    def init_cards(self, json_input):
        for card in json_input:
            new_card = Card.from_json_input(card, self.name, self.id)
            self.cards.append(new_card)

    def get_cards(self):
        return self.cards

    def print(self):
        num_cards_in_list = len(self.cards)
        print("List")
        print(f"List Name: {self.name}")
        print(f"List ID: {self.id}")
        print(f"List contains {num_cards_in_list} cards\n\n")

        for card in self.cards:
            card.print()

