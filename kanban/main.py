from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from datetime import date

from controller.kanbanController import KanbanController
from model.taskStateEnum import TaskStateEnum


class Master(TabbedPanel):

    Builder.load_file('./view/master.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class Main(App):
    def build(self):
        self.kanban_controller = KanbanController()
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )
        self.kanban_controller.add_item(
            title='Implementar login',
            created_at=date(2024, 7, 30),
            due_date=date(2024, 8, 15),
            state="todo"
        )

        self.kanban_controller.add_item(
            title='Design do dashboard',
            created_at=date(2024, 7, 25),
            due_date=date(2024, 8, 1),
            state="doing"
        )

        self.kanban_controller.add_item(
            title='Testar API',
            created_at=date(2024, 7, 20),
            due_date=date(2024, 7, 30),
            state="done"
        )
            
        return Master()

if __name__ == '__main__':
    Main().run()
