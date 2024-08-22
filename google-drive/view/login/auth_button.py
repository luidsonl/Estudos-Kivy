import webbrowser
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from repository.google_api_conn import GoogleApiConn

class AuthButton(MDRaisedButton):
    conn: GoogleApiConn = MDApp.get_running_app().conn

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Autenticar'
        self.on_release = self.handle_click

        self.pos_hint = {'center_x': 0.5} 
        self.size_hint = (None, None)

    def handle_click(self):
        if self.conn.auth_url:
            print(self.conn.auth_url)
            webbrowser.open(self.conn.auth_url)
        else:
            self.conn.authenticate()
