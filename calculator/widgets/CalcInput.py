from kivy.uix.textinput import TextInput


class CalcInput(TextInput):
     def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.halign = 'right'
        self.font_size = 65
        self.size_hint = (1, 0.15)