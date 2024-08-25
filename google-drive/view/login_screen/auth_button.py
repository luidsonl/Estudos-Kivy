import webbrowser
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from repository.google_api_conn import GoogleApiConn

class AuthButton(MDRaisedButton):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn: GoogleApiConn = MDApp.get_running_app().conn

        self.text = 'Autenticar'
        self.on_release = self.handle_click

        self.pos_hint = {'center_x': 0.5} 
        self.size_hint = (None, None)

    def handle_click(self):
            self.conn.authenticate()
