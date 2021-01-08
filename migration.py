from app import db


def main():
    db.create_all()
    print('tables created')


if __name__ == "__main__":
    main()