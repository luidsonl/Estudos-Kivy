from datetime import date
from model.taskStateEnum import TaskStateEnum



class KanbanCard:
    id = 1
    title = ''
    created_at =''
    due_date = ''
    state = ''

    def __init__(self, title: str, created_at: date, due_date: date, state: TaskStateEnum) -> None:
        self.id = KanbanCard.id
        KanbanCard.id += 1

        self.title = title
        self.created_at = created_at
        self.due_date = due_date
        self.state = state


    