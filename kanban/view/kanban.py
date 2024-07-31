from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

from model.kanbanItem import KanbanItem

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

        self.height = len(kanban_controller.items) * 100

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

class KanbanCard(BoxLayout):
    def __init__(self, kanban_item: KanbanItem, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.size_hint_y = None
        self.height = 100

        title = Label(text=kanban_item.title)
        created_at = Label(text=str(kanban_item.created_at))
        due_date = Label(text=str(kanban_item.due_date))

        self.add_widget(title)
        self.add_widget(created_at)
        self.add_widget(due_date)