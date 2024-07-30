from datetime import date
from model.kanbanItem import KanbanItem
from model.taskStateEnum import TaskStateEnum

from kivy.uix.tabbedpanel import TabbedPanel


class KanbanController:
    def __init__(self):
        self.items = []

    def add_item(self, title: str, created_at :date, due_date: date, state: TaskStateEnum):
        item = KanbanItem(title, created_at, due_date, state)
        self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]

    def edit_item_state(self, item_id: int, new_state: TaskStateEnum):

        for item in self.items:
            if item.id == item_id:
                item.state = new_state
                break
    
