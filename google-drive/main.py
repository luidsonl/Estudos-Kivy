from kivymd.app import MDApp
from repository.google_api_conn import GoogleApiConn
from view.master import Master

        

class App(MDApp):
    
    def build(self):
        self.conn = GoogleApiConn()
        return Master()
    
    def reload_app(self):
        self.root.clear_widgets()
        self.root.add_widget(self.build())

if __name__ == '__main__':
    App().run()
