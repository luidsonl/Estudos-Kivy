from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from widgets.Calc import Calc


Window.size = (500,700)


class Main(App):
    def build(self):
        return Calc()

if __name__ == '__main__':
    Main().run()