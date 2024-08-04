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
            
        return Master()
    
    def on_stop(self):
        self.kanban_controller.persist_data()
        
if __name__ == '__main__':
    Main().run()
