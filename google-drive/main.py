from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from repository.google_api_conn import GoogleApiConn

class Master(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class App(MDApp):
    
    def build(self):
        self.conn = GoogleApiConn()
        Builder.load_file('view/master.kv')
        return Master()

if __name__ == '__main__':
    App().run()
