""" SQLite operations class and methods

 Documentation used for this class
 https://www.tutorialsteacher.com/python/property-decorator
 https://www.tutorialsteacher.com/python/public-private-protected-modifiers
 https://docs.python.org/3/library/stdtypes.html#typecontextmanager
 https://docs.python.org/3/tutorial/classes.html
 https://docs.python.org/3/library/sqlite3.html
 https://peps.python.org/pep-0249/
"""

import sqlite3

class DatabaseOperation:

    """ Custom sqlite methods for database operations """

    def __init__(self, database_file):
        self._conn = sqlite3.connect(database_file)
        self._cursor = self._conn.cursor()
        # print(f"database {database_file} connected!")

    # context managers / magic methods
    def __enter__(self):
        """ context manager to allow "with" statement
        starts runtime
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ context manager exit runtime with
         exception type, value and traceback information
         in case of exception
        """
        self.db_close()

    # decorators
    @property
    def db_conn(self):
        """ Allow other methods access the protected variable "conn". """
        return self._conn

    @property
    def db_cursor(self):
        """ Allow other methods access the protected variable "cursor". """
        return self._cursor

    # methods with conn
    def db_commit(self):
        """ This method commits the current transaction. """
        self.db_conn.commit()

    def db_close(self, db_commit=True):
        """ If commit is true then commit before close the
         database conection """
        if db_commit:
            self.db_commit()
        self.db_conn.close()
        # print("database conection closed!")

    # methods with cursor
    def db_execute(self, sql, params=None):
        """ Send commands to database with one or more params. """
        self.db_cursor.execute(sql, params or ())

    def db_executemany(self, sql, params=None):
        """ Send many commands to database with one or more params. """
        self.db_cursor.executemany(sql, params or ())

    def db_fetchall(self):
        """ Fetches all (remaining) rows of a query result, returning a list. """
        return self.db_cursor.fetchall()

    def db_fetchone(self):
        """ Fetches the next row of a query result set, returning a single sequence,
         or None when no more data is available. """
        return self.db_cursor.fetchone()

    def db_query(self, sql, params=None):
        """ Send commands to database with one or more params and then fetches the
         next row of a query result set, returning a single sequence,
         or None when no more data is available. """
        self.db_cursor.execute(sql, params or ())
        return self.db_fetchone()
