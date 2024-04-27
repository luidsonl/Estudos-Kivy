from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label


class ScrollableFormArea(ScrollView):
    def __init__(self, update_params: callable , **kwargs):
        super().__init__(**kwargs)

        self.update_params = update_params
        self.counter = 0

        self.scroll_content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)

        self.scroll_content.bind(minimum_height=self.scroll_content.setter('height'))

        self.increment_button = Button(text='+', size_hint=(None, None), height=40, width=40)
        self.increment_button.bind(on_press=self.add_input)

        self.add_widget(self.scroll_content)

        self.scroll_content.add_widget(self.increment_button)
    
    def add_input(self, instance):
        input_row = InputRow(index=self.counter, update_params=self.update_params)
        self.scroll_content.add_widget(input_row)
        self.counter += 1


class InputRow(GridLayout):
    def __init__(self, update_params:callable , index: int, **kwargs):
        super().__init__(**kwargs)
        
        self.update_params = update_params
        self.index = index

        self.cols = 4
        self.size_hint_y = None
        self.height = 50
        self.padding = [0, 0, 50, 20]

        self.add_widget(Label(
            text='Substituir'
        ))

        self.key_field = TextInput(height=40)
        self.add_widget(self.key_field)

        self.add_widget(Label(
            text='Por'
        ))

        self.value_field = TextInput(height=40)
        self.add_widget(self.value_field)

        self.key_field.bind(text=self.update_key)
        self.value_field.bind(text=self.update_value)


    def update_key(self, instance, value):
        self.update_params(index=self.index, key='key',value=value)

    def update_value(self, instance, value):
        self.update_params(index=self.index, key='value',value=value)


