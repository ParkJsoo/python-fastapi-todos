from typing import List # 스탠다드 라이브러리에서 타입 힌트를 위한 부분을 지원

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.orm import ToDo

def get_todos(session: Session) -> List[ToDo]:
    return list(session.scalars(select(ToDo))) # 젠체 ToDo를 조회해서 return

def get_todo_by_todo_id(session: Session, todo_id: int) -> ToDo | None:
    return session.scalar(select(ToDo).where(ToDo.id == todo_id))