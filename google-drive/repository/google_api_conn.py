import os.path
import threading
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.exceptions import RefreshError

# Se modificar esses escopos, exclua o arquivo token.json.
SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly", 
    "https://www.googleapis.com/auth/drive.file" 
]

class GoogleApiConn:
    def __init__(self, initial_folder_id=None):
        self.creds = None
        self.initial_folder_id = initial_folder_id
        self.auth_url = ''

    def authenticate(self):
        token_path = "credentials/token.json"
        secrets_path = "credentials/secrets.json"

        if os.path.exists(token_path):
            self.creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
        if not self.creds or not self.creds.valid:
            auth_thread = threading.Thread(target=self._authenticate, args=(secrets_path, token_path), daemon=True)
            auth_thread.start()

    def _authenticate(self, secrets_path, token_path):
        if self.creds and self.creds.expired and self.creds.refresh_token:
            try:
                self.creds.refresh(Request())
            except RefreshError:
                self._initiate_auth_flow(secrets_path, token_path)
        else:
            self._initiate_auth_flow(secrets_path, token_path)

    def _initiate_auth_flow(self, secrets_path, token_path):
        flow = InstalledAppFlow.from_client_secrets_file(secrets_path, SCOPES)
        self.auth_url, _ = flow.authorization_url()
        self.creds = flow.run_local_server(port=0)
        with open(token_path, "w") as token:
            token.write(self.creds.to_json())


    def list_files(self, folder_id=None):
        """Retorna a lista de arquivos no diretório especificado ou no diretório raiz."""

        if self.initial_folder_id and not folder_id:
            folder_id = self.initial_folder_id

        try:
            service = build("drive", "v3", credentials=self.creds)
            
            query = f"'{folder_id}' in parents" if folder_id else "'root' in parents"
            
            results = (
                service.files()
                .list(q=query, pageSize=10, fields="nextPageToken, files(id, name)")
                .execute()
            )
            items = results.get("files", [])

            return items
        
        except HttpError as error:
            print(f"An error occurred: {error}")
