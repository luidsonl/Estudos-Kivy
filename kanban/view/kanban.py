from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

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
        self.size_hint_y = (None)

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

class KanbanToDo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.size_hint_y = None

class KanbanDoing(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.size_hint_y = None

class KanbanDone(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.size_hint_y = None
