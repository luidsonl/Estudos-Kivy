from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from repository.google_api_conn import GoogleApiConn

class DriveViewer(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class DriveApp(MDApp):
    def build(self):
        return DriveViewer()

if __name__ == '__main__':
    google_api_conn = GoogleApiConn()
    google_api_conn.authenticate()
    google_api_conn.list_files()

    DriveApp().run()
