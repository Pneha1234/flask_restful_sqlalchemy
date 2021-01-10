from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///moru_blog.db', echo=True)
Base = declarative_base()

def main():
    Base.metadata.create_all(engine)
    moru_blog_connection = engine.connect()
    moru_blog_trans = moru_blog_connection.begin()
    moru_blog_connection.execute("alter table blog_model add column active boolean default True;")
    moru_blog_connection.execute("update blog_model set views=5  where views is null;")
    moru_blog_trans.commit()
    print('tables created')


if __name__ == "__main__":
    main()