from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from datetime import date

from controller.kanbanController import KanbanController


class Master(TabbedPanel):

    Builder.load_file('./view/master.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        kanban_controller = KanbanController()


class Main(App):
    def build(self):
            
        return Master()

if __name__ == '__main__':
    Main().run()
