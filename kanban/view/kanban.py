import re
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button

from view.kanbanCard import KanbanCard, NewKanbanForm



class Kanban(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (1, 1)
        self.do_scroll_x = False
        self.do_scroll_y = True
        self.padding = [10, 30, 10, 10]

        

class KanbanBody(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.size_hint_y = None

        kanban_controller = App.get_running_app().kanban_controller

        self.height = len(kanban_controller.items) * 100 + 50

class KanbanHeader(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.spacing = 10
        self.size_hint_y = None
        self.height = 50

class KanbanContent(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.spacing = 10
        self.size_hint_y = None
        self.height = self.minimum_height


    def update_kanban(self):
        self.clear_widgets()
        
        self.add_widget(KanbanToDo())
        self.add_widget(KanbanDoing())
        self.add_widget(KanbanDone())
        

class KanbanToDo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 10
        

        kanban_controller = App.get_running_app().kanban_controller

        for item in kanban_controller.items:
            if item.state == 'todo':
                card = KanbanCard(item)
                self.add_widget(card)

        new_kanban_button = Button(text="New Task", size_hint_y = None, height = 50)
        new_kanban_button.bind(on_press=self.show_popup)
        self.add_widget(new_kanban_button)

    def show_popup(self, instance):
        popup = NewKanbanForm(size_hint=(None, None), size=(400, 400))
        popup.open()


class KanbanDoing(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 10

        kanban_controller = App.get_running_app().kanban_controller

        for item in kanban_controller.items:
            if item.state == 'doing':
                card = KanbanCard(item)
                self.add_widget(card)



class KanbanDone(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 10

        kanban_controller = App.get_running_app().kanban_controller

        for item in kanban_controller.items:
            if item.state == 'done':
                card = KanbanCard(item)
                self.add_widget(card)

