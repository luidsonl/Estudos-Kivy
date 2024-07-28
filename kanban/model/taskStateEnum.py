from enum import Enum, auto

class TaskStateEnum(Enum):
    todo = auto()
    doing = auto()
    done = auto()