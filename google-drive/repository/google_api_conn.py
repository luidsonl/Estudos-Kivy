import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Se modificar esses escopos, exclua o arquivo token.json.
SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly", 
    "https://www.googleapis.com/auth/drive.file" 
]

class GoogleApiConn:
    def __init__(self):
        self.creds = None

    def authenticate(self):
        """Autentica o usuário e obtém credenciais válidas."""
        # O arquivo token.json armazena o acesso e os tokens de atualização do usuário.
        # É criado automaticamente quando o fluxo de autorização é concluído pela primeira vez.
        if os.path.exists("credentials/token.json"):
            self.creds = Credentials.from_authorized_user_file("credentials/token.json", SCOPES)
        
        # Se não há credenciais (válidas), permita que o usuário faça login.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials/secrets.json", SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Salve as credenciais para a próxima execução
            with open("credentials/token.json", "w") as token:
                token.write(self.creds.to_json())
    
    def list_files(self):

        try:
            service = build("drive", "v3", credentials=self.creds)

            results = (
                service.files()
                .list(pageSize=10, fields="nextPageToken, files(id, name)")
                .execute()
            )
            items = results.get("files", [])

            if not items:
                print("No files found.")
                return
            print("Files:")
            for item in items:
                print(f"{item['name']} ({item['id']})")
        except HttpError as error:
            print(f"An error occurred: {error}")
