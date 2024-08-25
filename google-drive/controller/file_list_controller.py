from kivymd.app import MDApp
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class FileListController:
    def __init__(self):
        self.creds = MDApp.get_running_app().conn.creds

    def list_files(self):
        try:
            service = build('drive', 'v3', credentials=self.creds)
            results = service.files().list(pageSize=10).execute()
            items = results.get('files', [])
            return items
        except HttpError as error:
            print(f'An error occurred: {error}')
            return []