from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from repository.google_api_conn import GoogleApiConn
from view.login_screen.login_screen import LoginScreen

class Master(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn: GoogleApiConn = MDApp.get_running_app().conn

        if self.conn.authenticated:
            self.add_widget(MDLabel(text="autenticado"))
        
        else:
            self.add_widget(LoginScreen())
