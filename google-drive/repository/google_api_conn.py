import os.path
import threading
from kivy.clock import Clock
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.exceptions import RefreshError
from kivymd.app import MDApp

SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly", 
    "https://www.googleapis.com/auth/drive.file" 
]
TOKEN_PATH = "credentials/token.json"
SECRETS_PATH = "credentials/secrets.json"

class GoogleApiConn:
    def __init__(self):
        self.creds = self._get_creds()
        self.authenticated = self._validate_token()
        

    def authenticate(self):
        if not self.authenticated:
            auth_thread = threading.Thread(target=self._initiate_auth_flow, daemon=True)
            auth_thread.start()


    
    def _validate_token(self):
        try:
            if self.creds:
                self.creds.refresh(Request())
                return True
            else:
                return False
        
        except RefreshError:
            return False
            
            
    def _get_creds(self):
        if os.path.exists(TOKEN_PATH):
            try:
                return Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
            except: return None
        else:
            return None

    def _initiate_auth_flow(self):
        flow = InstalledAppFlow.from_client_secrets_file(SECRETS_PATH, SCOPES)
        self.creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(self.creds.to_json())

            Clock.schedule_once(self._on_auth_complete, 0)

    def _on_auth_complete(self, dt):
        self.authenticated = self._validate_token()
        if self.authenticated:
            print("Autenticação concluída com sucesso!")
            MDApp.get_running_app().reload_app()
        else:
            print("Falha na autenticação!")
        
