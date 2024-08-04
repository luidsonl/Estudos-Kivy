import re
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from datetime import datetime
from kivy.uix.button import Button
from kivy.event import EventDispatcher

from model.kanbanItem import KanbanItem
from model.taskStateEnum import TaskStateEnum

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

class KanbanCard(BoxLayout):
    def __init__(self, kanban_item: KanbanItem, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.size_hint_y = None
        self.height = 100
        self.id = kanban_item.id
        self.state = kanban_item.state

        title = Label(text = kanban_item.title)
        created_at = Label(text =f"start: {kanban_item.created_at.strftime('%Y-%m-%d')}")
        due_date = Label(text = f"due: {kanban_item.due_date.strftime('%Y-%m-%d')}")
        switch_button = ActionArea(self.id, self.state)


        self.add_widget(title)
        self.add_widget(created_at)
        self.add_widget(due_date)
        self.add_widget(switch_button)

class ActionArea(GridLayout):
    def __init__(self, id:int, state: TaskStateEnum, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        to_left_button = Button(text='<')
        to_right_button = Button(text='>')
        delete_button = Button(text='X')
        delete_button.bind(on_press=lambda f: self.remove_card(id=id))

        if state == 'todo':
            self.add_widget(delete_button)
            to_right_button.bind(on_press=lambda f: self.update_state(id=id, new_state='doing'))
            self.add_widget(to_right_button)
        
        elif state == 'doing':
            to_left_button.bind(on_press=lambda f: self.update_state(id=id, new_state='todo'))
            self.add_widget(to_left_button)

            self.add_widget(delete_button)

            to_right_button.bind(on_press=lambda f: self.update_state(id=id, new_state='done'))
            self.add_widget(to_right_button)
        
        elif state == 'done':
            to_left_button.bind(on_press=lambda f: self.update_state(id=id, new_state='doing'))
            self.add_widget(to_left_button)

            self.add_widget(delete_button)


    def update_state(self, id: int, new_state: TaskStateEnum):

        app = App.get_running_app()
        kanban_controller = app.kanban_controller
        kanban_controller.edit_item_state(id, new_state)
        app.root.ids.kanban_content.update_kanban()

    def remove_card(self, id: int):
        app = App.get_running_app()
        kanban_controller = app.kanban_controller
        kanban_controller.remove_item(id)
        app.root.ids.kanban_content.update_kanban()



class NewKanbanForm(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'New task'
        
        layout = BoxLayout(orientation='vertical')
        
        self.title_input = TextInput(hint_text='Title')
        layout.add_widget(self.title_input)

        layout.add_widget(Label(text='Created at'))

        self.created_at_input = DateTimeInput(hint_text='YYYY-MM-DD')
        layout.add_widget(self.created_at_input)

        layout.add_widget(Label(text='Due date'))

        self.due_date_input = DateTimeInput(hint_text='YYYY-MM-DD')
        layout.add_widget(self.due_date_input)
        
        
        submit_button = Button(text='create')
        submit_button.bind(on_press=self.submit_new_kanban_form)
        
        layout.add_widget(submit_button)
        
        self.add_widget(layout)

    def submit_new_kanban_form(self, instance):
        title = self.title_input.text
        created_at = datetime.strptime(self.created_at_input.text, "%Y-%m-%d")
        due_date = datetime.strptime(self.due_date_input.text, "%Y-%m-%d")

        app = App.get_running_app()

        kanban_controller = app.kanban_controller

        kanban_controller.add_item(title, created_at, due_date, 'todo')

        app.root.ids.kanban_content.update_kanban()

        
        self.dismiss()


class DateTimeInput(TextInput):
    def __init__(self, **kwargs):
        if 'text' not in kwargs:
            kwargs['text'] = datetime.now().strftime("%Y-%m-%d")
        super(DateTimeInput, self).__init__(**kwargs)
        self.bind(focus=self.on_focus)
        self.text

    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() or substring in "- ":
            new_text = self.text + substring
            new_text = self.format_input(new_text)
            if len(new_text) <= 10:
                self.text = new_text
                self.cursor = (len(self.text), 0)

    def format_input(self, text):
        text = re.sub(r'[^\d]', '', text)
        formatted = ''
        
        if len(text) > 4:
            formatted += text[:4] + '-'
            text = text[4:]
        else:
            return text

        if len(text) > 2:
            formatted += text[:2] + '-'
            text = text[2:]
        else:
            return formatted + text

        return formatted + text

    def format_date(self, text):
        text = ''.join(filter(str.isdigit, text))
        DEFAULT_DATE = datetime.today()

        defaults = {
            'year': '2024',
            'month': '01',
            'day': '01'
        }
        
        year = text[:4].rjust(4, '0') or defaults['year']
        month = text[4:6].rjust(2, '0') or defaults['month']
        day = text[6:8].rjust(2, '0') or defaults['day']

        try:
            date = datetime(int(year), int(month), int(day))
        except ValueError:
            date = DEFAULT_DATE

        formatted = date.strftime("%Y-%m-%d")
        
        return formatted

    def validate_and_correct_date(self):
        text = self.format_date(self.text)

        text = text.replace(' ', 'T')
        year, month, day = int(text[:4]), int(text[5:7]), int(text[8:10])

        if day < 1:
            day = 1
        
        if month > 12:
            month = 12
        elif month < 1:
            month = 1
        
        if month == 2:
            if day > 29:
                day = 29
            elif day > 28:
                if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    day = 29
                else:
                    day = 28
        else:
            days_in_month = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
            if day > days_in_month[month - 1]:
                day = days_in_month[month - 1]

        formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
        
        self.text = formatted_date

    def on_focus(self, instance, value):
        if value == False:
            corrected_date = self.validate_and_correct_date()
            if corrected_date:
                self.text = corrected_date