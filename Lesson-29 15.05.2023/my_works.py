import sys


class Singleton:
    def __new__(cls, db_adress, db_port, server_port):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        else:
            print(f"You are resetting {cls.__name__} object attributes", file=sys.stderr)
            sys.stderr.flush()
        cls.__init__(cls._instance, db_adress, db_port, server_port)
        return cls._instance


class AppSettings(Singleton):
    def __init__(self, db_adress, db_port, server_port ):
        self.db_address = db_adress
        self.db_port = db_port
        self.server_port = server_port

    def get_database_address(self):
        return self.db_address

    def get_database_port(self):
        return self.db_port

    def get_server_port(self):
        return self.server_port


app_settings = AppSettings("127.0.0.1", "800", "8000")


print(app_settings.get_database_address())
print(app_settings.get_database_port())
print(app_settings.get_server_port())