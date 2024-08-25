from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView

from controller.file_list_controller import FileListController 


class FileListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = FileListController()

        self.populate_file_list()

    def populate_file_list(self):
        file_list = self.controller.list_files()
        scroll_view = MDScrollView()
        list_view = MDList()

        for file in file_list:
            item = OneLineListItem(text=file['name'])
            list_view.add_widget(item)
        
        scroll_view.add_widget(list_view)
        self.add_widget(scroll_view)

class App(MDApp):
    def build(self):
        return FileListScreen()

if __name__ == '__main__':
    App().run()
