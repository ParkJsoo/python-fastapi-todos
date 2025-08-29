from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# Base 클래스를 상속 받아서 데이터베이스 테이블을 클래스로 모델링

class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    # 데이터를 보기 쉽게 하기 위해서 어떤 객체가 출력되는지 보기 쉽게 하기 위해서 Python 클래스의 repr 매직 메소드 오버라이딩
    def __repr__(self):
        return f"ToDo(id={self.id}, contents='{self.contents}', is_done={self.is_done})"
    # f-string: 문자열 안에서 변수나 표현식을 간결하게 삽입할 수 있는 문법
    # 문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수나 수식 작성
    # javascript의 템플릿 리터럴(``백틱 + ${})와 비슷