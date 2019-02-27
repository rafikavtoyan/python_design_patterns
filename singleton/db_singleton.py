import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    cursor_obj = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor_obj = self.connection.cursor()
        return self.cursor_obj


db1 = Database().connect()
db2 = Database().connect()
print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
