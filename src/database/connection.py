from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:todos@127.0.0.1:3306/todos"

engine = create_engine(DATABASE_URL, echo=True)
# echo=True: 쿼리가 대신 처리될 때 어떤 SQL이 사용되었는지 사용되는 시점에 SQL을 출력해주는 옵션
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionFactory()

    try:
        yield session
    finally:
        session.close()