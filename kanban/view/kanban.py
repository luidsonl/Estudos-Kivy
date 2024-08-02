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

        new_kanban_button = Button(text="New Task", size_hint_y = None, height = 100)
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

        title = Label(text=kanban_item.title)
        created_at = Label(text=str(kanban_item.created_at))
        due_date = Label(text=str(kanban_item.due_date))

        self.add_widget(title)
        self.add_widget(created_at)
        self.add_widget(due_date)


class NewKanbanForm(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'New task'
        self.id = 'new_kanban_form'
        
        layout = BoxLayout(orientation='vertical')
        
        self.title_input = TextInput(hint_text='Title')
        layout.add_widget(self.title_input)

        self.created_at_input = DateTimeInput(hint_text='YYYY-MM-DD')
        layout.add_widget(self.created_at_input)

        self.due_date_input = DateTimeInput(hint_text='YYYY-MM-DD')
        layout.add_widget(self.due_date_input)
        
        
        submit_button = Button(text='create')
        submit_button.bind(on_press=self.submit_new_kanban_form)
        
        layout.add_widget(submit_button)
        
        self.add_widget(layout)

    def submit_new_kanban_form(self, instance):
        title = self.title_input.text
        created_at = self.created_at_input.text
        due_date = self.due_date_input.text

        print(f'title: {title}, created {created_at}, due {due_date}')
        
        self.dismiss()


class DateTimeInput(TextInput):
    def __init__(self, **kwargs):
        super(DateTimeInput, self).__init__(**kwargs)
        self.bind(focus=self.on_focus)

    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() or substring in "- ":
            new_text = self.text + substring
            new_text = self.format_input(new_text)
            if len(new_text) <= 10:  # Limita o comprimento da entrada para a data
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
        # Filtra apenas dígitos do texto
        text = ''.join(filter(str.isdigit, text))

        # Define os valores padrão
        defaults = {
            'year': '1000',
            'month': '01',
            'day': '01'
        }
        
        # Divide o texto em partes
        year = text[:4].rjust(4, '0') or defaults['year']
        month = text[4:6].rjust(2, '0') or defaults['month']
        day = text[6:8].rjust(2, '0') or defaults['day']

        # Formata a data
        formatted = f"{year}-{month}-{day}"
        
        return formatted

    def validate_and_correct_date(self):
        text = self.format_date(self.text)

        text = text.replace(' ', 'T')
        year, month, day = int(text[:4]), int(text[5:7]), int(text[8:10])
        
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