from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class TextInputArea(GridLayout):
    def __init__(self, update_input_text: callable, **kwargs):
        super().__init__(**kwargs)
        self.update_input_text = update_input_text

        self.cols = 1

        self.text_input = TextInput(hint_text="Insira aqui o texto a ser substituído")

        self.text_input.bind(text=self.on_text_changed)
        self.add_widget(self.text_input)



    def on_text_changed(self, instance, value):
        self.update_input_text(value)



