from datetime import date
from model.kanbanCard import KanbanCard
from model.taskStateEnum import TaskStateEnum

from kivy.uix.tabbedpanel import TabbedPanel


class KanbanController:
    def __init__(self):
        self.cards = []

    def add_card(self, title: str, created_at :date, due_date: date, state: TaskStateEnum):
        card = KanbanCard(title, created_at, due_date, state)
        self.cards.append(card)

    def remove_card(self, card_id: int):
        self.cards = [card for card in self.cards if card.id != card_id]

    def edit_card_state(self, card_id: int, new_state: TaskStateEnum):

        for card in self.cards:
            if card.id == card_id:
                card.state = new_state
                break
    
