from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

from view.file_list_screen.file_list_screen import FileListScreen

from repository.google_api_conn import GoogleApiConn
from view.login_screen.login_screen import LoginScreen

class Master(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn: GoogleApiConn = MDApp.get_running_app().conn

        if self.conn.authenticated:
            self.add_widget(FileListScreen())
        
        else:
            self.add_widget(LoginScreen())
