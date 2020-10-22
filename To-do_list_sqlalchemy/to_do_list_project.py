# To-Do list can improve your work and personal life.
# You can use it to reduce the stress in your life and get more done in less time.
# It also helps you become more reliable for other people and save time for the best things in life.

# Made with basics of SQLAlchemy to manage SQLite database


# import for creating a database file
from sqlalchemy import create_engine
# imports for creating a table in database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

# import to get access for created database
from sqlalchemy.orm import sessionmaker
# import dates
from datetime import datetime, timedelta

# creating database file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
# creating instance of declarative database mainly for table
Base = declarative_base()


class Table(Base):
    # the name of the table in db
    __tablename__ = 'task'
    # id is integer column and primary key
    id = Column(Integer, primary_key=True)
    # task is string column
    task = Column(String, default='task')
    # deadline is for test date
    deadline = Column(Date, default=datetime.today())

    # return a string representation of each row in a table
    def __repr__(self):
        am = self.deadline.strftime('%b')
        ad = self.deadline.day
        return f"{self.id}. {self.task}. {ad} {am}"


# creating database
Base.metadata.create_all(engine)
# To access the db, session is created
Session = sessionmaker(bind=engine)
session = Session()

today_day = datetime.today()
# the day of the current month
td = today_day.day
# short name of the current month
month_actual = today_day.strftime('%b')


def menu():
    while True:
        command = int(input("1) Today's tasks\n"
                            "2) Week's tasks\n"
                            "3) All tasks\n"
                            "4) Missed tasks\n"
                            "5) Add task\n"
                            "6) Delete task\n"
                            "0) Exit\n"))

        if command == 1:
            print()
            day_tasks(today_day)
        elif command == 2:
            week_tasks()
        elif command == 3:
            all_tasks()
        elif command == 4:
            missed_tasks()
        elif command == 5:
            add_task()
        elif command == 6:
            delete_task()
        # execute order 66
        elif command == 66:
            delete_table()
        elif command == 0:
            print('\nBye!')
            exit()


# showing tasks that was missed
def missed_tasks():
    missed = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
    if missed:
        for i, j in enumerate(missed):
            print(f'{i + 1}. {j.task}. {j.deadline.day} {j.deadline.strftime("%b")}')
        print()
    else:
        print('Nothing is missed!\n')


def delete_task():
    print("Choose the number of the task you want to delete:")
    rows = session.query(Table).order_by(Table.deadline).all()

    if rows:
        for i, j in enumerate(rows):
            print(f'{i + 1}. {j.task}. {j.deadline.day} {j.deadline.strftime("%b")}')
        task_to_delete = int(input())
        for i, j in enumerate(rows):
            if i + 1 == task_to_delete:
                row_to_delete = rows[i]
                session.delete(row_to_delete)
                session.commit()
                print("The task has been deleted!\n")
    else:
        print('Nothing to delete!\n')


def day_tasks(current_day, current_day_name='Today'):
    print(f"{current_day_name} {current_day.day} {current_day.strftime('%b')}:")
    day_rows = session.query(Table).filter(Table.deadline == current_day.date()).all()

    if day_rows:
        for i in day_rows:
            print(i)
        print()
    else:
        print('Nothing to do!\n')


def week_tasks():
    print()
    current_day = today_day
    for i in range(today_day.weekday(), today_day.weekday() + 7):
        day_tasks(current_day, current_day.strftime('%A'))
        current_day += timedelta(days=1)


def all_tasks():
    print('\nAll tasks:')
    rows = session.query(Table).order_by(Table.deadline).all()

    if rows:
        for i, j in enumerate(rows):
            print(f'{i + 1}. {j.task}. {j.deadline.day} {j.deadline.strftime("%b")}')
        print()
    else:
        print('Nothing to do!\n')


def add_task():
    # Write any task
    task = input('\nEnter task\n')
    # input date format is 2020-04-28
    dl = input('Enter deadline:\n')
    deadline = datetime.strptime(dl, '%Y-%m-%d').date()

    session.add(Table(task=task, deadline=deadline))
    session.commit()
    print('The task has been added!\n')


# clearing table, full delete
def delete_table():
    Base.metadata.drop_all(engine)


# starting program
if __name__ == '__main__':
    menu()
