from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

class Master(TabbedPanel):
    Builder.load_file('./view/master.kv')
    Builder.load_file('./view/kanban.kv')
    Builder.load_file('./view/calendar.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Main(App):
    def build(self):
        return Master()

if __name__ == '__main__':
    Main().run()
