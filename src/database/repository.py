from typing import List # 스탠다드 라이브러리에서 타입 힌트를 위한 부분을 지원

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.orm import ToDo

def get_todos(session: Session) -> List[ToDo]:
    return list(session.scalars(select(ToDo))) # 젠체 ToDo를 조회해서 return

def get_todo_by_todo_id(session: Session, todo_id: int) -> ToDo | None:
    return session.scalar(select(ToDo).where(ToDo.id == todo_id))

def create_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo) # 생성안 ORM 객체를 Session Object에 추가
    session.commit() # 데이터베이스에 저장, id 할당
    session.refresh(instance=todo) # 데이터베이스에서 데이터 읽음, todo_id 결정 및 반영

    return todo

def update_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo)
    session.commit()
    session.refresh(instance=todo)

    return todo