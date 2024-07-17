from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class Calc(BoxLayout):
    Builder.load_file('./screens/Calc.kv')

    def clear(self):
        self.ids.calc_input.text = '0'