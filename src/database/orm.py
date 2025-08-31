from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

from schema.request import CreateToDoRequest

Base = declarative_base()
# Base 클래스를 상속 받아서 데이터베이스 테이블을 클래스로 모델링

class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    # 데이터를 보기 쉽게 하기 위해서 어떤 객체가 출력되는지 보기 쉽게 하기 위해서 Python 클래스의 repr 매직 메소드 오버라이딩
    # __repr__ 매직 메소드: 파이썬 객체를 문자열로 표현할 때 호출되는 특수 메소드
    # 기본적으로는 <클래스이름 object at 메모리주소> 형태의 다소 불친절한 문자열을 반환
    # 단순히 “메모리 주소”만 보여주는 기본 출력 대신, 객체의 중요한 속성을 드러내는 표현으로 바꾸기 위해 오버라이드
    def __repr__(self):
        return f"ToDo(id={self.id}, contents='{self.contents}', is_done={self.is_done})"
    # f-string: 문자열 안에서 변수나 표현식을 간결하게 삽입할 수 있는 문법
    # 문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수나 수식 작성
    # javascript의 템플릿 리터럴(``백틱 + ${})와 비슷

    @classmethod
    def create(cls, request: CreateToDoRequest) -> "ToDo":
        return cls(
            contents=request.contents,
            is_done=request.is_done,
        )