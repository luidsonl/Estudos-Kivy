from kivy.uix.button import Button

class CalcKey(Button):
     def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.size_hint = (0.2 ,0.2)
        self.font_size = 32