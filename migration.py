from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///moru_blog.db', echo=True)
Base = declarative_base()

def main():
    Base.metadata.create_all(engine)
    print('tables created')


if __name__ == "__main__":
    main()