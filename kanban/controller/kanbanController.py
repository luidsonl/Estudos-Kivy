import datetime
from model.kanbanItem import KanbanItem
from model.taskStateEnum import TaskStateEnum
import pandas as pd



class KanbanController:
    def __init__(self):
        self.items = []
        self.load_data()


    def persist_data(self):
        obj_list = [{'id': item.id, 'title': item.title, 'created_at': item.created_at, 'due_date': item.due_date, 'state': item.state} for item in self.items]

        df = pd.DataFrame(obj_list)
        df.to_excel('db/db.xlsx', index=None)

    def load_data(self):
        try:
            df = pd.read_excel('db/db.xlsx')

            for _, row in df.iterrows():
                title = row['title']
                created_at = row['created_at'].to_pydatetime()
                due_date = row['due_date'].to_pydatetime()
                state = row['state']
                
                self.add_item(title=title, created_at=created_at, due_date=due_date, state=state)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def add_item(self, title: str, created_at :datetime.date, due_date: datetime.date, state: TaskStateEnum):
        item = KanbanItem(title, created_at, due_date, state)
        self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]

    def edit_item_state(self, item_id: int, new_state: TaskStateEnum):

        for item in self.items:
            if item.id == item_id:
                item.state = new_state
                break
    
